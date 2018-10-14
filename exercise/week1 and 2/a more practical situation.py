visitors=int(input('please enter expected number of visitors:'))
content=70000
labor=30000
server=50000
rate=0.1
sub_fee=15
ad=0.8

if visitors<=50000:
	net_income=0.1*visitors*sub_fee+ad*visitors-content-labor-server
else:
    net_income=0.1*visitors*sub_fee+ad*visitors-content-labor-server-0.001*(visitors-50000)
