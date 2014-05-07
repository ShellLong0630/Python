import re,os,mysql.connector,shutil

path = 'D:\\张玉龙\\Python\\attractions'
goal = 'D:\\张玉龙\\Python\\trip_landmark'

host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db   = 'wwere_v3'
cnx  = mysql.connector.connect(host=host,user=user,database=db,password=pwd)
cursor=cnx.cursor()
sql = 'select l.localId,t.sourceId from landmark l left join townfile_local t on l.localId=t.localId where l.landmarkRank>0 and t.images="" and t.sourceId regexp "tripadvisor"'
cursor.execute(sql)
result = cursor.fetchall()
dic = {}
for s in result:
    sourceId = re.findall('tripadvisor_(g[\d]+-d[\d]+)',s[1])
    for t in sourceId:
        dic[t] = s[0]
for root,dirs,files in os.walk(path):
    if dirs == [] and files == []:
        pass
    elif dirs != [] and files == []:
        pass
    elif dirs == [] and files != []:
        sourceId = re.findall('(g[\d]+-d[\d]+)',root)[0]
        if sourceId in dic.keys():
            for f in files:
                if not os.path.exists(goal+'\\'+str(dic[sourceId])):
                    os.makedirs(goal+'\\'+str(dic[sourceId]))
                if not os.path.isfile(goal+'\\'+str(dic[sourceId])+'\\'+f):
                    shutil.copyfile(os.path.join(root,f),goal+'\\'+str(dic[sourceId])+'\\'+f)
    else:
        pass

cnx.commit()
cursor.close()
cnx.close()
