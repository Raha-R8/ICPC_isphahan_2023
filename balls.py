def main():
    balls = list(input())
    colors = set(balls)
    twodballs = []
    key = 1
    count = 0
    for i in range(len(balls)):    
        if i+1 < len(balls) and balls[i] == balls[i+1]:
            twodballs += [[balls[i],key]]
        else:
            twodballs += [[balls[i],key]]
            key +=1
    for color in colors:
        for i in range(len(twodballs)+1):
            twodballs.insert(i,[color,-1])
            if checkelimination([i[:] for i in twodballs],i):
                count+=1
            del twodballs[i]
    print(count)

def checkelimination(twodballs,i):
    chain = 1
    rightchecker = i+1
    leftchecker = i-1
    moveright = True
    moveleft = True
    while (True):
        if moveright and rightchecker <len(twodballs):
            if twodballs[i][0] == twodballs[rightchecker][0]:
                chain +=1
                rightchecker+=1
            else:
                moveright = False
        if moveleft and leftchecker >=0:
            if twodballs[i][0] == twodballs[leftchecker][0]:
                chain+=1
                leftchecker-=1
            else:
                moveleft = False
        if  leftchecker == -1:
            moveleft = False
        if  rightchecker == len(twodballs):
            moveright = False
        if moveleft + moveright == 0:
            break
    if chain > 2:
        for i in range(chain):
            del twodballs[leftchecker+1]
    else:
        return False
    chain = 0
    lowerlimit = 0
    dif_key = False
    i = 0
    while i < len(twodballs):
        if i+1 < len(twodballs):
            if twodballs[i+1][0] == twodballs[i][0]:
                chain +=1
                if twodballs[i+1][1] != twodballs[i][1]:
                    dif_key = True
            else:
                if chain > 2 and dif_key:
                    for j in range(chain):
                        del twodballs[lowerlimit]
                    dif_key = False
                    chain = 1
                    i = 0
                else:
                    lowerlimit = i+1
        i+=1
    if len(twodballs) == 0:
        return True
    elif dif_key and chain >2:
        return True
    return False

main()