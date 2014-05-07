import re
file = 'D:/张玉龙/Python/20140304_landmarks_update_CN_d3.txt'
file2= 'D:/张玉龙/Python/提交/20140306_UPDATE_landmark.sql'
f1   = open(file ,'r',encoding='utf-8')
f2   = open(file2,'w',encoding='utf-8')

for s in f1:
    localId = re.findall('^d([\d]+),',s)
    if localId:
        sql = 'UPDATE local_stars SET landmark = 1 WHERE localId = %s ;\n'% localId[0]
        f2.write(sql)
    else:
        pass

f1.close()
f2.close()
