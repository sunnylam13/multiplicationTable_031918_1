try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'The program takes a number *N* from the command line and creates an *N x N* multiplication table in an Excel spreadsheet...',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['openpyxl'],
	'scripts': [],
	'name': 'Multiplication Table Maker'
}

setup(**config)