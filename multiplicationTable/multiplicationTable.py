# -*- coding: utf-8 -*-

#! python3

import openpyxl, sys

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

# parse the command line

# multi_number_cmdline = sys.argv[1] # should be the first argument in the command line i.e. the number, if you use 0 you get the program name

multi_number_cmdline = "3" # set for purposes of testing, disable at end of development

logging.debug('The command line value entered for the max multi-table value is:  %s' % (multi_number_cmdline))

# create the frozen header row

for x in range(2,int(multi_number_cmdline) + 2):  # since you started the loop at 2, then you need to shift the ending value by 2
	column_letter = get_column_letter(x)
	# the row stays the same i.e. 1
	logging.debug('The current header column letter is:  %s' % (column_letter))
	sheet[column_letter + '1'] = x # set that cell to the current x value in the loop
	logging.debug('The current header column letter and row number changed is:  %s' % (column_letter + '1'))

# create the frozen header column

for x in range(2,int(multi_number_cmdline) + 2):
	sheet["A" + x] = x
	logging.debug('The current header column letter and row number changed is:  %s' % ("A" + x))

# save the final sheet

# wb.save('multiplicationTable.xlsx')
