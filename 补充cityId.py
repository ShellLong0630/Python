import re,mysql.connector

##host = '192.168.1.15'
##user = 'data'
##db   = 'wwere_v3'
##pwd  = 'skst'
##
##cnx  = mysql.connector.connect(host=host,user=user,database=db,password=pwd)
##cursor= cnx.cursor()
##
##file1 = 'D:\\张玉龙\\Python\\20140418_cityId_update_6.txt'
##file2 = 'D:\\张玉龙\\Python\\20140418_cityId_update_7.txt'
##f1    = open(file1,'r',encoding='utf-8')
##f2    = open(file2,'w',encoding='utf-8')
##
##for s in f1:
##    if re.findall(',0$',s):
##        b = re.split('"',s)
##        sql = 'SELECT cityId FROM city WHERE countryId = "%s" and province = "%s" and cityName = "%s"'% (b[1],b[3],b[5])
##        cursor.execute(sql)
##        result = cursor.fetchall()
##        if result:
##            f2.write(s.replace(',0\n',','+str(result[0][0])+'\n'))
##        else:
##            f2.write(s)
##    else:
##        f2.write(s)
##cnx.commit()
##cursor.close()
##cnx.close()
##f1.close()
##f2.close()

file1 = 'D:\\张玉龙\\源文件\\20140418_cityId_raw.csv'
file2 = 'D:\\张玉龙\\Python\\20140418_cityId_update_7.txt'
file3 = 'D:\\张玉龙\\Python\\提交\\20140420_UPDATE_cityId.sql'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'r',encoding='utf-8')
f3    = open(file3,'w',encoding='utf-8')
dic   = {}
for s in f2:
    b = re.split('"',s)
    c = re.split(',|\n',s)
    country = b[1]
    province= b[3]
    city    = b[5]
    address = re.sub('^中国'+province+city,'',b[7])
    dic[c[0]]=[b[1],address,c[-2]]
for s in f1:
    b = re.split('"',s)
    localId = s.split(',')[0]
    if localId in dic.keys():
        sql_c = 'UPDATE townfile_local SET cityId = %s, updateTime = "2014-04-20 16:30:00" WHERE localId = %s;\n'% (dic[localId][2],localId)
        f3.write(sql_c)
        if not b[1]:
            sql_t = 'UPDATE townfile_local SET countryId = "%s" WHERE localId = %s;\n'% (dic[localId][0],localId)
            f3.write(sql_t)
        if not b[3]:
            sql_a = 'UPDATE townfile_local SET address = "%s" WHERE localId = %s;\n'% (dic[localId][1],localId)
            f3.write(sql_a)

f1.close()
f2.close()
f3.close()
