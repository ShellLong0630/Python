import re
import mysql.connector
import sys,os,json

file1 = 'D:/张玉龙/Python/20140428_remark.txt'
file2 = 'D:\\张玉龙\Python\\提交\\20140429_DELETE_townfile_shop.sql'
f1=open(file1,'r',encoding='utf-8')
f2=open(file2,'w',encoding='utf-8')

user   = 'data'
pwd    = 'skst'
host   = '192.168.1.15'
db     = 'wwere_v3'
cnx    = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
cursor = cnx.cursor()
Time   = "2014-04-30 19:00:00"
a          = []
b          = []
d_Id       = []
d_sourceId = []
nd_Id      = []
def field(i):
    u_field = ''
    dic = {0:'sourceId',1:'suit',2:'feature',3:'businessArea',4:'avgCost',5:'recommend',6:'aliasName',7:'shopHours',8:'traffic',9:'parking',
           10:'shopUrl',11:'shopRank',12:'cityId',13:'phoneNumber',14:'priceSymbol',15:'24h',16:'catId',17:'parentId',18:'images',19:'star'}
    table = 'shop_local'
    if i in [0,6,12,16,17,18,19]:
        table = 'townfile_local'
    if bool(result_d[i]):
        pass#u_field = result_d[i]
    elif bool(result_n[i]):
        u_field = result_n[i]
        u_field_sql ='UPDATE %s SET %s = "%s", updateTime = "%s" WHERE localId = %s ;\n'% (table,dic.get(i),str(u_field).replace('"','\\"'),Time,str(min(nd_Id)))
        f2.write(u_field_sql)
    else:
        pass

def combine(j):
    dic = {0:'sourceId',1:'suit',2:'feature',3:'businessArea',4:'avgCost',5:'recommend',6:'aliasName',7:'shopHours',8:'traffic',9:'parking',
           10:'shopUrl',11:'shopRank',12:'cityId',13:'phoneNumber',14:'priceSymbol',15:'24h',16:'catId',17:'parentId',18:'images',19:'star'}
    u_com = ''
    a = []
    b = []
    table = 'shop_local'
    if j in [0,6,12,16,17,18,19]:
        table = 'townfile_local'
    if result_n[j]==result_d[j]:
        pass
    else:
        if bool(result_n[j]):
            if re.findall(',',result_n[j]):
                a = re.split(',',result_n[j])            
                for s in a :
                    b.append(s)
            else:
                b.append(result_n[j])
        else:
            pass    
        if bool(result_d[j]):
            if re.findall(',',result_d[j]):
                a = re.split(',',result_d[j])            
                for s in a :
                    b.append(s)
            else:
                b.append(result_d[j])
        else:
            pass    
    if b:
        b = list(set(b))
        u_com+=','.join(b)
        u_com_sql = 'UPDATE %s SET %s = "%s", updateTime = "%s" WHERE localId = %s ;\n'% (table,dic.get(j),u_com.replace('"','\\"'),Time,str(min(nd_Id)))
        u_com_sql = u_com_sql.replace('," WHERE','" WHERE')
        f2.write(u_com_sql)
    else:
        pass
def recommend(k):
    try:
        if bool(result_n[k]):
            recom_n = json.loads(result_n[k].replace('{','{"').replace('{""','{"'))
            recom_u = {}
            for h in recom_n.keys():
                recom_u[h] = recom_n[h]
            if bool(result_d[k]):
                recom_d = json.loads(result_d[k])
                for h in recom_d.keys():
                    recom_u[h] = recom_d[h]
            else:
                pass
            recom = json.dumps(recom_u,ensure_ascii=False)
            recom_sql = 'UPDATE shop_local SET recommend = "%s", updateTime = "%s" WHERE localId = %s ;\n'% (recom.replace('"','\\"'),Time,str(min(nd_Id)))
            f2.write(recom_sql)
        else:
            pass
    except:
        print(nd_Id)
dic = {}
content = {}
for s in f1:
    
    if len(s)<5 and len(d_Id)==0:
        Name=''
        d_Id=[]
        nd_Id=[]
        d_sourceId=[]  
    elif len(s)<5 and len(d_Id):       
        #查询nd_Id中min的sourceId并追加给它d_sourceId
        sql='SELECT sourceId,length(sourceId) from townfile_local where localId = '+str(min(nd_Id))
        #print('b',sql)
        cursor.execute(sql)
        sourceId1=cursor.fetchall()
        d_sourceId = list(set(d_sourceId))        
        select_n = 'SELECT t.sourceId,s.suit,s.feature,s.businessArea,s.avgCost,s.recommend,t.aliasName,s.shopHours,s.traffic,s.parking,s.shopUrl,s.shopRank,t.cityId,s.phoneNumber,s.priceSymbol,s.24h,t.catId,t.parentId,t.images,t.star,t.address FROM shop_local s left join townfile_local t on s.localId=t.localId WHERE s.localId = %s'% str(min(nd_Id))
        select_d = 'SELECT t.sourceId,s.suit,s.feature,s.businessArea,s.avgCost,s.recommend,t.aliasName,s.shopHours,s.traffic,s.parking,s.shopUrl,s.shopRank,t.cityId,s.phoneNumber,s.priceSymbol,s.24h,t.catId,t.parentId,t.images,t.star,t.address FROM shop_local s left join townfile_local t on s.localId=t.localId WHERE s.localId = %s'% str(max(d_Id))        
        cursor.execute(select_n)
        result_n = cursor.fetchall()[0]
        cursor.execute(select_d)
        result_d = cursor.fetchall()[0]
        
        #判断min(nd_Id)如果没有sourceId
            #1、sourceId：在shop_local中将max（新id）的localId更新为min(老id)，并将被delete的数据的sourceId追加给保留的数据
            #2、name和address：将min(老id)的name和address更新为max（新id）的name和address
        if sourceId1[0][1]==0:#sourceId为空
            pass
                            #UPDATE 如果没有sourceId，townfile_local中将老Id删除，将新id更新为老Id
                ##            d_min_t = 'DELETE FROM townfile_local WHERE localId = %s ;\n'% str(min(nd_Id))
                ##            u_max_t = 'UPDATE townfile_local SET localId = %s WHERE localId = %s ;\n'% (str(min(nd_Id)),str(max(d_Id))) 
                ##            f2.write(d_min_t)
                ##            f2.write(u_max_t)
                ##            ##DELETE语句
                ##            for m in d_Id:                        
                ##                d_townfile='DELETE FROM townfile_local WHERE localId = '+str(m)+' ;\n'
                ##                d_shop='DELETE FROM shop_local WHERE localId = '+str(m)+' ;\n'
                ##                if m == max(d_Id):
                ##                    pass
                ##                else:
                ##                    f2.write(d_townfile)
                ##                    f2.write(d_shop)
        #有sourceId的将更新为最新数据，需要逐字段判断，新数据为空则不更新
        else:
            d_sourceId.append(sourceId1[0][0])
            ##DELETE语句
        for m in d_Id:                        
            d_townfile='DELETE FROM townfile_local WHERE localId = '+str(m)+' ;\n'
            d_shop='DELETE FROM shop_local WHERE localId = '+str(m)+' ;\n'
            if m == max(d_Id):
                f2.write(d_townfile)
            else:
                f2.write(d_townfile)
                f2.write(d_shop)
            
        d_min = 'DELETE FROM shop_local WHERE localId = %s ;\n'% str(min(nd_Id))
        u_max = 'UPDATE shop_local SET localId = %s WHERE localId = %s ;\n'% (str(min(nd_Id)),str(max(d_Id))) 
        f2.write(d_min)
        f2.write(u_max)
        u_source = 'UPDATE townfile_local SET sourceId = "%s", updateTime = "%s" WHERE localId = %s ;\n'% (','.join(d_sourceId),Time,str(min(nd_Id)))
        f2.write(u_source)        
        #UPDATE      
        combine(1)
        combine(2)
        field(3)
        field(4)
        recommend(5)
        field(6)
        field(7)
        field(8)
        field(9)
        field(10)
        field(11)
        field(12)
        field(13)
        field(14)
        field(15)
        field(16)
        field(17)
        field(18)
        field(19)
        #address 取长的
        if len(result_d[20])>len(result_n[20]):
            u_field = result_d[20]
            u_field_sql ='UPDATE townfile_local SET address = "%s", updateTime = "2014-04-29 17:00:00" WHERE localId = %s ;\n'% (str(u_field).replace('"','\\"'),str(min(nd_Id)))
            f2.write(u_field_sql)                              
        d_Id=[]
        nd_Id=[]
        d_sourceId=[]   
    elif re.findall('d',str(re.split(';',s)[0])) and int(str(re.split(';',s)[0]).replace('d',''))>17720000:
        #print('a',str(re.split(';',s)[0]))
        d_Id.append(int(str(re.split(';',s)[0]).replace('d','')))
        sql='SELECT sourceId from townfile_local where localId='+str(re.split(';',s)[0]).replace('d','')
        cursor.execute(sql)
        sourceId=cursor.fetchall()
        d_sourceId.append(sourceId[0][0])
        if int(str(re.split(';',s)[0]).replace('d',''))==int(max(d_Id)):
            Name=re.split(';',s)[1]
        else:
            pass
    else:
        nd_Id.append(int(str(re.split(';',s)[0])))

cnx.commit()
cursor.close()
cnx.close()
f1.close()
f2.close()

##import re
##import mysql.connector
##import sys,os,json
##
##file1 = 'D:/张玉龙/Python/20140428_remark.txt'
##file3 = 'D:\\张玉龙\Python\\提交\\20140429_UPDATE_shop_townfile.sql'
##f1=open(file1,'r',encoding='utf-8')
###f2=open(file2,'w',encoding='utf-8')
##f3=open(file3,'w',encoding='utf-8')
##user   = 'data'
##pwd    = 'skst'
##host   = '192.168.1.15'
##db     = 'wwere_v3'
##cnx    = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
##cursor = cnx.cursor()
##a          = []
##b          = []
##d_Id       = []
##d_sourceId = []
##nd_Id      = []
##
##def field(i):
##    u_field = ''
##    dic = {0:'sourceId',1:'suit',2:'feature',3:'businessArea',4:'avgCost',5:'recommend',6:'aliasName',
##           7:'shopHours',8:'traffic',9:'parking',10:'shopUrl',11:'shopRank',12:'cityId',13:'phoneNumber',14:'priceSymbol',15:'24h'}
##    table = 'shop_local'
##    if i in [0,6,12]:
##        table = 'townfile_local'
##    if bool(result_d[i]):
##        u_field = result_d[i]
##    elif bool(result_n[i]):
##        u_field = result_n[i]
##        u_field_sql ='UPDATE %s SET %s = "%s" WHERE localId = %s ;\n'% (table,dic.get(i),str(u_field).replace('"','\\"'),str(min(nd_Id)))
##        f3.write(u_field_sql)
##    else:
##        pass
##
##def combine(j):
##    dic = {0:'sourceId',1:'suit',2:'feature',3:'businessArea',4:'avgCost',5:'recommend',6:'aliasName',7:'shopHours',
##           8:'traffic',9:'parking',10:'shopUrl',11:'shopRank',12:'cityId',13:'phoneNumber',14:'priceSymbol',15:'24h'}
##    u_com = ''
##    a = []
##    b = []
##    if bool(result_n[j]):
##        if re.findall(',',result_n[j]):
##            a = re.split(',',result_n[j])            
##            for s in a :
##                b.append(s)
##        else:
##            b.append(result_n[j])
##    else:
##        pass    
##    if bool(result_d[j]):
##        if re.findall(',',result_d[j]):
##            a = re.split(',',result_d[j])            
##            for s in a :
##                b.append(s)
##        else:
##            b.append(result_d[j])
##    else:
##        pass    
##    if b:
##        b = set(b)
##        for s in b:
##            u_com+=s+','
##        u_com_sql = 'UPDATE shop_local SET %s = "%s" WHERE localId = %s ;\n'% (dic.get(j),u_com.replace('"','\\"'),str(min(nd_Id)))
##        u_com_sql = u_com_sql.replace('," WHERE','" WHERE')
##        f3.write(u_com_sql)
##    else:
##        pass
##def recommend(k):
##    try:
##        if bool(result_n[k]):
##            recom_n = json.loads(result_n[k].replace('{','{"').replace('{""','{"'))
##            recom_u = {}
##            for h in recom_n.keys():
##                recom_u[h] = recom_n[h]
##            if bool(result_d[k]):
##                recom_d = json.loads(result_d[k])
##                for h in recom_d.keys():
##                    recom_u[h] = recom_d[h]
##            else:
##                pass
##            recom = json.dumps(recom_u,ensure_ascii=False)
##            recom_sql = 'UPDATE shop_local SET recommend = "%s" WHERE localId = %s ;\n'% (recom.replace('"','\\"'),str(min(nd_Id)))
##            f3.write(recom_sql)
##        else:
##            pass
##    except:
##        print(str(min(nd_Id)))
##for s in f1:
##
##    ##初始化
##    try:
##        if len(s)<5 and len(d_Id)==0:
##            Name=''
##            Address=''
##            d_Id=[]
##            nd_Id=[]
##            d_sourceId=[]        
##        #处理数组
##        elif len(s)<5 and len(d_Id):
##            dsource=''        
##            #查询nd_Id中min的sourceId并追加给它d_sourceId
##            sql='SELECT sourceId,length(sourceId) from townfile_local where localId='+str(min(nd_Id))
##            cursor.execute(sql)
##            sourceId1=cursor.fetchall()
##            #拼接sourceId
##            d_sourceId = list(set(d_sourceId))
##            if len(d_sourceId)>1:
##                for t in d_sourceId:
##                    dsource+=t+','
##            else:
##                dsource=d_sourceId[0]
##            
####            #判断min(nd_Id)是否在shop_local
####                #1、sourceId：在shop_local中将max（新id）的localId更新为min(老id)，并将被delete的数据的sourceId追加给保留的数据
####                #2、name和address：将min(老id)的name和address更新为max（新id）的name和address
####
####            if sourceId1[0][1]==0:#bool(sourceId1)==False:
####                #UPDATE
####                u_address='UPDATE townfile_local SET address = "%s",localName = "%s" WHERE localId = %s ;\n'% (Address.replace('"','\\"'),Name.replace('"','\"'),str(min(nd_Id))) 
####                if re.findall(',',dsource):#len(dsource)>1:
####                    u_source = 'UPDATE townfile_local SET localId = %s,sourceId = "%s" WHERE localId = %s ;\n'% (str(min(nd_Id)),dsource,str(max(d_Id)))
####                    u_source = u_source.replace('," WHERE','" WHERE')
####                else:
####                    u_source='UPDATE townfile_local SET localId = %s WHERE localId = %s ;\n'% (str(min(nd_Id)),str(max(d_Id)))
####                f3.write(u_source)
####                f3.write(u_address)          
####                #DELETE
####                for m in d_Id:
####                    d_townfile='DELETE FROM townfile_local WHERE localId = '+str(m)+' ;\n'
####                    d_shop='DELETE FROM shop_local WHERE localId = '+str(m)+' ;\n'
####                    if m == max(d_Id):
####                        f3.write(d_townfile)
####                    else:
####                        f3.write(d_townfile)
####                        f3.write(d_shop)
####            #有sourceId的将更新为最新数据，需要逐字段判断，新数据为空则不更新
####            else:
##            select_n = 'SELECT t.sourceId,s.suit,s.feature,s.businessArea,s.avgCost,s.recommend,t.aliasName,s.shopHours,s.traffic,s.parking,s.shopUrl,s.shopRank,t.cityId,s.phoneNumber,s.priceSymbol,s.24h FROM shop_local s left join townfile_local t on s.localId=t.localId WHERE s.localId = %s'% str(min(nd_Id))
##            select_d = 'SELECT t.sourceId,s.suit,s.feature,s.businessArea,s.avgCost,s.recommend,t.aliasName,s.shopHours,s.traffic,s.parking,s.shopUrl,s.shopRank,t.cityId,s.phoneNumber,s.priceSymbol,s.24h FROM shop_local s left join townfile_local t on s.localId=t.localId WHERE s.localId = %s'% str(max(d_Id))
##            
##            cursor.execute(select_n)
##            result_n = cursor.fetchall()[0]
##            cursor.execute(select_d)
##            result_d = cursor.fetchall()[0]
##            d_min = 'DELETE FROM shop_local WHERE localId = %s ;\n'% str(min(nd_Id))
##            u_max = 'UPDATE shop_local SET localId = %s WHERE localId = %s ;\n'% (str(min(nd_Id)),str(max(d_Id))) 
##
##            f3.write(d_min)
##            f3.write(u_max)
##            u_sourceId_sql='UPDATE townfile_local SET sourceId = "'+dsource+','+sourceId1[0][0]+'" WHERE localId = '+str(min(nd_Id))+' ;\n'
##            f3.write(u_sourceId_sql.replace(',,',','))
##            ##DELETE语句
##            for m in d_Id:
##                
##                d_townfile='DELETE FROM townfile_local WHERE localId = '+str(m)+' ;\n'
##                d_shop='DELETE FROM shop_local WHERE localId = '+str(m)+' ;\n'
##                if m == max(d_Id):
##                    f3.write(d_townfile)
##                else:
##                    f3.write(d_townfile)
##                    f3.write(d_shop)
##            #UPDATE      
##            combine(1)
##            combine(2)
##            field(3)
##            field(4)
##            recommend(5)
##            field(6)
##            field(7)
##            field(8)
##            field(9)
##            field(10)
##            field(11)
##            field(12)
##            field(13)
##            field(14)
##            field(15)
##                              
##            d_Id=[]
##            nd_Id=[]
##            d_sourceId=[]    
##        elif re.findall('d',str(re.split(';',s)[0])) and int(str(re.split(';',s)[0]).replace('d',''))>17720000:
##            d_Id.append(int(str(re.split(';',s)[0]).replace('d','')))
##            sql='SELECT sourceId from townfile_local where localId='+str(re.split(';',s)[0]).replace('d','')
##            cursor.execute(sql)
##            sourceId=cursor.fetchall()
##            d_sourceId.append(sourceId[0][0])
##            if int(str(re.split(';',s)[0]).replace('d',''))==int(max(d_Id)):
##                sql='SELECT address from townfile_local where localId='+str(re.split(';',s)[0]).replace('d','')
##                cursor.execute(sql)
##                addr=cursor.fetchall()
##                Address=addr[0][0]
##                Name=re.split(';',s)[1]
##            else:
##                pass
##        else:
##            nd_Id.append(int(str(re.split(';',s)[0])))
##    except:
##        print('error!  '+s)
##cnx.commit()
##cursor.close()
##cnx.close()
##f1.close()
###f2.close()
##f3.close()

#----判断相同的sourceId走合并流程

##import re
##import mysql.connector
##import sys,os,json
##
##file1 = 'D:/张玉龙/源文件/20140428_createTime=2014-04-28_0.88_0.0025.log'
##file2 = 'D:/张玉龙/Python/20140428_createTime=2014-04-28_0.88_0.0025_update.log'
##file3 = 'D:\\张玉龙\Python\\提交\\20140429_DELETE_townfile_shop.sql'
##f1=open(file1,'r',encoding='utf-8')
##f2=open(file2,'w',encoding='utf-8')
##f3=open(file3,'w',encoding='utf-8')
##
##user   = 'data'
##pwd    = 'skst'
##host   = '192.168.1.15'
##db     = 'wwere_v3'
##cnx    = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
##cursor = cnx.cursor()
###找出checkNum>0的点
##checkNum = []
##sql    = 'select localId from d01.townfile_local where checkNum >0 and localId>17757772'
##cursor.execute(sql)
##check = cursor.fetchall()
##for s in check:
##    checkNum.append(s[0])
##checkNum = set(checkNum)
##print(len(checkNum))
##d_Id       = []
##nd_Id      = []
##
##def field(i):
##    u_field = ''
##    dic = {0:'sourceId',1:'suit',2:'feature',3:'businessArea',4:'avgCost',5:'recommend',6:'aliasName',7:'shopHours',8:'traffic',9:'parking',
##           10:'shopUrl',11:'shopRank',12:'cityId',13:'phoneNumber',14:'priceSymbol',15:'24h',16:'catId',17:'parentId',18:'images',19:'address'}
##    table = 'shop_local'
##    if i in [0,6,12,16,17,18,19]:
##        table = 'townfile_local'
##    if bool(result_d[i]):
##        u_field = result_d[i]
##    elif bool(result_n[i]):
##        u_field = result_n[i]
##        u_field_sql ='UPDATE %s SET %s = "%s", updateTime = "2014-04-29 17:00:00" WHERE localId = %s ;\n'% (table,dic.get(i),str(u_field).replace('"','\\"'),str(nd_Id))
##        f3.write(u_field_sql)
##    else:
##        pass
##
##def combine(j):
##    dic = {0:'sourceId',1:'suit',2:'feature',3:'businessArea',4:'avgCost',5:'recommend',6:'aliasName',7:'shopHours',8:'traffic',9:'parking',
##           10:'shopUrl',11:'shopRank',12:'cityId',13:'phoneNumber',14:'priceSymbol',15:'24h',16:'catId',17:'parentId',18:'images',19:'address'}
##    u_com = ''
##    a = []
##    b = []
##    table = 'shop_local'
##    if i in [0,6,12,16,17,18,19]:
##        table = 'townfile_local'
##    if result_n[j]==result_d[j]:
##        pass
##    else:
##        if bool(result_n[j]):
##            if re.findall(',',result_n[j]):
##                a = re.split(',',result_n[j])            
##                for s in a :
##                    b.append(s)
##            else:
##                b.append(result_n[j])
##        else:
##            pass    
##        if bool(result_d[j]):
##            if re.findall(',',result_d[j]):
##                a = re.split(',',result_d[j])            
##                for s in a :
##                    b.append(s)
##            else:
##                b.append(result_d[j])
##        else:
##            pass    
##    if b:
##        b = list(set(b))
##        u_com+=','.join(b)
##        u_com_sql = 'UPDATE %s SET %s = "%s", updateTime = "2014-04-29 17:00:00" WHERE localId = %s ;\n'% (table,dic.get(j),u_com.replace('"','\\"'),str(nd_Id))
##        u_com_sql = u_com_sql.replace('," WHERE','" WHERE')
##        f3.write(u_com_sql)
##    else:
##        pass
##def recommend(k):
##    try:
##        if bool(result_n[k]):
##            recom_n = json.loads(result_n[k].replace('{','{"').replace('{""','{"'))
##            recom_u = {}
##            for h in recom_n.keys():
##                recom_u[h] = recom_n[h]
##            if bool(result_d[k]):
##                recom_d = json.loads(result_d[k])
##                for h in recom_d.keys():
##                    recom_u[h] = recom_d[h]
##            else:
##                pass
##            recom = json.dumps(recom_u,ensure_ascii=False)
##            recom_sql = 'UPDATE shop_local SET recommend = "%s", updateTime = "2014-04-29 17:00:00" WHERE localId = %s ;\n'% (recom.replace('"','\\"'),str(nd_Id))
##            f3.write(recom_sql)
##        else:
##            pass
##    except:
##        print(nd_Id)
##dic = {}
##content = {}
##for s in f1:
##
##    if len(s)<5 and len(dic.keys())==0:
##        dic = {}
##        content = {}
##        f2.write('\n')
##    elif len(s)<5 and len(dic.keys()):
##        for k in dic:
##            #判断一个sourceId是否有多个localId
##            if k =='no':
##                for x in dic['no']:
##                    f2.write(content[x])
##            elif len(dic[k])==1:
##                if dic[k][0] in content.keys():
##                    f2.write(content[dic[k][0]])
##                    del content[dic[k][0]]
##            else:
##                if min(dic[k]) in content.keys():
##                    f2.write(content[min(dic[k])])
##                    del content[min(dic[k])]
##                sql1 = 'SELECT sourceId FROM townfile_local WHERE localId in %s'% '('+','.join(dic[k])+')'
##                cursor.execute(sql1)
##                result = cursor.fetchall()
##                allsource = []
##                for source in result:
##                    for i in source[0].split(','):
##                        allsource.append(i)
##                if len(list(set(allsource)))==1:
##                    pass
##                else:
##                    allsource = ','.join(list(set(allsource)))
##                    sql2 = 'UPDATE townfile_local SET sourceId = "%s" WHERE localId = %s;\n'% (allsource,min(dic[k]))
##                    f3.write(sql2)
##                nd_Id = min(dic[k])
##                dic[k].remove(min(dic[k]))
##                for d in dic[k]:
##                    if int(d) in checkNum:
##                        #print('checkNum>0',d)
##                        dic[k].remove(d)
##                        f2.write(content[d])
##                d_Id = dic[k]
##                if d_Id:
##                    select_n = 'SELECT t.sourceId,s.suit,s.feature,s.businessArea,s.avgCost,s.recommend,t.aliasName,s.shopHours,s.traffic,s.parking,s.shopUrl,s.shopRank,t.cityId,s.phoneNumber,s.priceSymbol,s.24h,t.catId,t.parentId,t.images,t.address FROM shop_local s left join townfile_local t on s.localId=t.localId WHERE s.localId = %s'% str(nd_Id)
##                    select_d = 'SELECT t.sourceId,s.suit,s.feature,s.businessArea,s.avgCost,s.recommend,t.aliasName,s.shopHours,s.traffic,s.parking,s.shopUrl,s.shopRank,t.cityId,s.phoneNumber,s.priceSymbol,s.24h,t.catId,t.parentId,t.images,t.address FROM shop_local s left join townfile_local t on s.localId=t.localId WHERE s.localId = %s'% str(max(d_Id))
##                    
##                    cursor.execute(select_n)
##                    result_n = cursor.fetchall()[0]
##                    cursor.execute(select_d)
##                    result_d = cursor.fetchall()[0]
##                    d_min = 'DELETE FROM shop_local WHERE localId = %s ;\n'% str(nd_Id)
##                    u_max = 'UPDATE shop_local SET localId = %s WHERE localId = %s ;\n'% (str(nd_Id),str(max(d_Id))) 
##
##                    f3.write(d_min)
##                    f3.write(u_max)            
##                    ##DELETE语句
##                    for m in d_Id:                        
##                        d_townfile='DELETE FROM townfile_local WHERE localId = '+str(m)+' ;\n'
##                        d_shop='DELETE FROM shop_local WHERE localId = '+str(m)+' ;\n'
##                        if m == max(d_Id):
##                            f3.write(d_townfile)
##                        else:
##                            f3.write(d_townfile)
##                            f3.write(d_shop)
##                    #UPDATE      
##                    combine(1)
##                    combine(2)
##                    field(3)
##                    field(4)
##                    recommend(5)
##                    field(6)
##                    field(7)
##                    field(8)
##                    field(9)
##                    field(10)
##                    field(11)
##                    field(12)
##                    field(13)
##                    field(14)
##                    field(15)
##                    field(16)
##                    field(17)
##                    field(18)
##                    #field(19)
##                    #address 取长的
##                    if len(result_d[19])>len(result_n[19]):
##                        u_field = result_d[19]
##                        u_field_sql ='UPDATE townfile_local SET address = "%s", updateTime = "2014-04-29 17:00:00" WHERE localId = %s ;\n'% (str(u_field).replace('"','\\"'),str(nd_Id))
##                        f3.write(u_field_sql)                              
##                    d_Id=[]
##                    nd_Id=[]
##        dic = {}  
##        content = {}
##        f2.write('\n')
##            
##    else:
##        b = re.split(';|\n',s)
####        if int(b[0]) in checkNum:
####            print(b[0])
##        sourceId = list(set(b[-2].split(',')))
##        content[b[0]] = s
##        if sourceId[0]:
##            for t in sourceId:
##                if t in dic.keys():
##                    dic[t].append(b[0])
##                elif t=='':
##                    pass
##                else:
##                    dic[t] = [b[0]]
##        else:
##            if 'no' not in dic.keys():
##                dic['no'] = [b[0]]
##            else:
##                dic['no'].append(b[0])
##
##cnx.commit()
##cursor.close()
##cnx.close()
##f1.close()
##f2.close()
##f3.close()

###----
#判断相同的sourceId走合并流程（part）
##import re
##import mysql.connector
##import sys,os,json
##
##file1 = 'D:/张玉龙/源文件/20140423_country=US_0.88_0.0025.log'
###file2 = 'D:/张玉龙/Python/20140423_country=US_0.88_0.0025_update.log'
##file3 = 'D:\\张玉龙\Python\\提交\\20140426_DELETE_townfile_shop.sql'
##f1=open(file1,'r',encoding='utf-8')
###f2=open(file2,'w',encoding='utf-8')
##f3=open(file3,'w',encoding='utf-8')
##
##user   = 'data'
##pwd    = 'skst'
##host   = '192.168.1.15'
##db     = 'wwere_v3'
##cnx    = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
##cursor = cnx.cursor()
##dic = {}
##for s in f1:
##    try:
##        if len(s)<5 and len(dic.keys())==0:
##            dic = {}
##            content = {}
##        elif len(s)<5 and len(dic.keys()):
##            for k in dic:
##                if len(dic[k])==1:
##                    pass
##                else:
##                    sql1 = 'SELECT sourceId FROM townfile_local WHERE localId in %s'% '('+','.join(dic[k])+')'
##                    cursor.execute(sql1)
##                    result = cursor.fetchall()
##                    allsource = []
##                    #print(result)
##                    for source in result:
##                        for i in source[0].split(','):
##                            allsource.append(i)
##                    if len(list(set(allsource)))==1:
##                        pass
##                    else:
##                        allsource = ','.join(list(set(allsource)))
##                        sql2 = 'UPDATE townfile_local SET sourceId = "%s" WHERE localId = %s;\n'% (allsource,min(dic[k]))
##                        f3.write(sql2)
##                    nd_Id = min(dic[k])
##                    d_Id = dic[k].remove(min(dic[k]))                    
##                    for m in dic[k]:
##                        sql = 'DELETE FROM townfile_local WHERE localId = %s;\nDELETE FROM shop_local WHERE localId = %s;\n'% (m,m)
##                        f3.write(sql)
##            dic = {}  
##            content = {}         
##        else:
##            b = re.split(';|\n',s)
##            sourceId = b[-2].split(',')
##            content[b[0]] = s
##            for t in sourceId:
##                if t in dic.keys():
##                    dic[t].append(b[0])
##                elif t=='':
##                    pass
##                else:
##                    dic[t] = [b[0]]
##    except:
##        print('error!  '+s)
##
##f1.close()
##f3.close()
##cnx.commit()
##cursor.close()
##cnx.close()

#----判断相同sourceId的点

##import re
##import mysql.connector
##import sys,os,json
##
##file1 = 'D:/张玉龙/源文件/20140423_country=US_0.88_0.0025.log'
###file2 = 'D:/张玉龙/Python/20140423_country=US_0.88_0.0025_update.log'
##file3 = 'D:\\张玉龙\Python\\提交\\20140426_DELETE_townfile_shop.sql'
##f1=open(file1,'r',encoding='utf-8')
###f2=open(file2,'w',encoding='utf-8')
##f3=open(file3,'w',encoding='utf-8')
##
##user   = 'data'
##pwd    = 'skst'
##host   = '192.168.1.15'
##db     = 'wwere_v3'
##cnx    = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
##cursor = cnx.cursor()
##
##dic = {}
##for s in f1:
##    try:
##        if len(s)<5 and len(dic.keys())==0:
##            dic = {}
##        elif len(s)<5 and len(dic.keys()):
##            for k in dic:
##                if len(dic[k])==1:
##                    pass
##                else:
##                    sql1 = 'SELECT sourceId FROM townfile_local WHERE localId in %s'% '('+','.join(dic[k])+')'
##                    cursor.execute(sql1)
##                    result = cursor.fetchall()
##                    allsource = []
##                    #print(result)
##                    for source in result:
##                        for i in source[0].split(','):
##                            allsource.append(i)
##                    if len(list(set(allsource)))==1:
##                        pass
##                    else:
##                        allsource = ','.join(list(set(allsource)))
##                        sql2 = 'UPDATE townfile_local SET sourceId = "%s" WHERE localId = %s;\n'% (allsource,min(dic[k]))
##                        f3.write(sql2)
##                    #minId = min(dic[k])
##                    dic[k].remove(min(dic[k]))                    
##                    for m in dic[k]:
##                        sql = 'DELETE FROM townfile_local WHERE localId = %s;\nDELETE FROM shop_local WHERE localId = %s;\n'% (m,m)
##                        f3.write(sql)
##            dic = {}  
##                    
##        else:
##            b = re.split(';|\n',s)
##            sourceId = b[-2].split(',')
##            for t in sourceId:
##                if t in dic.keys():
##                    dic[t].append(b[0])
##                elif t=='':
##                    pass
##                else:
##                    dic[t] = [b[0]]
##    except:
##        print('error!  '+s)
##
##f1.close()
##f3.close()
##cnx.commit()
##cursor.close()
##cnx.close()
