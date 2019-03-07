
import os
import csv

file_dir=os.path('budget_data.csv')
with open(file_dir,newline='') as newfile:
    nfile_reader=csv.reader(newfile,delimiter=',')
