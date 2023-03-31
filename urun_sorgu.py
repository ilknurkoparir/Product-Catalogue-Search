# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 07:45:20 2023

@author: Lenovo
"""

import pyodbc 

#%% PART 1: Retrieving data from a database (Access database is used).

# Connect to the Access database
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Lenovo\OneDrive\Belgeler\urun_katalogu.accdb;')

#Create a cursor
cursor = conn.cursor()

# Execute a sample query
cursor.execute('SELECT * FROM urun_katalogu1')

# Fetch the results
rows = cursor.fetchall()
for row in rows:
    print(row)
    
 

#%% 2.PART: Product inquiry operations
number = input("Please enter the product number.")
print("Entered number:",number)

# Veritabanında ürün numarasının olup olmadığını kontrol et
cursor.execute("SELECT COUNT(PRODUCT_NUMBER) FROM urun_katalogu1 WHERE PRODUCT_NUMBER = ?", (number,))
result = cursor.fetchone()[0]

# Sonuçları göster
if result > 0:
    print("Product number {} exists in the database.".format(number))
    product_name, other_info = row[0], row[1]
    print("Product name: ", product_name)
    print("Other info: ", other_info)
else:
    print("Product number {} does not exist in the database.".format(number))

# Close the connection
conn.close()  





    
    
    
    