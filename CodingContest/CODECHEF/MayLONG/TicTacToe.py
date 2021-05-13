t=int(input())
for i in range(t):
    cx=0
    co=0
    n=0
    l = []
    for i in range(3):
        tic=input()
        l.append(tic)

    for i in range(3):
        for j in range(3):
            if l[i][j]=='X':
                cx+=1
            elif l[i][j]=='O':
                co+=1
            else:
                n+=1
    wx=0
    wo=0

    #Horizontal line - xxx
    if l[0][0]=='X' and l[0][1]=='X' and l[0][2]=='X':
        wx=1
    if l[1][0]=='X' and l[1][1]=='X' and l[1][2]=='X':
        wx=1
    if l[2][0]=='X' and l[2][1]=='X'  and l[2][2]=='X':
        wx=1

    #vertical line
    # x
    # x
    # x
    if l[0][0]=='X' and l[1][0]=='X' and l[2][0]=='X':
        wx=1
    if l[0][1]=='X' and l[1][1]=='X' and l[2][1]=='X':
        wx=1
    if l[0][2]=='X' and l[1][2]=='X'  and l[2][2]=='X':
        wx=1

    #diagonals
    #    x
    #   x
    # x
    if l[0][0]=='X' and l[1][1]=='X' and l[2][2]=='X':
        wx=1
    if l[0][2]=='X' and l[1][1]=='X'  and l[2][0]=='X':
        wx=1


    if l[0][0]=='O' and l[0][1]=='O' and l[0][2]=='O':
        wo=1
    if l[1][0]=='O' and l[1][1]=='O' and l[1][2]=='O':
        wo=1
    if l[2][0]=='O' and l[2][1]=='O'  and l[2][2]=='O':
        wo=1
    if l[0][0]=='O' and l[1][0]=='O' and l[2][0]=='O':
        wo=1
    if l[0][1]=='O' and l[1][1]=='O' and l[2][1]=='O':
        wo=1
    if l[0][2]=='O' and l[1][2]=='O'  and l[2][2]=='O':
        wo=1
    if l[0][0]=='O' and l[1][1]=='O' and l[2][2]=='O':
        wo=1
    if l[0][2]=='O' and l[1][1]=='O'  and l[2][0]=='O':
        wo=1

    if (wx==1 and wo==1) or (cx-co<0) or (cx-co>1):
        print(3)
    elif (cx==0 and co==0 and n==9):
        print(2)
    elif (wx==1 and wo==0 and cx>co):
        print(1)
    elif (wx==0 and wo==1 and cx==co):
        print(1)
    elif (wx==0 and wo==0 and n==0):
        print(1)
    elif (wx==0 and wo==0 and n>0):
        print(2)
    else:
        print(3)