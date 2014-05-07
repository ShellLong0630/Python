import re,os

path = 'D:\\张玉龙\\Python\\linkUrl_html'
f1   = open('D:\\张玉龙\\Python\\20140414_picUrl_baidu.txt','w',encoding='utf-8')
for file in os.listdir(path):
    f = open(os.path.join(path,file),'r',encoding='utf-8')
    content = f.read()
    jpg = ''
    if re.findall('^w_',file):
        pass
##        jpg = re.findall('<img[^<]+src="(//upload.wikimedia.org/wikipedia/commons/[\S]+/[\S]+/[\S]+\.jpg)/[\S]+\.jpg"',content,flags=re.I)
##        if jpg:
##            if jpg[0]!='//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Platopainting.jpg':
##                jpg = jpg[0].replace('/thumb/','/')
##                string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##                f1.write(string)
##            else:
##                #jpg = re.findall('src="(//upload.wikimedia.org/wikipedia/zh/thumb/[\S]+/[\S]+/[\S]+\.[^s]+)/[\S]+\.[^s]+"',content)
##                jpg = re.findall('src="(//upload.wikimedia.org/wikipedia/zh/[\S]+/[\S]+/[\S]+\.jpg)/[\S]+\.jpg"',content,flags=re.I)
##                if jpg:
##                    jpg = jpg[0].replace('/thumb/','/')
##                    string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##                    #print(string)
##                    f1.write(string)
##                else:
##                    jpg = re.findall('<img[^<]+src="(//upload.wikimedia.org/wikipedia/commons/[\S]+/[\S]+/[\S]+\.png)/[\S]+\.png"',content,flags=re.I)
##                    if jpg:
##                        jpg = jpg[0].replace('/thumb/','/')
##                        string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##                        f1.write(string)
##                    else:
##                        #jpg = re.findall('src="(//upload.wikimedia.org/wikipedia/zh/thumb/[\S]+/[\S]+/[\S]+\.[^s]+)/[\S]+\.[^s]+"',content)
##                        jpg = re.findall('src="(//upload.wikimedia.org/wikipedia/zh/[\S]+/[\S]+/[\S]+\.png)/[\S]+\.png"',content,flags=re.I)
##                        if jpg:
##                            jpg = jpg[0].replace('/thumb/','/')
##                            string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##                            #print(string)
##                            f1.write(string)
##                        else:
##                            jpg = re.findall('src="(//upload.wikimedia.org/wikipedia/zh/[\S]+/[\S]+/[\S]+\.[^s]+)/[\S]+\.[^s]+"',content,flags=re.I)
##                            if jpg:
##                                jpg = jpg[0].replace('/thumb/','/')
##                                string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##                                #print(string)
##                                f1.write(string)
##                            else:
##                                jpg = re.findall('src="(//upload.wikimedia.org/wikipedia/zh/[\S]+/[\S]+/[\S]+\.jpg)"',content,flags=re.I)
##                                if jpg:
##                                    jpg = jpg[0].replace('/thumb/','/')
##                                    string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##                                    #print(string)
##                                    f1.write(string)
##                                else:
##                                    print(file)
##    elif re.findall('^s_',file):
##        content = content.replace('http://pic.baike.soso.com/p/20140324/20140324113648-1861503478.jpg','')
##        jpg = re.findall('http://pic.baike.soso.com/[\S]+/[\S]+/[\S]+\.jpg',content,flags=re.I)
##        if jpg:
##            jpg = jpg[0]
##            string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##            #print(string)
##            f1.write(string)
##            f.seek(0)
##        elif re.findall('img ',content):
##            print(file)
##        else:
##            print(file)
##    elif re.findall('^h_',file):
##        jpg = re.findall('http://[\S]+\.att\.hudong.com/[\S]+/[\S]+/[\S]+.jpg"',content,flags=re.I)
##        if jpg:
##            jpg = jpg[0].split('_')[0]+'.jpg'
##            string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],jpg)
##            #print(string)
##            f1.write(string)
##            f.seek(0)
##        elif re.findall('img ',content):
##            print(file)
##        else:
##            print(file)
    elif re.findall('^b_',file):
        url = re.findall('href="(/picview/[\S]+\.html\?fr=lemma)"',content)
        if url:
            url = 'http://baike.baidu.com'+url[0]
            string = '%s,"%s"\n'% (re.findall('_([\d]+).',file)[0],url)
            #print(string)
            f1.write(string)
    elif re.findall('^e_',file):
        pass
    f.close()     


f1.close()
