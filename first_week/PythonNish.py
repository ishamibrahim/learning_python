#!/usr/bin/python
import MySQLdb
import csv
import argparse

import sys
import party 
from unresolved_party_type import unresolved_party_type_name

connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')

cursor = connection.cursor ()
cursor.execute ("select p.id,p.fullname,u.id,u.unresolved_party_type_name from party p inner join unresolved_party_type u on u.id=p.id order by p.id limit 10")
data = cursor.fetchall ()
print row[0], row[1]
cursor.close ()
connection.close()

def write_to_csv (csv_file, result_tuple):
                if not result_tuple:
                        return None

                for each_tuple in result_tuple:
                        #each_tuple values will be written to csv
                        row_tuple = (party,) + each_tuple
                        csv_writer.writerow(row_tuple)

                return None
sys.exit()

