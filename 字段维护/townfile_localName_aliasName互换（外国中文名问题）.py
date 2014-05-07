import re

#----localName aliasName 互换
##file1 = 'D:\\张玉龙\\源文件\\20140407_aliasName_raw.txt'
##file2 = 'D:\\张玉龙\\Python\\提交\\20140407_UPDATE_localName-aliasName.sql'
##f1    = open(file1,'r',encoding='utf-8')
##f2    = open(file2,'w',encoding='utf-8')
##for s in f1:
##    b = re.split('\t|\n',s)
##    localId  = b[0]
##    localName= re.sub('^"|"$','',b[1])
##    aliasName= re.sub('^"|"$','',b[2])
##    sql      = 'UPDATE townfile_local SET localName = "%s", aliasName = "%s", updateTime = "2014-04-07 17:00:00" WHERE localId = %s ;\n'% (aliasName.replace('"','\\"'),localName.replace('"','\\"'),localId)
##    #print(sql)
##    f2.write(sql)
##    #break
##f1.close()
##f2.close()

#----localName翻译,并将原来的名称改为aliasName
file1 = 'D:\\张玉龙\\Python\\20140423_cnName_update.csv'
file2 = 'D:\\张玉龙\\Python\\提交\\20140424_UPDATE_localName2.sql'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')
for s in f1:
    b = re.split(',|\n',s)
    localId  = b[0]
    localName= b[2]
    aliasName= b[3]
    if localName == '""':
        pass
    else:
        sql = 'UPDATE townfile_local SET localName = %s, aliasName = %s, updateTime = "2014-04-25 10:00:00" WHERE localId = %s ;\n'% (localName,aliasName,localId)
        #print(sql)
        f2.write(sql)
    #break
f1.close()
f2.close()
