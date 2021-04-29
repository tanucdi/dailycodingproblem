#returns the price of the selected seat.
def TicektPrice(i,j,ts,r):
    if ts<=60:
        Price=10
    else:
        if r%2==0:
            if i<=r//2:
                Price=10
            else:
                Price=8
        else:
            if i<=r//2:
                Price=10
            else:
                Price=8
    return Price