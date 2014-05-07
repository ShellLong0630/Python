import re,os

file1 = 'D:\\张玉龙\\源文件\\20140409_rank_raw.csv'
file2 = 'D:\\张玉龙\\Python\\提交\\20140409_UPDATE_landmarkRank.sql'
#file2 = 'D:\\张玉龙\\Python\\20140409_rank_raw.txt'
f3    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')
rank_dic = {}
for f in os.listdir('D:\\张玉龙\\Python\\tripadvisor'):
    f1 = open(os.path.join('D:\\张玉龙\\Python\\tripadvisor',f),'r',encoding='utf-8')
    content = f1.read()
    order = re.findall('排名第<span class="">([\d]+)</span></b> \(共 ([\d]+) ',content)
    rank  = re.findall('" alt="([\S]+)分" content=',content)
    if rank:
        rank=rank[0]
    else:
        rank=1
    #print
    if order:
        if len(order[0])==2:
            #print(order[0][0],rank,f)
            sourceId = f.split('.')[0]
            landmarkRank = int((1-float(order[0][0])/float(order[0][1]))*1.5*float(rank))
            if landmarkRank == 0:
                landmarkRank = 1
            string = '%s,%s\n'% (sourceId,landmarkRank)
            rank_dic[sourceId] = landmarkRank
            #print(string)
            #f2.write(f.split('.')[0]+','+str(int(((1-float(order[0][0])/float(order[0][1]))*1.5*float(rank[0]))))+'\n')
            #f2.write(string)
            #break
    f1.close()

for s in f3:
    localId  = s.split(',')[0]
    sourceId = re.findall('tripadvisor_(g[\d]+-d[\d]+)',s)[0]
    if sourceId in rank_dic.keys():
        sql = 'UPDATE landmark SET landmarkRank = %s, updateTime = "2014-04-09 10:30:00" WHERE localId = %s;\n'% (rank_dic[sourceId],localId)
        f2.write(sql)
f2.close()
f3.close()
