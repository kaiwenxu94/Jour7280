Fixed_Cost = 3000000
Content_Cost = 7000000
member_ff = 15
convert_rate = 0.1
ad_revenue_each_person = 1
subscribers=0
net_income=0.1*subscribers*member_ff+ad_revenue_each_person*subscribers-Fixed_Cost-Content_Cost
if net_income==0:
    print(subscribers)
else:
    while subscribers>=0:
        subscribers=subscribers+10000
        if subscribers<50000:
            net_income=0.1*subscribers*member_ff+ad_revenue_each_person*subscribers-Fixed_Cost-Content_Cost
        else:
            net_income=0.1*subscribers*member_ff+ad_revenue_each_person*subscribers-Fixed_Cost-Content_Cost-0.1*(subscribers-50000)
        if net_income>=0:
            break

while subscribers>=0:
    subscribers=subscribers-1
    if subscribers<50000:
        net_income=0.1*subscribers*member_ff+ad_revenue_each_person*subscribers-Fixed_Cost-Content_Cost
    else:
        net_income=0.1*subscribers*member_ff+ad_revenue_each_person*subscribers-Fixed_Cost-Content_Cost-0.1*(subscribers-50000)
        if net_income<0:
            break

subscribers=subscribers+1
print(subscribers)