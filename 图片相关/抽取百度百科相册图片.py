import re,os,json

path = 'D:\\张玉龙\\Python\\Baidu_Album'
f1   = open('D:\\张玉龙\\Python\\20140415_picUrl_baidu.txt','w',encoding='utf-8')

for file in os.listdir(path):
    #print(file)
    f = open(os.path.join(path,file),'r',encoding='utf-8')
    content = f.read()
    pic = {}
##    album = re.findall('albumList : \[({[\S ]+})\],summary:',content)
##    if album:
##        if len(re.findall('"albums"},{',album[0]))==0:
##            album = json.loads(album[0])
##            for t in album['pic'].keys():
##                img = album['pic'][t]['sizes'][max(album['pic'][t]['sizes'].keys())]['url']
##                f1.write(img)
##        else:
##            albums = re.split('"albums"},',album[0])
##            for a in albums:
##                if a!=albums[-1]:
##                    album = json.loads(a+'"albums"}')
##                    for t in album['pic'].keys():
##                        img = album['pic'][t]['sizes'][max(album['pic'][t]['sizes'].keys())]['url']
##                        f1.write(img)
##                else:
##                    album = a
##                    album = json.loads(album)
##                    for t in album['pic'].keys():
##                        img = album['pic'][t]['sizes'][max(album['pic'][t]['sizes'].keys())]['url']
##                        f1.write(img)                    
##        #print(album['pic'][list(album['pic'].keys())[0]]['sizes'][(max(album['pic'][list(album['pic'].keys())[0]]['sizes'].keys()))]['url'])
##        #break
##    else:
##        print('None  ',file)
    pics = re.findall('("[\d]+":{"url":"http:\\\\/\\\\/[a-z]+.hiphotos.baidu.com\\\\/baike\\\\/[^,"]+\.[a-z]+)"',content)
    if pics:
        for p in pics:
            size = re.findall('"([\d]+)":{"url":"http:',p)[0]
            url  = re.findall('"url":"(http:\\\\/\\\\/[a-z]+.hiphotos.baidu.com\\\\/baike\\\\/[^,"]+\.[a-z]+)',p)[0]
            key  = re.split('/',url)[-1]
            if key not in pic.keys():
                pic[key]=[]
            pic[key].append((url,size))
        #print(pic)
        for k in pic:
            a = []
            for p in pic[k]:
                a.append(int(p[1]))
            a=list(set(a))
            for p in pic[k]:
                if int(p[1])==max(a):
                    string = '%s,"%s"\n'% (file.split('.')[0],p[0].replace('\\',''))
                    if re.findall('/s%3D',string):
                        pass
                    else:
                        f1.write(string)
                    #print(string)
                    break
    else:
        print('null ',file)
    #break
    f.close()
f1.close()
