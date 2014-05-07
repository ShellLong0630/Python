import httplib2,urllib.request,re,os,time,mysql.connector,random
file1 = 'D:\\张玉龙\\Python\\20140314_url.txt'
file2 = 'D:\\张玉龙\\Python\\20140314_url_city.txt'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')
host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db   = 'd01_backup'
cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
cursor = cnx.cursor()
for s in f1:
    city = ""
    b = re.split(',"',s)
    localId = b[0]
    sql = 'SELECT city FROM tape_local WHERE id=%s'% localId
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        city  = result[0][0]
    string = re.sub('^'+localId+',',localId+',"'+city+'",',s)
    f2.write(string)
f1.close()
f2.close()
