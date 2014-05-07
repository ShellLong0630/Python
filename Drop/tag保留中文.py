import re
f1=open('D:\\张玉龙\\Python\\提交\\20140319_INSERT_v3landmark.sql','r',encoding='utf-8')
f2=open('D:\\张玉龙\\Python\\提交\\20140319_INSERT_v3landmark_2.sql','w',encoding='utf-8')
for s in f1:
    tag = re.findall(",'([\S]+,[a-z A-Z]+)','",s)
    if tag:
        tag = tag[0]
        string = s.replace(tag,re.split(',',tag)[0])
        f2.write(string)
    else:
        print(s)
        f2.write(s)
f1.close()
f2.close()
