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

multi_number_cmdline = sys.argv[1] # should be the first argument in the command line i.e. the number, if you use 0 you get the program name

logging.debug('The command line value entered for the max multi-table value is:  %s' % (multi_number_cmdline))

# create the frozen header row

# for x in range():
# 	pass

# create the frozen header column



# save the final sheet

# wb.save('multiTable.xlsx')