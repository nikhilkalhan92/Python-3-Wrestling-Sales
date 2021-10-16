import gspread
from google.oauth2.service_account import Credentials
import pandas as pd # This is used to read the csv and show data for a particular column

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('data')

sales = SHEET.worksheet('data')

data = sales.get_all_values()

print(data)

class Sales_insight:

	def __init__(self,file):
		# Initialising all variables that'll be used across different functions/methods
		file_read = open('data.csv','r')
		self.data = file_read.readlines()[1:] # Indexing from 1 to not read the columns as general data
		self.sales = {}
		self.avg_sales = {}
		self.df = pd.read_csv('data.csv') # Creating dataframe using pandas
	
	def average(self):
		for line in self.data: 
			temp_var = line.split(',') # Getting all data present in the iterated line
			val_sum = 0
			for x in temp_var[1:]:
				try:
					if '\n' in x:
						x = x[:-1]
					val_sum+=float(x)
				except:
					break
			if len(temp_var[0])>3:
				self.avg_sales[temp_var[0]] = val_sum/len(temp_var[1:]) # Adding the data for all dates into the dictionary

		print('Sales Average across different days :\n') # Iterating through dictionary to print average sales for all dates
		for i in self.avg_sales:
			print(f"{i} : {self.avg_sales[i]}")

	def max_sales(self):
		for line in self.data:
			temp_var = line.split(',')
			val_sum = 0
			for x in temp_var[1:]:
				if len(temp_var[0])>3:
					val_sum+=float(x)
			if len(temp_var[0])>3:
				self.sales[temp_var[0]] = val_sum

		# In the bottom section we are using simple linear search algorithm to get maximum sales
		max_val = 0
		date = None
		for j in self.sales:
			if self.sales[j]>max_val:
				max_val=self.sales[j]
				date = j
		print(f'Maximum sales took place on {date} worth {max_val}')

	def read_data(self):
		date = str(input('Enter Date : '))
		data_point = {}
		for line in self.data:
			temp_var = line.split(',')
			if temp_var[0] == date and len(temp_var[0])>3:
				data_point['Kenny Omega T Shirt'] = temp_var[1]
				data_point['Young bucks Tshirt'] = temp_var[2]
				data_point['Cody T shirt'] = temp_var[3]
				data_point['Hangman T shirt'] = temp_var[4]
				data_point['Adam Cole T shirt'] = temp_var[5]
				data_point['Chris Jericho T shirt'] = temp_var[6]

		for y in data_point:
			print(f'{y} : {data_point[y]}')

	def add_data(self):
		print('Please input Sales data for following ')
		date = str(input('Enter Date : '))
		kt = str(input('Kenny Omega T Shirt : '))
		yb = str(input('Young bucks Tshirt : '))
		ct = str(input('Cody T shirt : '))
		ht = str(input('Hangman T shirt : '))
		ac = str(input('Adam Cole T shirt : '))
		cj = str(input('Chris Jericho T shirt : '))
		file_open = open('data.csv','a',newline='') # Opening the file in append mode, newline = '' means to write new row in next line
		writer = csv.writer(file_open) # Initialising the writer
		writer.writerow([date,kt,yb,ct,ht,ac,cj]) # Writing the row
		file_open.close() 
		print('Data added succesfully!')

	def tshirt_search(self):
		tshirt = str(input('Tshirt name : '))
		try:
			print(self.df[tshirt])
		except:
			print('Please check if you have entered correct column name')


class_object = Sales_insight('data.csv')
print('Welcome to Sale management App')
while True:
	print('\n\n1)Calculate average sales\n2)Get maximum sales \n3)Read data for particular day\n4)Add Data\n5)Search Tshirt\n6)Exit')
	inp = int(input('Your input : '))
	if inp == 1:
		class_object.average()
	elif inp == 2:
		class_object.max_sales()
	elif inp == 3:
		class_object.read_data()
	elif inp == 4:
		class_object.add_data()
	elif inp == 5:
		class_object.tshirt_search()
	elif inp == 6:
		break
	else:
		print('Error! Invalid input')