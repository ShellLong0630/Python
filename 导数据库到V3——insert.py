import re

file1 = 'D:\\张玉龙\\Python\\提交\\20140327_INSERT_v3shop_local_part3.sql'
file2 = 'D:\\张玉龙\\Python\\提交\\20140327_INSERT_v3shop_local_3.sql'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'a',encoding='utf-8')
i=0
for s in f1:
    if re.findall('^INSERT',s):
        ##shoplocal的字段替换
        s = re.sub(',null',",''",s,flags=re.I)
        s = s.replace('`','')
        s = s.replace('id,rank,phoneNumber,businessArea,avgCost,priceSymbol,parking,traffic,shopHours,24h,suit,feature,recommend,shopUrl,updateTime',
                      'localId,shopRank,phoneNumber,businessArea,avgCost,priceSymbol,parking,traffic,shopHours,24h,suit,feature,recommend,shopUrl,updateTime')

        
        ##townfile_local的字段替换
##        s = re.sub(',null',",''",s,flags=re.I)
##        s = s.replace('`','')
##        s = s.replace('id,star,lat,lng,country,cityId,address,sourceId,name,alias,catId,parentId,createTime,updateTime',
##                      'localId,star,lat,lng,countryId,cityId,address,sourceId,localName,aliasName,catId,parentId,createTime,updateTime')
##        s = s.replace(",'中国',",",'CN',")
        #s = s.replace(');',",'2014-03-24 12:00:00','2014-03-24 12:00:00');")
        if i<10:
            i+=1
            print(s)
        f2.write(s)
f1.close()
f2.close()
