import re
file1 = 'D:\\张玉龙\\Python\\提交\\20140401_countryId_raw.csv'
file2 = 'D:\\张玉龙\\Python\\提交\\20140401_UPDATE_countryIds.sql'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')
countryId = []
for s in f1:
    countryId.append(s.replace('\n',''))
countryId = list(set(countryId))

for s in countryId:
    if re.findall('[a-z]',s):
        sql = 'UPDATE townfile_local SET countryId = "%s" WHERE countryId = "%s" ;\n'% (s.upper(),s)
        print(sql)
        f2.write(sql)
f1.close()
f2.close()
