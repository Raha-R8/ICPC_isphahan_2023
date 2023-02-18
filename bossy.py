import math

a = input().split()
losers = int(a[0])
players = int(a[1])
money_dict = {}
count = 0
will_dict ={}

def losers_sum1(money_dict,loser_count = losers):
    losers_sum = 0
    for i in range(loser_count):
        a = money_dict[i+1]
        if math.isinf(a):
            a = round(money_dict[i+1],2)
        losers_sum+= a
    return losers_sum
for player in range(1,players+1):
    money_dict[player] = 0


for i in range(losers):
    a =input().split()
    losers_money = int(a[0])
    money_dict[i+1] += losers_money
    will_list = int(a[1])
    will_dict[i+1] = []
    for n in range(will_list):
        count+=1
        a = input().split()
        will_number = int(a[0])
        split_share = float(a[1])
        losers_money = money_dict[i+1]
        money_dict[will_number]+=(split_share*losers_money)
        will_dict[i+1]+=[[will_number,split_share]]
    money_dict[i+1] = 0    


print(money_dict)
print(will_dict)
losers_sum = losers_sum1(money_dict)
while count<20 and losers_sum !=0:
    for loser,m in will_dict.items():
        if losers_money!=0:
            losers_money = money_dict[loser]
            for n in m:
                will_number = n[0]
                split_share = n[1]
                losers_money = money_dict[loser]
                money_dict[will_number]+=(split_share*losers_money)
            money_dict[loser] = 0    
    count+=1
    losers_sum = losers_sum1(money_dict)
for i in money_dict.values():
    i = round(i,2)
    print(int(i))

















#
