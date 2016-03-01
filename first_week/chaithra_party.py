




#!/usr/bin/env python
  
import MySQLdb
import csv

def main():
        connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
        mysql_cursor=connection.cursor()
        mysql_cursor.execute("select p.id,p.fullname,up.unresolved_party_type_name,m.id from party as p inner join party_unresolved_party_type_map as m on p.id=m.party_id inner join unresolved_party_type as up on m.unresolved_party_type_id=up.id order by p.id limit 10")
        result_set = mysql_cursor.fetchall()
#       print result_set
        for row in result_set:
                print row


        f = open("mypartyfile.csv","wb")
        fwriter = csv.writer(f,quoting=csv.QUOTE_ALL)
	fwriter.writerow(['ID','Full name','party type','map id'])

    
        for col in result_set:
                fwriter.writerow(col)
        f.close()
        return 0


if __name__ == '__main__':
        main()

