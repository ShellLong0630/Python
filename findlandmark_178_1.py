import re,os,mysql.connector,shutil

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
        ori = '/data/Tripadvisor/Photos/%s/%s' % (t[0:4],t)
        to  = '/data/Tripadvisor/landmark/%s'% s[0]
        dic[t] = [s[0],ori,to]
for key in sorted(dic.items(), key=lambda d:d[0]):
    k=key[0]
    if os.path.exists(dic[k][1]):
        for root,dirs,files in os.walk(dic[k][1]):
            if dirs == [] and files == []:
                pass
            elif dirs != [] and files == []:
                pass
            elif dirs == [] and files != []:
                for f in files:
                    if not os.path.exists(dic[k][2]):
                        os.makedirs(dic[k][2])
                    if not os.path.isfile(dic[k][2]+'/'+f):
                        print(dic[k][1],f)
                        shutil.copyfile(dic[k][1]+'/'+f),dic[k][2]+'/'+f))
            else:
                pass
    else:
        print(k,'not found!')

cnx.commit()
cursor.close()
cnx.close()
