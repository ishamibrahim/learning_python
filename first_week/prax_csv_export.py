#!/usr/bin/python
import MySQLdb as mdb
import csv
import re
#-------------[ Get party information from db & export to a CSV file ]-------------------
con = mdb.connect("localhost","codaxtr_user","c0d@xtr","codaxtr")
print (' ')
print ('------> Connected to DB successfully.......')
# prepare a cursor object using cursor() method
cur = con.cursor()
# execute SQL query using execute() method.
keyword = raw_input('------> Please enter party name to search: ')
if not re.match("^[a-zA-Z0-9_\s?]*$", keyword):
 print "Invalid characters entered. Enter only aplhabets & numbers"
else:
 query="SELECT c.case_number as CASE_NUM,p.fullname as PARTY_NAME,upt.unresolved_party_type_name as PARTY_TYPE \
       FROM party as p INNER JOIN party_unresolved_party_type_map as pt on p.id=pt.party_id \
       INNER JOIN courtcase as c on c.id=p.case_id \
       INNER JOIN unresolved_party_type as upt on upt.id= pt.unresolved_party_type_id \
       WHERE fullname like %s limit 25"
 cur.execute(query,('%'+keyword+'%',))
 # Fetch single row using fetchone() method. To fetch all rows use fetchall()
 data = cur.fetchall()
 if data:
 # if(len(data))>25:
  # print '------> Found more than 25 records found matching the keyword [',keyword,'.Only the the first 25 records are displayed'
  #else:
  print '------>', len(data),'records found matching the keyword [' ,keyword,']'
  desc = cur.description
  print "  %s      %s                %s" % (desc[0][0], desc[1][0], desc[2][0])
  for row in data:
   print "%s      %s         %s" % row
   file = open('export_party.csv', 'wb')
   writer = csv.writer(file)
  for row in data :
   writer.writerow(row)
  print ('-----> Result successfully exported to CSV file.......')
  print ('------------ <<< End Of Result >>> -------- ')
 else:
  print 'No results to display'
 cur.close()
con.close()
print (' ')
#-------------------------------------- [end of File]--------------------------------------
