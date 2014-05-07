import urllib.request,mysql.connector
import re
import json

host  = '192.168.1.15'
user  = 'data'
pwd   = 'skst'
db    = 'wwere_v3'
file1 = 'd:/张玉龙/Python/提交/20140409_UPDATE_aliasName.txt'
file2 = 'd:/张玉龙/Python/提交/20140409_raw__aliasName.txt'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')
cnx   = mysql.connector.connect(host=host,database=db,user=user,password=pwd)
cursor= cnx.cursor()
for s in f1:
    localId = re.findall('localId = ([\d]+);',s)[0]
    aliasName = re.split('aliasName = "|", up',s)[1]
    sql = 'SELECT localName FROM townfile_local WHERE localId = %s'% localId
    cursor.execute(sql)
    result = cursor.fetchall()
    string = '%s,"%s","%s"\n'% (localId,result[0][0],aliasName)
    #print(string)
    f2.write(string)
f1.close()
f2.close()
cnx.commit()
cursor.close()
cnx.close()

##sql = "SELECT l.localId,t.localName FROM landmark l left join townfile_local t on l.localId=t.localId where l.landmarkRank>0 and t.countryId not in ('cn','mo','hk','tw') and t.localName regexp '^[a-z]' and t.aliasName='' and l.updateTime > '2014-04-01 00:00:00'"
##cursor.execute(sql)
##name = cursor.fetchall()
##i=0
##for s in name:
##    print(i)
###----访问有道词典的网页，并抽取翻译结果
##    msg=s[1]
##    #msg = urllib.request.quote(msg)
##    #url = 'http://dict.youdao.com/search?q='+msg+'%20Place&keyfrom=fanyi.smartResult'
####    url = 'http://dict.youdao.com/search?le=eng&q='+msg+'&keyfrom=dict.top'
####    result = urllib.request.urlopen(url).read().decode('utf-8')
####    translate = ''
####    if re.findall('''<span>
####                ([\S ]+)</span>''',result):
####        translate = re.findall('''<span>
####                ([\S ]+)</span>''',result)
####        #print(translate)
####    elif re.findall('''                          ([\S ]+)
####              </p>''',result):
####        translate = re.findall('''                          ([\S ]+)
####              </p>''',result)
####        #print(translate)
##    url = 'http://fanyi.youdao.com/openapi.do'
##    key = '1102910165' #有道API key
##    keyfrom = 'lifeix'
##    msg = urllib.request.quote(msg)
##    url = url + '?keyfrom=' + keyfrom + '&key='+ key + '&type=data&doctype=json&version=1.1&q=' + msg
##    #print(urllib.request.quote('George Square'),msg,url)
##    result = urllib.request.urlopen(url).read().decode('utf-8')
##    #print(result)
##    json_result = json.loads(result)
##    try:
##        if 'web' in json_result.keys():
##            #if json_result["web"][0]['value']:
##            translate = json_result["web"][0]['value'][0]
##        else:
##            translate = json_result["translation"][0]
##    except:
##        translate = ''
##    if translate:
##        string = 'UPDATE townfile_local SET aliasName = "%s", updateTime = "2014-04-09 17:00:00" WHERE localId = %s;\n'% (translate.replace('"','\\"'),s[0])
##        #print(string)
##        f1.write(string)
##        #break
##    i+=1
##f1.close()
##cnx.commit()
##cursor.close()
##cnx.close()
#----访问有道词典的网页，并抽取翻译结果
##while True:
##    msg=input()
##    if msg == 'quit':
##        break
##    msg = urllib.request.quote(msg)
##    #url = 'http://dict.youdao.com/search?q='+msg+'%20Place&keyfrom=fanyi.smartResult'
##    url = 'http://dict.youdao.com/search?le=eng&q='+msg+'&keyfrom=dict.top'
##    result = urllib.request.urlopen(url).read().decode('utf-8')
##    if re.findall('''<span>
##                ([\S ]+)</span>''',result):
##        translate = re.findall('''<span>
##                ([\S ]+)</span>''',result)
##        print(translate)
##    elif re.findall('''                          ([\S ]+)
##              </p>''',result):
##        translate = re.findall('''                          ([\S ]+)
##              </p>''',result)
##        print(translate)

#----使用有道Api请求，对于地名不够智能
##while True:
##    msg=input()
##    if msg == 'quit':
##        break
##    url = 'http://fanyi.youdao.com/openapi.do'
##    key = '1102910165' #有道API key
##    keyfrom = 'lifeix'
##    msg = urllib.request.quote(msg)
##    url = url + '?keyfrom=' + keyfrom + '&key='+ key + '&type=data&doctype=json&version=1.1&q=' + msg
##    print(url)
##    result = urllib.request.urlopen(url).read().decode('utf-8')
##    print(result)
##    json_result = json.loads(result)
##    json_result = json_result["web"][0]['value']
##    print(json.loads(result)["translation"])
##    for i in json_result:
##        print(i)
