# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlrd
from bs4 import BeautifulSoup 


workbook = xlrd.open_workbook("test.xlsx")
worksheet = workbook.sheet_by_name('Sheet1')
#print(worksheet.cell(0,0).value)
#print(worksheet.cell(0,0).value)
#print(worksheet.cell(0,1).value)

  
# Reading the data inside the xml 
# file to a variable under the name  
# data 
with open('items.xml', 'r') as f: 
    data = f.read() 
  
# Passing the stored data inside 
# the beautifulsoup parser, storing 
# the returned object  
Bs_data = BeautifulSoup(data, "xml") 
  
# Finding all instances of tag  
# `unique` 
b_unique = Bs_data.find_all('chotas') 
  
print(b_unique) 



# Using find() to extract attributes  
# of the first instance of the tag 
b_name = Bs_data.find('items', {'name':'Frank'}) 
  
print(b_name) 
  

# Extracting the data stored in a 
# specific attribute of the  
# `child` tag 
value = b_name.get('test') 
  
print(value) 

























