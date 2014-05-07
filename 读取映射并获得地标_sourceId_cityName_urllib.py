import json,re
import httplib2,urllib.request,re,os,time,mysql.connector,random

file = 'D:\\张玉龙\\Python\\POIs_tripadvisor_20131210.txt'
#file2 = 'D:\\张玉龙\\Python\\tripadvisor_landmark_html.txt'
f1   = open(file,'r',encoding='utf-8')
#f2   = open(file2,'w',encoding='utf-8')

dic = {}
i=0
for s in f1:
    landmarks = []
    j = json.loads(s)
    sourceId = re.split('_|-',j['sourceId'])[1]
    if sourceId in ['g1526974','g187216','g187498','g189525','g189527','g190456',
                    'g2391375','g255060','g297437','g298129','g298523','g33256']:#not in dic.keys():
        if os.path.isfile('D:\\张玉龙\\Python\\landmarks\\'+sourceId+'.txt')== False:
            dic[sourceId] = (j['city'],j['provice'])
            url='http://www.daodao.com/Attractions-%s-Activities-c47-%s_%s.html'% (sourceId,j['city'],j['provice'])
            headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
            req    =urllib.request.Request(url,None,headers)
            content=urllib.request.urlopen(req).read().decode('utf-8')

            if re.findall('地标\([\d]+\)',content):
                count    = int(re.findall('地标\(([\d]+)\)',content)[0])            
                if count <16:
                    print(count,sourceId)
                    landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)[0:count]
                    for m in landmark:
                        landmarks.append(m)
                else:
                    landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)
                    for m in landmark:
                        landmarks.append(m)
                    page     = int(re.findall('</b>/([\d]+)页</span>',content)[0])
                    print(count,page,sourceId)
                    for t in range(page):
                        if t==0:
                            pass
                        else:
                            url='http://www.daodao.com/Attractions-%s-Activities-c47-oa%s-%s_%s.html'% (sourceId,str(15*t),j['city'],j['provice'])
                            headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
                            req    =urllib.request.Request(url,None,headers)
                            content=urllib.request.urlopen(req).read().decode('utf-8')
                            landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)
                            for m in landmark:
                                landmarks.append(m)
                file2 = 'D:\\张玉龙\\Python\\landmarks\\'+sourceId+'.txt'
                f2   = open(file2,'w',encoding='utf-8')
                for k in landmarks:
                    f2.write(k+'\n')
                f2.close()

f1.close()

