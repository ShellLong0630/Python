import httplib2,urllib.request,re,os,time,mysql.connector,random


url='http://www.daodao.com/Attractions-g60763-Activities-c47-New_York_City_New_York.html'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
req    =urllib.request.Request(url,None,headers)
content=urllib.request.urlopen(req).read().decode('utf-8')


if re.findall('地标',content):
    #print(content)
    count    = int(re.findall('地标\(([\d]+)\)',content)[0])
    landmark = re.findall('<a href="/Attraction_Review-([\S]+)" class=',content)
    print(count)
    print(str(landmark).replace("', '",'\nhttp://www.daodao.com/Attraction_Review-').replace("'",''))

