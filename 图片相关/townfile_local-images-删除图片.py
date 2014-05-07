import re,mysql.connector
file = 'D:\\张玉龙\\源文件\\photos_bad.txt'
f1   = open(file,'r',encoding='utf-8')
f2   = open('D:\\张玉龙\\Python\\提交\\20140331_UPDATE_images.sql','w',encoding='utf-8')
host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db   = 'wwere_v3'
total= 9099767
cnx = mysql.connector.connect(host=host,user=user,database=db,password=pwd)
cursor = cnx.cursor()

for s in f1:
    image = 'wwere_%s%s/%s'% (s[0],s[1],s.replace('\n',''))
    sql = 'SELECT localId,images FROM townfile_local WHERE images regexp "%s"'% image
    cursor.execute(sql)
    result = cursor.fetchall()
    for t in result:
        images = re.split(';',t[1])
        #print(images)
        images.remove(image)
        #print(images)
        images = str(images).replace(']','').replace('[','').replace(', ',';').replace("'",'')
        sql_i = 'UPDATE townfile_local SET images = "%s" WHERE localId = %s ;\n'% (images,t[0])
        #print(sql_i)
        f2.write(sql_i)       

f1.close()
f2.close()
