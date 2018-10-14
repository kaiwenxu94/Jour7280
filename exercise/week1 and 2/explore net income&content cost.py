content=float(input('please enter expected number of content cost:'))
visitors=int(input('please enter expected number of visitors:'))
labor=30000
server=50000
rate=0.1
sub_fee=15
ad=0.8
net_income=0.1*visitors*sub_fee+ad*visitors-content-labor-server