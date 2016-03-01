#!/usr/bin/python
import MySQLdb
import csv
connection = MySQLdb.connect(host='localhost', user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
cur= connection.cursor()
query="select p.id,p.fullname,p.prefix,p.fname,p.mname,p.lname,p.suffix,upt.unresolved_party_type_name from party p inner join party_unresolved_party_type_map as ptm on ptm.party_id=p.id inner join unresolved_party_type upt on upt.id=ptm.unresolved_party_type_id order by p.id desc limit 10;"
cur.execute(query)   
result = cur.fetchall()
for row in result:
	id=row[0]
	fullname=row[1]
	prefix=row[2]
	fname=row[3]
	mname=row[4]
	lname=row[5]
	suffix=row[6]
	unresolved_party_type_name=row[7]
	print "id=%d\nfullname=%s\nprefix=%s\nfname=%s\nmname=%s\nlname=%s\nsuffix=%s\nunresolved_party_type_name=%s\n"%(id,fullname,prefix,fname,mname,lname,suffix,unresolved_party_type_name)
f=open('p.csv','wb')
mf=csv.writer(f)
mf.writerow(('Id','Fullname','Prefix','Fname','Mname','Lname','Suffix','Party Type'))
mf.writerows(result)
f.close()
connection.close()
