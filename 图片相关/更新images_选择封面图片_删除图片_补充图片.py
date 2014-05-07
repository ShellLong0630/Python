import os,re,mysql.connector

file = 'd:/张玉龙/Python/提交/20140504_UPDATE_images.sql'
#file2= 'd:/张玉龙/源文件/20140424_images.txt'
f1   = open(file,'w',encoding='utf-8')
#f2   = open(file2,'r',encoding='utf-8')
host = '192.168.1.15'
user = 'data'
db   = 'wwere_v3'
pwd  = 'skst'
ori  = 'D:/张玉龙/Python/600x600'
Paths     = []
cnx = mysql.connector.connect(host=host,user=user,database=db,password=pwd)
cursor = cnx.cursor()
dic_name = {}
sql = 'SELECT l.localId,t.images FROM landmark l left join townfile_local t on l.localId=t.localId WHERE l.landmarkRank>0 and t.images!="" and t.updateTime = "2014-05-04 18:00:00"order by l.localId'
cursor.execute(sql)
result = cursor.fetchall()
#----删除图片
total = os.walk(ori)
allfile = []
for rootDir,pathList,fileList in total:
    for file in fileList:
        if re.findall('jpg$',file):
            allfile.append(file[0]+file[1]+'/'+file)
allfile = set(allfile)
print(len(allfile))
for s in result:
    delete  = []
    localId = s[0]
    cover   = s[1].split(';')
    length  = len(cover)
    for pic in cover:
        if pic in allfile:
            pass
        else:
            delete.append(pic)
            print(pic)
    for d in delete:
            cover.remove(d)
    if len(cover) == length:
        pass
    else:
        allFile   = ';'.join(cover)
        sql = 'UPDATE townfile_local SET images = "%s", updateTime = "2014-05-04 18:00:00" WHERE localId = %s; \n'% (allFile,localId) 
        f1.write(sql)
#f2.close()

#----补充封面图片

##total = os.walk(ori)
##allfile = []
##for rootDir,pathList,fileList in total:
##    for file in fileList:
##        if re.findall('jpg$',file):
##            allfile.append(file[0]+file[1]+'/'+file)
##allfile = set(allfile)
##for s in f2:
##    localId = re.split('\t|\n',s)[0]
##    cover   = re.split('\t|\n',s)[1].split(';')
##    #print(cover)
##    for pic in cover:
##        if pic not in allfile:
##            cover.remove(pic)
##    sql = 'SELECT l.localId,t.images FROM landmark l left join townfile_local t on l.localId=t.localId WHERE l.localId = %s'% localId
##    cursor.execute(sql)
##    name = cursor.fetchall()
##    #print(cover,name)
##    for s in name:
##        allFile   = s[1]+';'+str(cover).replace(']','').replace('[','').replace(', ',';').replace("'",'')#str(s[1].split(';')).replace(']','').replace('[','').replace(', ',';').replace("'",'')
##        #print(allFile)
##        sql = 'UPDATE townfile_local SET images = "%s", updateTime = "2014-04-16 17:00:00" WHERE localId = %s; \n'% (allFile,s[0])
##        #print(sql)    
##        f1.write(sql)
##f2.close()
    ##    print(sql)
    ##    break

#----调整图片顺序，将选中图片放在首位做封面

##sql = 'SELECT l.localId,t.images,t.localName FROM landmark l left join townfile_local t on l.localId=t.localId WHERE l.landmarkRank>0 and t.images!="" order by l.localId'
##cursor.execute(sql)
##name = cursor.fetchall()
##for s in name:
##    dic_name[s[0]]=(s[2],s[1].split(';'))
##    select=[]
##    partfiles = [(ori+'/').replace('/','\\\\')+i for i in dic_name[s[0]][1]]
####    print(partfiles)
##    for t in partfiles:
####        if os.path.exists(s.split('/')[0].replace("600x600","Photos_Select")):
####            pass
####        else:
####            os.makedirs(s.split('/')[0].replace("600x600","Photos_Select"))
##        if os.path.isfile(t.replace('/','\\\\')):
##            pass
##        else:
##            partfiles.remove(t)
##            select.append(t.split('\\')[-1])
##    partfiles = [i.split('\\')[-1] for i in partfiles]
####    print(partfiles)
####    print(select)
##    allFile   = select + partfiles
##    allFile   = str(allFile).replace(']','').replace('[','').replace(', ',';').replace("'",'')
####    print(allFile)
##    sql = 'UPDATE townfile_local SET images = "%s", updateTime = "2014-04-04 16:30:00" WHERE localId = %s; \n'% (allFile,s[0])
##    f1.write(sql)
####    print(sql)
####    break

cnx.commit()
cursor.close()
cnx.close()
f1.close()

    
