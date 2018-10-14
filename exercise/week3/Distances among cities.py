import math
city=['HongKong','New York','Vancouver','Stockholm','BuenosAires','Perth']
latitude=[22.3964,40.7128,49.2827,59.3293,-34.6037,-31.9505,]
longitude=[114.1095,-74.0060,-123.1207,18.0686,-58.3816,115.8605]
index=[0,1,2,3,4]
r=6371
for x in index:
    a=latitude[x+1]
    c=math.sin(a)
    f=math.cos(a)
    g=longitude[x+1]
    i=math.sin(22.3964)*c+math.cos(22.3964)*f*math.cos(abs(114.1095-g))
    angle=math.acos(i)
    distance=angle*r
    print('distance between {0} and {1}: {2}km'.format('Hong Kong',city[x+1],distance))