import re

#标记后对比原文本，生成sql

orifile = 'D:\\张玉龙\\源文件\\20140329_landmark_name.txt'
tarfile = 'D:\\张玉龙\\Python\\20140329_landmark_name_update2.txt'
sql_file = 'D:\\张玉龙\\Python\\提交\\20140329_UPDATE_landmarks.sql'
#name_file = 'D:\\张玉龙\\Python\\提交\\20140313_UPDATE_name2.sql'
#tape_file = 'D:\\张玉龙\\Python\\提交\\20140313_UPDATE_tapename.sql'

f1 = open(orifile,'r',encoding='utf-8')
f2 = open(tarfile,'r',encoding='utf-8')
f3 = open(sql_file,'w',encoding='utf-8')
#f4 = open(name_file,'w',encoding='utf-8')
#f5 = open(tape_file,'w',encoding='utf-8')
ori_dic = {}
for s in f1:
    if re.findall('\t ',s):
        b = re.split('\t |\n',s)
        #c = re.split('",',s)
        localId = b[0]
        star    = b[1]
        name    = b[2]
        ori_dic[localId] = (name,star)
for s in f2:
    if re.findall(',',s):
        b = re.split(',|\n',s)
        if len(b)==4:
            localId = b[0]
            star    = b[1]
            name    = b[2]
            if name==ori_dic[localId][0]:
                pass
            else:
                name_town = 'UPDATE townfile_local SET localName = "%s" WHERE localId = %s ;\n'% (name.replace('"','\\"'),localId)
                #name_tape = 'UPDATE tape_local SET name = %s" WHERE id = %s ;\n'% (name,localId)
                f3.write(name_town)
                #f4.write(name_tape)
            if star==ori_dic[localId][1]:
                pass
            else:
                star_sql = 'UPDATE landmark SET landmarkRank = %s WHERE localId = %s ;\n'% (star,localId)
                f3.write(star_sql)
        elif len(b)==5:
            localId = b[0]
            star    = b[1]
            name    = b[2]
            alias   = b[3]
            alias_sql = 'UPDATE townfile_local SET aliasName = "%s" WHERE localId = %s ;\n'% (alias.replace('"','\\"'),localId)
            f3.write(alias_sql)
            if name==ori_dic[localId][0]:
                pass
            else:
                name_town = 'UPDATE townfile_local SET localName = "%s" WHERE localId = %s ;\n'% (name.replace('"','\\"'),localId)
                #name_tape = 'UPDATE tape_local SET name = %s" WHERE id = %s ;\n'% (name,localId)
                f3.write(name_town)
                #f4.write(name_tape)
            if star==ori_dic[localId][1]:
                pass
            else:
                star_sql = 'UPDATE landmark SET landmarkRank = %s WHERE localId = %s ;\n'% (star,localId)
                f3.write(star_sql)

f1.close()
f2.close()
f3.close()
#f4.close()
#f5.close()

#landmark调整
'''
orifile = 'D:\\张玉龙\\源文件\\20140325_landmark_dedup.txt'
tarfile = 'D:\\张玉龙\\Python\\20140325_landmark_dedup_update_4.txt'
star_file = 'D:\\张玉龙\\Python\\提交\\20140326_UPDATE_landmarkRank.sql'
f1 = open(orifile,'r',encoding='utf-8')
f2 = open(tarfile,'r',encoding='utf-8')
f3 = open(star_file,'w',encoding='utf-8')

ori_dic = {}
by      = ',|\n'
for s in f1:    
    b = re.split(by,s)
    localId = b[0]
    star    = b[-2]
    ori_dic[localId] = star
for s in f2:
    b = re.split(by,s)
    localId = b[0]
    star    = b[-2]
    if int(star)==0:
        star_sql = 'UPDATE landmark SET landmarkRank = %s WHERE localId = %s ;\n'% (star,localId)
        f3.write(star_sql)
    elif star==ori_dic[localId]:
        pass
    else:
        print(ori_dic[localId]+'  '+s)
        star_sql = 'UPDATE landmark SET landmarkRank = %s WHERE localId = %s ;\n'% (star,localId)
        f3.write(star_sql)
f1.close()
f2.close()
f3.close()
'''






