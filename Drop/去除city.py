import re

file1 = 'D:\\张玉龙\\Python\\20140314_url_city.txt'
file2 = 'D:\\张玉龙\\Python\\20140316_url.txt'
file3 = 'D:\\张玉龙\\Python\\20140316_nourl.txt'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')
f3    = open(file3,'w',encoding='utf-8')

for s in f1:
    localId = re.split(',',s)[0]
    b=re.split('","',s)
    if re.findall('d',str(localId)):
        b[0] = re.sub('^d','',b[0])
        string = '%s","%s",""\n'% (b[0],b[1])
        f3.write(string)
    else:
        string = '%s","%s","%s'% (b[0],b[1],b[3])
        f2.write(string)
f1.close()
f2.close()
f3.close()
        
