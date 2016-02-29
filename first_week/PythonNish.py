
 #!/usr/bin/python
import MySQLdb
import csv
import argparse
import sys


connection = MySQLdb.connect(host='localhost', port=3350, user='root', passwd='', db='codaxtr')

cursor = connection.cursor ()
#cursor.execute ("select * from party")
#cursor.execute ("select p.id,p.fullname,u.id,u.PartyType from party p inner join PartyType u on u.id=p.id order by p.id limit 10")
cursor.execute("select p.id,p.fullname,u.id,u.unresolved_party_type_name from party p inner join unresolved_party_type u on u.id=p.id order by p.id limit 10")
data = cursor.fetchall ()


for item in data:
	print item

def write_to_csv (csv_file, result_tuple):
                if not result_tuple:
                        return None

                for each_tuple in result_tuple:
                        #each_tuple values will be written to csv
                        row_tuple = (party,) + each_tuple
                        csv_writer.writerow(row_tuple)

                return None
