import re

##file1 = 'D:\\张玉龙\\Python\\资料保存\\全球大学Top100.txt'
##file2 = 'D:\\张玉龙\\Python\\提交\\20140408_INSERT_landmarkRank_shop_local.sql'
##
##f1    = open(file1,'r',encoding='utf-8')
##f2    = open(file2,'w',encoding='utf-8')

#----INSERT
##for s in f1:
##    b = re.split(',',s)
##    sql = "INSERT INTO landmark (localId,landmarkRank,tag,linkUrl,updateTime) VALUES (%s,%s,'','','2014-03-25 17:00:00') ;%s\n"% (b[0],b[1],b[3])
##    f2.write(sql)
##a=[]
##for s in f1:
##    b = re.split('\t|;|\n',s)
##    a.append(b[-2].replace('new',''))
##    if re.findall('new',b[-2]):
##        sql_s = 'INSERT INTO shop_local (localId,updateTime) VALUES (%s,"2014-04-16 18:00:00") ;\n'% b[-2].replace('new','')
##        f2.write(sql_s)
##    if int(b[0])<11:
##        sql_l = "INSERT INTO landmark (localId,landmarkRank,tag,linkUrl,updateTime) VALUES (%s,%s,'University','','2014-04-16 18:00:00') ;\n"% (b[-2].replace('new',''),9,)
##    elif int(b[0])<41:
##        sql_l = "INSERT INTO landmark (localId,landmarkRank,tag,linkUrl,updateTime) VALUES (%s,%s,'University','','2014-04-16 18:00:00') ;\n"% (b[-2].replace('new',''),8,)
##    else:
##        sql_l = "INSERT INTO landmark (localId,landmarkRank,tag,linkUrl,updateTime) VALUES (%s,%s,'University','','2014-04-16 18:00:00') ;\n"% (b[-2].replace('new',''),7,)
##    #sql = "INSERT INTO landmark (localId,landmarkRank,tag,linkUrl,updateTime) VALUES (%s,%s,'','','2014-03-25 17:00:00') ;%s\n"% (b[0],b[1],b[3])
##    f2.write(sql_l)
##print(a)

#----UPDATE star

##for s in f1:
##    if re.findall(',0$',s):
##        b = re.split(',',s)
##        sql = 'UPDATE townfile_local SET star = 0 WHERE localId = %s ;\n'% b[0]
##        f2.write(sql)

#----DELETE from landmark表，并star降为0
##f1 = open('D:\\张玉龙\\Python\\20140425_cn去重_update_1.csv','r',encoding='utf-8')
##f2 = open('D:\\张玉龙\\Python\\提交\\20140425_DELETE_landmark2.sql','w',encoding='utf-8')
##for s in f1:
##    if re.findall('^d',s):
##        b = re.split(',',s)
##        b[0] = b[0].replace('d','')
##        sql = 'UPDATE townfile_local SET star = 0, updateTime = "2014-04-25 15:00:00" WHERE localId = %s ;\nDELETE FROM landmark WHERE localId = %s;\n'% (b[0],b[0])
##        f2.write(sql)
##    elif re.findall('^t',s):
##        b = re.split(',',s)
##        b[0] = b[0].replace('t','')
##        sql = 'UPDATE landmark SET landmarkRank = 0, updateTime = "2014-04-25 18:00:00" WHERE localId = %s ;\n'% (b[0])
##        f2.write(sql)
##f1.close()
##f2.close()

#----UPDATE tag

##for s in f1:
##    b = re.split(',|"',s)
##    sql = 'UPDATE landmark SET tag = "%s" WHERE localId = %s ;\n'% (b[2],b[0])
##    f2.write(sql)
##    print(sql)

#----UPDATE landmarkRank
##for s in f1:
##    b = re.split(',|"',s)
##    if re.findall('\[',b[2]):
##        rank = float(re.findall('^([1-5]\.[05])\[',b[2])[0])
##        order= float(re.findall('第([\d]+) ',b[2])[0])
##        total= float(re.findall('共 ([\d]+) ',b[2])[0])
##        landmarkRank = (1-order/total)*rank*1.5
##        landmarkRank = int(landmarkRank)
##        if landmarkRank==0:
##            landmarkRank=1
##        sql = 'UPDATE landmark SET landmarkRank = %s, updateTime = "2014-04-08 14:00:00" WHERE localId = %s ;\n'% (landmarkRank,b[0])
##        #break
##        f2.write(sql)
##        print(sql)

#--localName
##f1 = open('D:\\张玉龙\\Python\\20140504_localName_update.csv','r',encoding='utf-8')
##f2 = open('D:\\张玉龙\\Python\\提交\\20140504_UPDATE_localName.sql','w',encoding='utf-8')
##for s in f1:
##    b = re.split(',|"',s)
##    sql = 'UPDATE townfile_local SET localName = "%s", updateTime = "2014-05-04 15:00:00" WHERE localId = %s ;\n'% (b[2],b[0])
##    f2.write(sql)
##f1.close()
##f2.close()

#----比较raw和update生成sql
##f1 = open('D:\\张玉龙\\源文件\\20140428_beijing_raw.txt','r',encoding='utf-8')
##f2 = open('D:\\张玉龙\\Python\\20140428_beijing_update.txt','r',encoding='utf-8')
####f3 = open('D:\\张玉龙\\源文件\\20140418_park_raw.csv','r',encoding='utf-8')
####f4 = open('D:\\张玉龙\\Python\\20140418_park_update_1.csv','r',encoding='utf-8')
##f5 = open('d:\\张玉龙\\Python\\提交\\20140428_UPDATE_landmark.sql','w',encoding='utf-8')
##dic = {}
##for s in f1:
##    b       = re.split('\t |\n',s)
##    localId = b[0]
##    rank    = b[1]
##    dic[localId] = rank
##for s in f2:
##    b       = re.split('\t |\n',s)
##    localId = b[0]
##    rank    = b[1]
##    if dic[localId] != rank:
##        sql = 'UPDATE landmark SET landmarkRank = %s, updateTime = "2014-04-28 11:00:00" WHERE localId = %s;\n'% (rank,localId)
##        f5.write(sql)
##dic = {}
##for s in f3:
##    b       = re.split(',|\n',s)
##    localId = b[0]
##    rank    = b[-2]
##    dic[localId] = rank
##for s in f4:
##    b       = re.split(',|\n',s)
##    localId = b[0]
##    rank    = b[-2]
##    if dic[localId] != rank:
##        sql = 'UPDATE landmark SET landmarkRank = %s, updateTime = "2014-04-20 10:00:00" WHERE localId = %s;\n'% (rank,localId)
##        f5.write(sql)
##f1.close()
##f2.close()
##f3.close()
##f4.close()
##f5.close()

#----标记重名点
##file1 = 'D:\\张玉龙\\源文件\\20140421_landmarkRank_shanghai.txt'
##file2 = 'D:\\张玉龙\\Python\\20140421_landmarkRank_shanghai_update.txt'
####f1 = open(file1,'r',encoding='utf-8')
####f2 = open(file2,'w',encoding='utf-8')
####content = f1.read()
####f1.seek(0)
####for s in f1:
####    b = re.split('\t |\n',s)
####    #print(b[2])
####    if len(re.findall(b[2],content))>1:
####        f2.write('d'+s)
####    else:
####        f2.write(s)
####f1.close()
####f2.close()
##    #--生成sql
##file3 = 'D:\\张玉龙\\Python\\提交\\20140421_UPDATE_landmark.sql'
##f1 = open(file1,'r',encoding='utf-8')
##f2 = open(file2,'r',encoding='utf-8')
##f3 = open(file3,'a',encoding='utf-8')
##dic = {}
##for s in f1:
##    b = re.split('\t |\n',s)
##    dic[b[0]]=[b[1],b[2]]
##for s in f2:
##    b = re.split('\t |\n',s)
##    if b[1]!=dic[b[0]][0]:
##        rank_sql = 'UPDATE landmark SET landmarkRank = %s, updateTime = "2014-04-22 11:30:00" WHERE localId = %s;\n'% (b[1],b[0])
##        f3.write(rank_sql)
##    if b[2]!=dic[b[0]][1]:
##        name_sql = 'UPDATE townfile_local SET localName = "%s", updateTime = "2014-04-22 11:30:00" WHERE localId = %s;\n'% (b[2],b[0])
##        f3.write(name_sql)
##f1.close()
##f2.close()
##f3.close()

