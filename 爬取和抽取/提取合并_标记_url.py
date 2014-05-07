import re,os
f3 = open('D:\\张玉龙\\Python\\20140504_url1.txt','w',encoding='utf-8')
f2 = open('D:\\张玉龙\\Python\\20140504_url2.txt','w',encoding='utf-8')

##b = []
##for s in f3:
##    if re.findall('^[1-9]',s):
##        b.append(re.split(',',s)[0])
##        f2.write(s)
##    else:
##        pass
##b = set(b)

for f in os.listdir('D:\\张玉龙\\Python\\url_0504'):
    #print(f)
    f1=open(os.path.join('D:\\张玉龙\\Python\\url_0504',f),'r',encoding='utf-8')
    string = re.split('\n\n',f1.read())[0]
    if re.findall('^S',f):
        f3.write(string)
    else:
        f2.write(string)
#----标记关键词完全匹配的url
##    c = re.split(',',string)
##    if c[0] not in b:
##        b = list(b)
##        b.append(c[0])
##        b = set(b)
##        if c[1]==c[2]:
##            f2.write('y'+string)
##        else:
##            f2.write(string)
##    else:
##        pass
    f1.close()
f2.close()
f3.close()
