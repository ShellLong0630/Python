import httplib2,urllib.request,re,os,time,mysql.connector,random

f1 = open('d:/张玉龙/Python/url.txt','w',encoding='utf-8')

host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db   = 'wwere_v3'
cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
cursor = cnx.cursor()
#sql = 'SELECT m.localId,n.localName,m.star FROM local_stars m left join townfile_local n ON m.localId=n.localId WHERE landmark>0 limit 500'
sql = "SELECT t.localId,t.localName,c.cityName FROM landmark l left join townfile_local t on l.localId = t.localId left join city c on t.cityId = c.cityId where l.updateTime = '2014-04-01 17:00:00'"
cursor.execute(sql)

result = cursor.fetchall()
#print(result)
#user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'
#headers={'User-Agent':user_agent,} 
for s in result:
    try:
        string = urllib.request.quote(s[2]+''+s[1])
        #city = urllib.request.quote(s[2])
        url = 'http://www.baidu.com/baidu?word='+string+'%20wikipedia&ie=utf-8'
        content=urllib.request.urlopen(url).read().decode('utf-8')
        find = '		><em>%s</em> - <em>维基百科</em>,自由的百科全书</a>'% s[1]
        i=0
        file2 = 'd:/张玉龙/Python/url/%s.txt'% s[0]+'_'+s[1]
        f2 = open(file2,'w',encoding='utf-8')
        f2.write(content)
        f2.close()
        f3 = open(file2,'r',encoding='utf-8')
        for t in f3:
            write=''
            if re.findall(find,t):
                i=1
            elif re.findall('          href="http://www.baidu.com/link',t):
                url = re.split('href=',t)[1]
                i+=1
                if i==2:
                    write = '%s,"%s",%s'% (s[0],s[1],url)
                    f1.write(write)
                    break
                else:
                    break
        if not write:
            write = '%s,"%s",%s'% (s[0],s[1],'""\n')
            f1.write(write)
        f3.close()
    except:
        print(s)

cnx.commit()
cursor.close()
cnx.close()
f1.close()





#url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%E5%A4%A9%E5%AE%89%E9%97%A8'
#url = 'http://cn.bing.com/search?q=%E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6&src=IE-TopResult&FORM=IE10TR'
#url = 'http://so.360.cn/s?q=%s&src=se6_addr&ie=utf-8'% string
#url = 'http://www.google.com.hk/search?newwindow=1&safe=strict&q=%s'% string
#url = 'http://www.google.com.hk/search?client=aff-360daohang&hl=zh-CN&ie=utf-8&newwindow=1&q=%s'% string
