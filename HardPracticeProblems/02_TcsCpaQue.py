class Property:
    def __init__(self,property_type,property_value,max_bid_price):
        self.property_type = property_type
        self.property_value = property_value
        self.max_bid_price = max_bid_price

class Tender:
    def __init__(self,buyerName,propertyType,bidPrice):
        self.buyerName = buyerName
        self.propertyType = propertyType
        self.bidPrice = bidPrice
      

def bidProperty(property,tender):
    buyers = []
    for p in property:
        tn = ''
        h = 0
        for t in tender:
            if(p.property_type.lower() == t.propertyType.lower() and t.bidPrice > h and (t.bidPrice>=p.property_value and t.bidPrice<=p.max_bid_price)):
                tn = t.buyerName
                h = t.bidPrice
        if(tn!=''):
            buyers.append(tn)
            propertySold.append(p.property_type)
    if(len(buyers)):
        return buyers
    return None

propertySold = []      
propertyList = []
tenderList = []

np = int(input())

for i in range(np):
    pt = input()
    pv = int(input())
    mbp = int(input())
    propertyList.append(Property(pt,pv,mbp))
    
nt = int(input())

for i in range(nt):
    bn = input()
    pt = input()
    bp = int(input())
    tenderList.append(Tender(bn,pt,bp))
    
pl = bidProperty(propertyList,tenderList)
if(pl == None):
    print("Property not found")
else:
    for p in pl:
        print(p)
for p in propertyList:
    if(p.property_type not in propertySold):
        print(p.property_type)