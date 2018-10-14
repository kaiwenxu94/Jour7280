a=input('please enter today\'s Dow Jones Industrial Average closing price:')
b=input('please enter yesterday\'s Dow Jones Industrial Average closing price:')
c=round(abs((float(a)/float(b)-1)*100),2)
if (float(a)-float(b))<0:
    verb='dropped'
else:
    verb='rose'
print('On Wall Street today, The Dow Jones Industrial Average {0} {1} percent to {2} points.'.format(verb,c,a) )
