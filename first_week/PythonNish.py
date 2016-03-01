#:wq!/usr/bin/python
import MySQLdb
import csv
import argparse
import sys
import csv

def csv_writer(data, path):

    """

    Write data to a CSV file path

    """

    with open(path, "wb") as csv_file:

        writer = csv.writer(csv_file, delimiter=',')

        for line in data:

            writer.writerow(line)

def write_to_csv (csv_file, result_tuple):
        if not result_tuple:
                return None

        for each_tuple in result_tuple:
                #each_tuple values will be written to csv
                #row_tuple = (party,) + each_tuple
                csv_writer.writerow(each_tuple)

        return None


#connection = MySQLdb.connect(host='localhost', port=3350, user='root', passwd='', db='codaxtr')
connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
cursor = connection.cursor ()
#cursor.execute ("select * from party")
#cursor.execute ("select p.id,p.fullname,u.id,u.PartyType from party p inner join PartyType u on u.id=p.id order by p.id limit 10")
cursor.execute("select p.id,p.fullname,u.id,u.unresolved_party_type_name from party p inner join unresolved_party_type u on u.id=p.id order by p.id limit 10")
data = cursor.fetchall ()

csv_writer(data, "output.csv")
	



