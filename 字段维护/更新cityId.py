import mysql.connector

file   ='d:\\张玉龙\\Python\\提交\\20140326_UPDATE_cityId.sql'
f1     =open(file,'w',encoding='utf-8')
user   ='data'
pwd    ='skst'
host   ='192.168.1.15'
db     ='d01_backup'
cnx    = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
cursor = cnx.cursor()
#sql    = 'select l.localId,m.cityId from (wwere_v3.townfile_local l left join d01_backup.tape_local t on l.localId=t.id) left join d01_backup.city m on t.country=m.country and t.provice=m.provice and t.city=m.city where l.cityId=0 and length(t.country)=2 and length(t.provice)>0 and length(t.city)>0'
sql1 = 'select l.localId,t.country,t.provice,t.city from wwere_v3.townfile_local l left join d01_backup.tape_local t on l.localId=t.id where l.cityId=0 and length(t.country)=2 and length(t.provice)>0 and length(t.city)>0'
cursor.execute(sql1)
result = cursor.fetchall()#[0][0]
print('a')
dic_city = {}
for s in result:
    dic_city[s[0]]=(s[1],s[2],s[3])
    sql2 = 'SELECT cityId FROM city WHERE country = "%s" and provice = "%s" and city = "%s"'% (s[1],s[2],s[3])
    cursor.execute(sql2)
    cityId = cursor.fetchall()
    if cityId:
        sql = 'UPDATE townfile_local SET cityId = %s WHERE localId = %s ;\n'% (cityId[0][0],s[0])
        f1.write(sql)
    else:
        print(s)
#print(result)

cnx.commit()
cursor.close()
cnx.close()
f1.close()
#print('"'+result[0][0]+'"')
##print(bool(result[3]))
