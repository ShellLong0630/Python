import re

file1 = 'D:\\张玉龙\\Python\\在哪catId_11.txt'
file3 = 'D:\\张玉龙\\源文件\\在哪catId_0.csv'
file4 = 'D:\\张玉龙\\源文件\\在哪catId_18.csv'
file5 = 'D:\\张玉龙\\源文件\\在哪catId_34.csv'
file6 = 'D:\\张玉龙\\源文件\\在哪catId_else.csv'
file2 = 'D:\\张玉龙\\Python\\提交\\20140327_UPDATE_v3category.sql'
file7 = 'D:\\张玉龙\\Python\\资料保存\\catId_parentId.txt'
f1    = open(file7,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')

for s in f1:
    b=re.split(',',s)
    sql = 'UPDATE townfile_category SET parentIds = "%s,0" WHERE catId = %s ;\n'% (b[2],b[0])
    f2.write(sql)
    
f1.close()
f2.close()
