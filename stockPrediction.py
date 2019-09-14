import csv
import pandas_datareader as pdr
from datetime import datetime

option = int(input("Select the indice:\n1. BSE \n2. NASDAQ \n"))
currentDT = datetime.now()
end_year = int(currentDT.year)
end_month = int(currentDT.month)
end_day = int(currentDT.day)

if (option == 1):
    scalar = 100
    stock = input("Select the stock: ")
    stock_file = pdr.get_data_yahoo(symbols = stock + '.ns', start = datetime(2010, 3, 30), end = datetime(end_year, end_month, end_day))
    indice_file = pdr.get_data_yahoo(symbols = "^BSESN", start = datetime(2010, 3, 30), end  = datetime(end_year, end_month, end_day))
elif (option == 2):
    scalar = 10
    stock = input("Select the stock: ")
    stock_file = pdr.get_data_yahoo(symbols = stock, start = datetime(2010, 3, 30), end = datetime(end_year, end_month, end_day))
    indice_file = pdr.get_data_yahoo(symbols = "^IXIC", start = datetime(2010, 3, 30), end  = datetime(end_year, end_month, end_day))

print("Extracted")

f_name = input("Enter the name of the file: ")
I_name = input("Enter the name of comaparator: ")

stock_close = stock_file['Close']
indice_close = indice_file['Close']/scalar

stock_close.to_csv(f_name + '.csv')
indice_close.to_csv(I_name + '.csv')
print("Saved")

f_name = f_name + '.csv'
I_name =  I_name + '.csv'

stock = []
ind = []

with open(f_name, 'r',  encoding='utf-8') as file:
    for line in file:
        data = line[11:]
        data = data.split('\n')
        data = float(data[0])
        stock.append(data)

with open(I_name, 'r',  encoding='utf-8') as file:
    for line in file:
        data = line[11:]
        data = data.split('\n')
        data = float(data[0])
        ind.append(data)

error, predict = 0, 0
a, b = 1, 1
alpha = 0.0008

for i in range(len(ind)):
    predict = a + (b * ind[i])
    error = stock[i] - predict
    a = a + (error * ind[i] * alpha)
    b = b + (error * alpha)
    print("A: %i    B: %i   Predict: %i" % (a, b, predict))

print("Finally,")
print("A is: %i     B is: %i" % (a, b))
print(a + (b * ind[i - 1]))