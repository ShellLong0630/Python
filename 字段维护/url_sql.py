import re,urllib.request
file1 = 'D:\\张玉龙\\Python\\20140319_url.txt'
file2 = 'D:\\张玉龙\\Python\\提交\\20140319_UPDATE_url.sql'
f1    = open(file1,'r',encoding='utf-8')
f2    = open(file2,'w',encoding='utf-8')

for s in f1:
    if re.findall('"n"$',s):
        pass
    else:
        b = re.split(',|"',s)
        url = urllib.request.quote(b[-2])
        string = 'UPDATE local_stars SET url = "%s" WHERE localId = %s ; \n'% (url,b[0])
        f2.write(string.replace('%3A',':'))
f1.close()
f2.close()
    
    
