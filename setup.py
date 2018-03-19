try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'The program takes a number *N* from the command line and creates an *N x N* multiplication table in an Excel spreadsheet...',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/multiplicationTable_031918_1',
	'download_url': 'https://github.com/sunnylam13/multiplicationTable_031918_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['openpyxl'],
	'scripts': [],
	'name': 'Multiplication Table Maker'
}

setup(**config)