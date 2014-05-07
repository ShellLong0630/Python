
import httplib2,urllib.request,re,os,time,mysql.connector,random
'''
#f1 = open('d:/张玉龙/Python/star.txt','a',encoding='utf-8')

host = '192.168.1.15'
user = 'data'
pwd  = 'skst'
db   = 'd01_backup'
cnx  = mysql.connector.connect(user=user,host=host,password=pwd,database=db)
cursor = cnx.cursor()

sql = 'SELECT m.localId,n.localName,m.star FROM local_stars m left join townfile_local n ON m.localId=n.localId WHERE star>8 limit 500'
cursor.execute(sql)
result = cursor.fetchall()
#user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'
#headers={'User-Agent':user_agent,} 
#for s in result:
#try:
#string=s[1]
string = urllib.request.quote('天安门')
#url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%E5%A4%A9%E5%AE%89%E9%97%A8'
#url = 'http://cn.bing.com/search?q=%E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6&src=IE-TopResult&FORM=IE10TR'
#url = 'http://so.360.cn/s?q=%s&src=se6_addr&ie=utf-8'% string
#url = 'http://www.google.com.hk/search?newwindow=1&safe=strict&q=%s'% string
#url = 'http://www.google.com.hk/search?client=aff-360daohang&hl=zh-CN&ie=utf-8&newwindow=1&q=%s'% string
#url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s'% string
url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyCn_IE6NM_ATjZ0j5vfXIFlyW-EpGs5gsU&cx=006431901905483214390:i3yxhoqkzo0&num=1&alt=atom&q=%s'% string
#url = 'http://www.google.com/search?q=%s'% string
#url='https://www.google.com.hk/search?newwindow=1&safe=strict&q=%s&gs_l=serp.3...11112.11112.0.11320.1.1.0.0.0.0.84.84.1.1.0....0...1c.1.36.serp..1.0.0.0usSDow3XaY'% string
print(url)
content=urllib.request.urlopen(url).read().decode('utf-8')
#num = re.findall('找到约 ([\d,]+) 条结果',content)[0].replace(',','')
print(content)
#write = '%s;"%s";%s;"%s"\n'% (s[0],s[1],s[2],num)
#f1.write(write)
    #except:
    #    print(s)
#f1.close()
'''
'''
Created on 2013-1-27
@author: isaced
''' 


f1 = open('d:/张玉龙/Python/num.txt','w',encoding='utf-8')
url = '/search?q=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6/'
#url = '/search?newwindow=1&safe=strict&espv=210&es_sm=93&q=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&oq=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&gs_l=serp.12...0.0.0.86503.0.0.0.0.0.0.0.0..0.0....0...1c..37.serp..0.0.0.IGbKj9hFGbI'
#url = "https://www.google.com.hk/search?q=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&oq=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6"
headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip,deflate,sdch',
    'host':'www.google.com.hk',
    'accept-language':'zh-CN,zh;q=0.8',
    'alexatoolbar-alx_ns_ph':'AlexaToolbar/alxg-3.2',
    'cookie':'SID=DQAAANgAAACiBYYNZW42MT7rij7WOcJO0uHcqJ_Aw71CRZJ9ulrCR0lWnaum8oyHdhwGvI-aJH7pSvZjTekIXbWytRgq6Un04ENb7VXTqvye6Rht-0MgH8MziwEUFYtAr65l7OO4M8k_Xip9eTlm4cvojWbKrmvtYbo0LHVOyvMvJkOq-pYfPGVwDcsXBrJWFwjUzR3b91qqvW0Qc5prvHDVkco9L9JzEld6Jyezpn4inSIIystt6VzqeFfUZZ4xHfgs1uAfhQOHAqM47LgC0p6YbgwAjzFbrECmSHK_ElYsRgqrrK-YSA; HSID=Axkjo3hW8pZsibDZG; SSID=A-XGWJg20xbraXZyv; APISID=61JHKwfTJtSdvXzb/AA4KTTMemzVq1pegJ; SAPISID=_eg4WDVqBRxo0lQt/Ag1pZWaA83tW3Cj4M; NID=67=mm8p7NZARq6tY0TYiei0P4L62Iv4tc5Zg4pIJ63aAfjSJaioM7p6ISSYSF5Geen_ZGPpQzRnf4PqFRjz1zvu3O7gBadGhVpQjZ1_onld7CjGwkgTLJ3DebG7gnFMwlvPSf6EW9StVMNyWBSKDmG7kBOo8nv-omnTtQMJHZRxWLNbjqUa80Nm_y_hyTvT2JN4JRA02tyw; PREF=ID=e9f35f65658935eb:U=792008ef727cea29:FF=2:LD=zh-CN:NW=1:TM=1381902429:LM=1394073401:GM=1:S=yn4w7B7PhvYXSTWG',
    'referer':'https://www.google.com.hk/',
    'user-agent':['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \(KHTML, like Gecko) Element Browser 5.0', 
         'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', 
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', 
         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', 
         'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \Version/6.0 Mobile/10A5355d Safari/8536.25', 
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/28.0.1468.0 Safari/537.36', 
         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)'],
    'x-client-data':'CO+1yQEIj7bJAQijtskBCKm2yQEIwbbJAQiehsoBCKeIygEIuYjKAQ=='
    }
con = httplib2.http.client.HTTPConnection('www.google.com.hk')
index = random.randint(0,8)
headers['user-agent'] = headers['user-agent'][index]
con.request(method='GET',url=url,headers = headers)
res = con.getresponse()

data = res.read().decode('utf-8')
if re.findall('条',data):
    print(data)
print(res.status)
f1.write(data)
f1.close()
con.close()

'''
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
        (KHTML, like Gecko) Element Browser 5.0', \
        'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
        'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
        Version/6.0 Mobile/10A5355d Safari/8536.25', \
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/28.0.1468.0 Safari/537.36', \
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
class google():
    def __init__(self):
        self.url= '' 
        self.title = '' 
        self.content = '' 
    def search(self,queryStr):
        queryStr = urllib.request.quote(queryStr)
        url = 'https://www.google.com.hk/search?hl=en&q=%s' % queryStr
        request = urllib.request.Request(url)
        index = random.randint(0, 9)
        user_agent = user_agents[index]
        request.add_header('User-agent', user_agent)
        response = urllib.request.urlopen(request)
        html = response.read()
        results = self.extractSearchResults(html)
        return results
    def extractSearchResults(self, html):
            results = list()
            soup = BeautifulSoup(html)
            div = soup.find('div', id  = 'search')
            if (type(div) != types.NoneType):
                lis = div.findAll('li', {'class': 'g'})
                if(len(lis) > 0):
                    for li in lis:
                        result = SearchResult()
                        h3 = li.find('h3', {'class': 'r'})
                        if(type(h3) == types.NoneType):
                            continue

                        # extract domain and title from h3 object
                        link = h3.find('a')
                        if (type(link) == types.NoneType):
                            continue

                        url = link['href']
                        url = self.extractDomain(url)
                        if(cmp(url, '') == 0):
                            continue
                        title = link.renderContents()
                        result.setURL(url)
                        result.setTitle(title)

                        span = li.find('span', {'class': 'st'})
                        if (type(span) != types.NoneType):
                            content = span.renderContents()
                            result.setContent(content)
                        results.append(result)
            return results
queryStr = '北京大学'
search(queryStr)
'''


