import re
file1 = 'D:\\张玉龙\\源文件\\20140317_landmarks_tag_raw.txt'
file2 = 'D:\\张玉龙\\Python\\提交\\201403\\20140317_landmarks_tag_update.txt'
file3 = 'D:\\张玉龙\\Python\\提交\\20140319_UPDATE_tag.sql'
#file4 = ''
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'r',encoding='utf-8')
f3    = open(file3,'w',encoding='utf-8')
#f4    = open(file4,'w',encoding='utf-8')

dic_raw = {}

for s in f1:
    b = re.split(',|\n',s)
    c = re.split('"',s)
    localId = b[0]
    name    = c[1]
    tag     = c[3]
    mark    = int(b[-3])
    dic_raw[localId] = (name,tag,mark)
for s in f2:
    b = re.split(',|\n',s)
    c = re.split('"',s)
    localId = b[0]
    name    = c[1]
    tag     = c[3]
    mark    = int(b[-3])
    if mark==0:
        sql = 'UPDATE local_stars SET landmark = 0 WHERE localId = %s ;\n'% localId
        f3.write(sql)
    else:
        if name!=dic_raw[localId][0]:
            tape_sql = 'UPDATE tape_local SET name = "%s" WHERE id = %s ;\n'% (name,localId)
            town_sql = 'UPDATE townfile_local SET localName = "%s" WHERE localId = %s ;\n'%(name,localId)
            f3.write(tape_sql)
            f3.write(town_sql)
        if tag!=dic_raw[localId][1]:
            tag_sql  = 'UPDATE townfile_local SET tag = "%s" WHERE localId = %s ;\n'% (tag,localId)
            f3.write(tag_sql)
f1.close()
f2.close()
f3.close()
    
