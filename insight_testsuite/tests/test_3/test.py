import sys
sys.path.append("../../../src")
from pharmacy_sales_summary import read_pharmacy_input,create_summary
import unittest
import csv

class testMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_read_pharmacy_input(self):
        drug_count,drug_cost = read_pharmacy_input('./input/testrecords.txt')
        self.assertTrue(drug_cost['HCL']==30)
        self.assertTrue(len(drug_count['HCL'])==3)

    def test_create_summary(self):
        drug_count,drug_cost = read_pharmacy_input('./input/testrecords.txt')
        create_summary('./output/testout.txt',drug_count,drug_cost)
        with open('./output/testout.txt') as f:
            rows = csv.reader(f)
            for row in rows:
                if row[0] == 'HCL':
                    self.assertTrue(row[1]=='3')
                    self.assertTrue(row[2]=='30')

