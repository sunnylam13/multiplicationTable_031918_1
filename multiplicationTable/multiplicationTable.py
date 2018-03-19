# -*- coding: utf-8 -*-

#! python3

import openpyxl

try:
	from openpyxl.cell import column_index_from_string,get_column_letter
except ImportError:
	from openpyxl.utils import column_index_from_string,get_column_letter

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

wb = openpyxl.Workbook() # create the workbook
sheet = wb.active # switch to the active sheet, there should only be one
sheet.title = "Multi Table" # rename the sheet

# get the user input

print("""
		Please enter the highest number of the multiplication table.\n
		i.e. if you want a 6 x 6 multiplication table, please enter 6.
	""")
user_input = input(">  ")

# create the frozen header row

for x in range():
	pass

# create the frozen header column



# save the final sheet

# wb.save('multiTable.xlsx')