def TicektPrice(i,j,ts):
    if ts<=60:
        Price=10
    else:
        if i%2==0:
            if i<=i//2:
                Price=10
            else:
                Price=8
        else:
            if i<=i//2:
                Price=10
            else:
                Price=8
    return Price