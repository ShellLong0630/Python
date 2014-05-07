import re

file1 = 'D:\\张玉龙\\Python\\提交\\20140324_countryId.csv'
file2 = 'D:\\张玉龙\\Python\\提交\\20140324_address.csv'
file3 = 'D:\\张玉龙\\Python\\提交\\20140325_catId-parentId.csv'
file4 = 'D:\\张玉龙\\Python\\提交\\20140325_UPDATE_v3townfile_local.sql'

f1   = open(file1,'r',encoding='utf-8')
f2   = open(file2,'r',encoding='utf-8')
f3   = open(file3,'r',encoding='utf-8')
f4   = open(file4,'w',encoding='utf-8')

for s in f1:
    b = re.split(';|\n',s)
    co_sql = 'UPDATE townfile_local SET countryId = "%s" WHERE localId = %s ;\n'% (b[2],b[0])
    f4.write(co_sql)
for s in f2:
    b = re.split('","|,"|"\n',s)
    if len(b)==4:
        a_sql = 'UPDATE townfile_local SET address = "%s" WHERE localId = %s ;\n'% (b[2].replace('"','\\"'),b[0])
        f4.write(a_sql)
    else:
        print(s)

for s in f3:
    b = re.split(',|\n',s)
    ca_sql = 'UPDATE townfile_local SET catId = %s, parentId = %s WHERE localId = %s ;\n'% (b[2],b[4],b[0])
    f4.write(ca_sql)


f1.close()
f2.close()
f3.close()
f4.close()
