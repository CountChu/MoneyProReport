#
# FILENAME.
#       money_logger.py - Money Logger Python App.
#
# FUNCTIONAL DESCRIPTION.
# 		The app reads the latest CSV file and generates money log files for all dates.
#
# 		The latest CSV file is read from the data directory where files are 
# 		sorted by file names. 
#
#		The log files are generated in the output directory, and each file is for
#		each date.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2023/10/11
#       Updated on 2023/11/1
#

import argparse

import os
import pandas as pd
import datetime

import util

import pdb 
br = pdb.set_trace

def build_args():
    desc = '''
    Usage 1: Generate all log files for all dates read from the latest CSV file. 
    	python money_logger.py

    Usage 2: Generate one log file for the given date from the latest CSV file.
    	python money_logger.py -d 2023-09-15
'''

    #
    # Build an ArgumentParser object to parse arguments.
    #

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

	#
	# Anonymous arguments.
	#

    parser.add_argument(
            '-d',
            dest='date',
            help='E.g., 2023-09-15')  	

    #
    # Check arguments.
    #

    args = parser.parse_args()	

    return args


def extract_date(value):
	date_str = value.split(' ')[0]
	date_obj = datetime.datetime.strptime(date_str, '%Y/%m/%d')
	out = datetime.datetime.strftime(date_obj, '%Y-%m-%d')

	return out

def extract_time(value):
	out = value.split(' ')[1]
	return out

def strip(value):
	return value.strip()

def update_money(value):
	if value[-3:] == '.00':
		value = value[:-3] + '   '
	return value

def write_daily(fn, df):
	print('Writing %s' % fn)
	f = open(fn, 'w')

	width = 0
	for row in df.iterrows():
		Amount = row[1]['金額']
		width = max(width, len(Amount))

	for row in df.iterrows():
		Time = row[1]['Time']
		Class = row[1]['分類']
		Memo = row[1]['敘述']
		Amount = row[1]['金額']
		Account = row[1]['帳戶']
		AccountTo = row[1]['帳戶（到）']
		TransClass = row[1]['交易類型']
		if TransClass == '資金轉帳':
			fmt = '%%s | %%%ds | %%s ---> %%s\n' % width
			f.write(fmt % (Time, Amount, Account, AccountTo))			
		else:
			fmt = '%%s | %%%ds | %%s | %%s\n' % width
			f.write(fmt % (Time, Amount, Class, Memo))

	f.close()

def main():

	#
	# Read arguments.
	#

	args = build_args()

	#
	# Get files in the data directory.
	#

	#
	# Get the latest CSV file.
	#

	csv = util.get_latest_csv('data')

	#
	# Parse csv.
	#

	df = pd.read_csv(csv)

	df.fillna('', inplace=True)

	df['Date'] = df['日期'].apply(extract_date)
	df['Time'] = df['日期'].apply(extract_time)
	df['分類'] = df['分類'].apply(strip)
	df['敘述'] = df['敘述'].apply(strip)
	df['金額'] = df['金額'].apply(update_money)

	#
	# If -d 
	#

	if args.date != None:
		df = df[df['Date'] == args.date]	

	Date_ls = df['Date'].unique()
	for Date in Date_ls:
		out_fn = os.path.join('output', '%s.txt' % Date)
		df2 = df[df['Date'] == Date]

		write_daily(out_fn, df2)


if __name__ == '__main__':
	main()