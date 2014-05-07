'''
import mysql.connector,re

file = 'D:\\张玉龙\\Python\\提交\\20140324_UPDATE_v3townfile_local_localNameS.sql'
f1   = open(file,'w',encoding='utf-8')
print('start')
host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db1  = 'd01_backup'
db2  = 'wwere_v3'
dic2 = {}
cnx2  = mysql.connector.connect(host=host,user=user,password=pwd,database=db2)
cursor2 = cnx2.cursor()
sql2  = 'SELECT localId,localName FROM townfile_local'
cursor2.execute(sql2)
result2= cursor2.fetchall()
for s in result2:
    dic2[s[0]]=s[1]
print('a')
cnx1  = mysql.connector.connect(host=host,user=user,password=pwd,database=db1)
cursor1 = cnx1.cursor()
sql1  = 'SELECT id,name FROM tape_local where id in %s'% list(dic2.keys())
cursor1.execute(sql1)
result1= cursor1.fetchall()
print('b')
for s in result1:
    if s[1]!=dic2[s[0]]:
        u = 'UPDATE townfile_local SET localName = "%s" WHERE localId = %s ;\n'% (name.replace('"','\\"'),s[0])
        f1.write(u)
    else:
        pass
f1.close()
'''
import mysql.connector,re

file = 'D:\\张玉龙\\Python\\提交\\20140325_UPDATE_v3townfile_local_countryId.sql'
f1   = open(file,'a',encoding='utf-8')

host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db1  = 'd01_backup'
db2  = 'wwere_v3'

cnx1  = mysql.connector.connect(host=host,user=user,password=pwd,database=db1)
cursor1 = cnx1.cursor()
cnx2  = mysql.connector.connect(host=host,user=user,password=pwd,database=db2)
cursor2 = cnx2.cursor()
sql2  = 'SELECT localId,countryId FROM townfile_local'
cursor2.execute(sql2)
result= cursor2.fetchall()
for s in result:
    sql1 = 'SELECT country FROM tape_local WHERE id = %s'% s[0]
    cursor1.execute(sql1)
    name = cursor1.fetchall()
    try:
        if name:
            name = name[0][0]
            if str(name)!=str(s[1]):
                print(str(s[0])+'  '+name+'  '+s[1])
                u = 'UPDATE townfile_local SET countryId = "%s" WHERE localId = %s ;\n'% (name.replace('"','\\"'),s[0])
                f1.write(u)
            else:
                pass
        else:
            name = ''
            print('@'+str(s[0])+'  '+s[1])
        
    except:
        print('#'+str(s[0])+'  '+name)
f1.close()

