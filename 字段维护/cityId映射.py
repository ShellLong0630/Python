import re,mysql.connector,json
file1 = 'D:\\张玉龙\\源文件\\20140421_tripsource.csv'
file2 = 'D:\\张玉龙\\Python\\cityId_cityName_trip.txt'
file3 = 'D:\\张玉龙\\Python\\临时存放\\POIs_tripadvisor_20131210.txt'
f1    = open(file1,'r',encoding='utf-8')
f3    = open(file3,'r',encoding='utf-8')
f2    = open(file2,'a',encoding='utf-8')
##host  = '192.168.1.15'
##user  = 'data'
##pwd   = 'skst'
##db    = 'wwere_v3'
##cnx   = mysql.connector.connect(host=host,user=user,database=db,password=pwd)
##cursor= cnx.cursor()

dic1 = {}
for s in f1:
    sourceId = re.findall('tripadvisor_(g[\d]+)-',s)
    if sourceId:
        sourceId = sourceId[0]
        b = re.split('"|,|\n',s)
        if sourceId not in dic1.keys():
            dic1[sourceId] = [b[-2],b[-4]]
#content = f1.read()
dic3 = {}
for s in f3:
    j = json.loads(s)
    if re.split('_|-',j['sourceId'])[1] not in dic3.keys():
        if re.split('_|-',j['sourceId'])[1] in dic1.keys():
            dic3[re.split('_|-',j['sourceId'])[1]] = [j['country'],j['provice'],j['city'],dic1[re.split('_|-',j['sourceId'])[1]][0],dic1[re.split('_|-',j['sourceId'])[1]][1]]
dic = {}
for s in dic3:
    if dic3[s][0] and dic3[s][1] and dic3[s][2]:
        string = dic3[s][0]+'~'+dic3[s][1]+'~'+dic3[s][2]
        if string not in dic.keys():
            dic[string]=[dic3[s][3],dic3[s][4]]
            string = '%s,"%s","%s","%s","%s"\n'% (dic3[s][3],dic3[s][4],dic3[s][0],dic3[s][1],dic3[s][2])
            f2.write(string)

print(len(dic.keys()))
f2.write(str(dic).replace(',',',\n'))    


f3.close()
f2.close()
