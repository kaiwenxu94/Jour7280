# -*- coding: utf-8 -*-
dict={
'荣':'榮',
'国':'國',
'际':'際',
'区':'區',
'域':'域',
'范':'範',
'围':'圍',
'岛':'島',
'龙':'龍',
'个':'個',
'屿':'嶼'
}
content=input('请输入简体字内容：')#香港是一座高度繁荣的国际大都市，区域范围包括香港岛、九龙、新界和周围262个岛屿
list=dict.items()
for x in list:
    content=content.replace(x[0],x[1])
print('繁体字版本：',content)