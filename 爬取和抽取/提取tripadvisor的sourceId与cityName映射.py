import json,re

file = 'D:\\张玉龙\\Python\\临时存放\\POIs_tripadvisor_20131210.txt'
file2 = 'D:\\张玉龙\\Python\\tripadvisor_source_country_province_city.txt'
f1   = open(file,'r',encoding='utf-8')
f2   = open(file2,'w',encoding='utf-8')

dic = {}
for s in f1:
    j = json.loads(s)
    if j['sourceId'] not in dic.keys():
        dic[re.split('_|-',j['sourceId'])[1]] = [j['country'],j['provice'],j['city']]
    #print(dic[re.split('_|-',j['sourceId'])[1]])
    #break
print(len(dic.keys()))
f2.write(str(dic))
f1.close()
f2.close()
