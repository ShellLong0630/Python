import re

file = 'd:/张玉龙/Python/20140304_landmarks_update_CN_n&d_s9.txt'
file2= 'd:/张玉龙/Python/20140304_landmarks_update_CN_d.txt'
f1   = open(file,'r',encoding='utf-8')
f2   = open(file2,'w',encoding='utf-8')
dic_d = ['博物馆','美术馆','机场','观','大学','学院','庙','纪念馆',
         '寺','庵','火车站','文化广场','滑雪场','山',
         '遗址','图书馆','景区','故居','旧居','break']
#dic_mark = {}
for s in f1:
    b=re.split('",',s.replace('\n',''))
    star = b[-1]
    name = b[-2]
    if re.findall('^[a-z]',s):
        f2.write(s)
    elif re.findall('园$',b[-2]) and re.findall('国家',b[-2]):
        f2.write('d'+s)
    elif re.findall('园$',b[-2]) and re.findall('省',b[-2]):
        f2.write('d'+s)
    else:
        for t in dic_d:
            if t=='break':
                f2.write(s)
                break
            elif re.findall(t+'$',b[-2]):
                f2.write('d'+s)
                break
    '''
    if name=='"':
        f2.write('n'+s)
    elif name not in dic_mark.keys():
        if int(star)>7:
            dic_mark[name]=s
            f2.write('d'+s)
        else:
            f2.write(s)
    else:
        f2.write('n'+s)
    '''
f1.close()
f2.close()
