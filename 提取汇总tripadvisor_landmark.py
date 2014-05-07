import re,os,mysql.connector

##host = '192.168.1.15'
##user = 'data'
##pwd  = 'skst'
##db   = 'wwere_v3'
##cnx  = mysql.connector.connect(host=host,user=user,password=pwd,database=db)
##cursor = cnx.cursor()

#f2 = open('D:\\张玉龙\\Python\\20140407_trip_landmarks.txt','w',encoding='utf-8')
f2 = open('D:\\张玉龙\\Python\\20140428_UPDATE_landmark.sql','w',encoding='utf-8')
f3 = open('D:\\张玉龙\\源文件\\20140428_tripsource_raw.csv','r',encoding='utf-8')
dic_trip = {}
for s in f3:
    
    try:
        source_trip = re.findall('tripadvisor_(g[\d]+-d[\d]+)',s)
        for t in source_trip:
            if t not in dic_trip.keys():
                dic_trip[t]=s.split(',')[0]
    except:
        print(s)
source = []
for f in os.listdir('D:\\张玉龙\\Python\\landmarks'):
    f1=open(os.path.join('D:\\张玉龙\\Python\\landmarks',f),'r',encoding='utf-8')
    for s in f1:
        if re.findall('^g',s):
            sourceId = s.split('-Reviews')[0]
            source   = set(source)
            if sourceId not in source:
                source = list(source)
                source.append(sourceId)
                if sourceId in dic_trip.keys():
                    localId = dic_trip[sourceId]
##                sql = 'SELECT localId FROM townfile_local WHERE sourceId regexp "%s"'% sourceId
##                cursor.execute(sql)
##                result = cursor.fetchall()
##                if result:
##                    localId = result[0][0]
                    u_landmark = "INSERT INTO landmark (localId,landmarkRank,tag,linkUrl,updateTime) VALUES (%s,1,'','','2014-04-28 18:00:00') ;\n"% localId
                    f2.write(u_landmark)
        else:
            pass

print(len(source))
#f2.write(str(source))
##cnx.commit()
##cursor.close()
##cnx.close()
f1.close()
f2.close()
f3.close()
