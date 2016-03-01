

#user/bin/python
import MySQLdb
import csv
import argparse
import sys

# arg_parser = argparse.ArgumentParser()
# arg_parser.add_argument ("select p.id,p.fullname,u.id, p.case_id, u.party_id, up.unresolved_party_type_name from party p inner join party_unresolved_party_type_map u on p.id=u.id inner join unresolved_party_type up on up.id=p.id order by p.id limit 10; ")
# args = arg_parser.parse_args ()
# sys.exit ()

connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
cursor = connection.cursor()
cursor.execute("select p.id,p.fullname,u.id, p.case_id, u.party_id, up.unresolved_party_type_name from party p inner join party_unresolved_party_type_map u on p.id= u.id inner join unresolved_party_type up on up.id=p.id order by p.id limit 10; ")


records_tuple = cursor.fetchall()
	


wf = open('preemas_csv.csv', 'w')
csv_writer = csv.writer(wf, delimiter =',', quotechar='"')
for record in records_tuple:
	csv_writer.writerow(list(record))

wf.close()



