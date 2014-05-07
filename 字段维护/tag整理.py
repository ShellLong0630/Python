import re

##f1 = open('D:\\张玉龙\\Python\\20140417_tag_update.txt','r',encoding='utf-8')
##f2 = open('D:\\张玉龙\\Python\\20140417_tag_update_1.txt','w',encoding='utf-8')
#----tag映射整理
##tag = {'马术步道':'Attractions', 'Amateur Sports Teams':'Stadium', '越野/沙滩车步道':'Attractions', '滑雪区':'Skiing', '矿山':'Mountain', '商店':'Market', 
##'观光巴士':'Attractions', '山脉':'Mountain', '森林':'Attractions', '公园':'Park', '芭蕾舞':'Theater', '灵异景点':'Attractions', '赌场':'Attractions',
##'体育馆':'Stadium','自然历史博物馆':'Museum', '游戏/娱乐中心':'Attractions', '自然/野生动物区':'Attractions', 'attractions':'Attractions', '观景台/塔':'Attractions', 
##'运动营/健诊营':'Sports', '单车步道':'Attractions', '艺术博物馆':'Museum', '渡轮/船':'Attractions', '农场':'Attractions', '动物园':'Zoo', '艺术建筑':'Attractions', 
##'水坝':'Attractions', '景观/史迹徒步区':'Historical Relics', '教育施设':'Education', '岩矿观光':'Mountain', '工厂参访':'Attractions', '码头/木板/人行道':'Attractions', 
##'马厩':'Attractions', '迪士尼':'Theme Park', '公共交通系统':'Attractions', '名产店':'Market', 'Landmarks & Historical Buildings':'Attractions',  
##'竞技场/体育场':'Stadium', 'Bay':'Bay', 'Education':'Education', '葡萄酒庄':'Attractions', '铁路观景游':'Attractions', '海滩':'Beach', '大洞穴/洞窟':'Attractions', 
##'其他':'Attractions', '百货公司':'Market', '船舶':'Attractions', '古迹':'Historical Relics', '国家公园':'National Park', '水族馆':'Attractions', 'Temple':'Temple', 
##'教堂':'Church', '牧场':'Attractions', '军事博物馆':'Museum', '演唱会':'Theater', '温泉観光地':'Attractions', 'Parks':'Park', 'Gallery':'Gallery', 
##'旅客服务中心':'Attractions', '桥梁':'Bridge', 'Public Transportation':'Attractions', '步行游览':'Attractions', '教育景点':'Education', 'Attractions':'Attractions', 
##'保龄球馆':'Sports', '古代遗址':'Historical Relics', '水域':'Attractions', '游艇码头':'Attractions', '卡拉OK酒吧':'KTV', 'Beach':'Beach', 'Church':'Church', 
##'酿酒厂':'Attractions', '海湾':'Bay', '建筑物':'Attractions', '墓园':'Memorial', 'Bridge':'Bridge', '史迹徒步区':'Historical Relics', '珊瑚礁':'Attractions', 
##'观景台/天文台':'Attractions', '火山':'Mountain', '旅游':'Attractions', 'Arts & Entertainment':'Attractions', '徒步观景区':'Attractions', '儿童博物馆':'Museum', 
##'蓝调酒吧':'Bar', '自驾旅游':'Attractions', '旅客/游客中心':'Attractions', '水上乐园':'Theme Park', 'Local Flavor':'Restaurant', '购物中心':'Market', '州立公园':'Park', 
##'铁路旅游':'Attractions', '健身中心':'Sports', 'Memorial':'Memorial', '舞厅/迪斯可':'Attractions', 'Travel Services':'Attractions', 'Shopping Centers':'Market', 
##'Mountain':'Mountain', '山谷':'Mountain', '博物馆':'Museum', '交通工具':'Attractions', 'Garden':'Garden', '天然涌泉/温泉':'Attractions', '冲浪营地':'Attractions', 
##'景点':'Attractions', '电车':'Attractions','花园':'Garden','剧场':'Theater','游艇':'Attractions','图书馆':'Library','Skiing':'Skiing','城堡':'Attractions',
##'Theme Park':'Theme Park', '自然保育区':'Attractions', '主题乐园':'Theme Park', '畅货中心':'Market', '会议中心':'Conference', '纪念碑/雕像':'Memorial','预订':'Attractions', 
##'餐馆剧院':'Theater', '啤酒厂':'Attractions', '慢跑步道':'Attractions', 'Spa':'Attractions', '战地史迹':'Historical Relics', '歌剧':'Theater', 'Art Galleries':'Gallery', 
##'沙漠':'Attractions', '街坊':'Attractions', '酒吧/俱乐部':'Bar', '步道':'Attractions', '大众交通':'Attractions', '军事基地/设施':'Attractions', '游乐场':'Theme Park', 
##'National Park':'National Park', '竞技场/体育场/运动场':'Stadium', '古董店':'Market', '政府机关':'Government', 'Park':'Park', '自驾观景游':'Attractions', 
##'Stadiums & Arenas':'Stadium', '度假社区':'Attractions', '政府建筑':'Government', '喷泉':'Attractions', '空城':'Attractions', '游乐园/主题乐园':'Theme park', 
##'跳蚤市场/露天市集':'Market', '电影院':'Theater', '健行步道':'Attractions', 'Historical Relics':'Historical Relics', '历史古迹':'Historical Relics', '岛屿':'Island', 
##'宗教地点':'Temple', 'Restaurant':'Restaurant', '瀑布':'Attractions', '码头':'Attractions', '了望台':'Attractions', '渡假中心':'Attractions', '邻近地区':'Attractions', 
##'Golf':'Golf', '赛车场':'Attractions', 'Venues & Event Spaces':'Attractions', '特色博物馆':'Museum', 'Museum':'Museum', '市政中心':'Government', 
##'水上运动':'Sports', '高尔夫球场':'Golf', '表演':'Theater', 'Skating Rinks':'Attractions', '澳洲料理':'Restaurant', '灯塔':'Attractions', '科学博物馆':'Museum', 
##'综合体育馆':'Stadium', '码头/堤防/人行道':'Attractions', 'Hotel':'Hotel', '历史博物馆':'Museum', '大峡谷':'Attractions', '预约式':'Attractions', 
##'教堂/大教堂':'Church', '美术馆':'Gallery', 'Tours':'Attractions', 'Government':'Government', '咖啡馆':'Coffee', '路面电车':'Attractions', '画廊':'Gallery', 
##'「课程/工作坊」':'Attractions'}
##for s in f1:
##    b = re.split('"',s)
##    a = []
##    for t in re.split(',',b[-2]):
##        if tag[t] not in a:
##            a.append(tag[t])
##        else:
##            pass
##    if len(a)>1 and 'Attractions' in a:
##        a.remove('Attractions')
##    string = '%s"%s","%s"\n'% (b[0],b[1],a[0])
##    f2.write(string)
##f1.close()
##f2.close()

#----生成sql
f1 = open('D:\\张玉龙\\Python\\20140417_tag_update_1.txt','r',encoding='utf-8')
f2 = open('D:\\张玉龙\\Python\\提交\\20140420_UPDATE_tag.sql','w',encoding='utf-8')

for s in f1:
    b = re.split(',|"',s)
    sql = 'UPDATE landmark SET tag = "%s", updateTime = "2014-04-20 10:00:00" WHERE localId = %s ;\n'% (b[-2],b[0])
    f2.write(sql)

f1.close()
f2.close()
