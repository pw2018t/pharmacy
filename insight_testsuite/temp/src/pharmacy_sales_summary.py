#!/usr/bin/env python3

"""
 pharmacy_sales_summary.py
 
 The scripts reads the pharmacy raw datafile and gives the summary
 aggregates on druglevel. The script creates the output file that 
 has the summary :- 
  - No. of unique drug subcriber
  - Total sales amount of drug
 
"""

import csv
from collections import defaultdict,Counter,OrderedDict
from operator import itemgetter
from timer import timeit
import sys

#-----------------------------------------------------------------------

#=======================================================================
# Writing functions
#=======================================================================

@timeit
def read_pharmacy_input(infile):
	"""
	This function reads the pharamcy file and returns
	the counter and dictionary for the total sale and
	unique subscribers.
	"""
	records = []
	drug_count= defaultdict(set)
	drug_cost= Counter()
	try:
		with open(infile) as rows:
			reader = csv.reader(rows)
			headers=next(reader) # skip the header row
			for rowno,row in enumerate(reader,start=1):
				try:
					drug_count[row[3]].add(row[1]+row[2])
					drug_cost[row[3]]+=int(row[4])
				except ValueError as err:
					print ('Row: ', rowno, 'bad row: ', row)
					print ('Row: ', rowno, 'Reason: ', err)
					continue  # skips to the next row
	except IOError:
		print (" File not found ")
		print ("File name: ", infile)
	return drug_count,drug_cost

@timeit
def create_summary(targetfile,drug_count,drug_cost):
	"""
	This function creates takes the output file name and creates the output
	summary file.
	"""
	with open(targetfile, 'a') as tfile:
		l=0
		for key,val in drug_cost.items():
			l+=1
			try:
				if l == 1:
					header = 'drug_name,num_prescriber,total_cost\n'
					tfile.write(header)
				wval = key+','+str(len(drug_count[key]))+','+str(val)+'\n'
#				wval = '"'+key+'"'+','+str(len(drug_count[key]))+','+str(val)+'\n'
				tfile.write(wval)
			except Exception as error:
				print(error)
				raise 

@timeit
def main(infile,targetfile):
	"""
	this function executes and create output file
	"""
	drug_count,drug_cost = read_pharmacy_input(infile)
	drug_cost = OrderedDict(sorted(drug_cost.items(), key=itemgetter(1), reverse=True))
	create_summary(targetfile,drug_count,drug_cost)

if __name__ == '__main__':
	infile = sys.argv[1]
	targetfile = sys.argv[2]
	main(infile,targetfile)
