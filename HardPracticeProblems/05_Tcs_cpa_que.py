class Volcano:
    def __init__(self,vname,vcountry,vele,varea,vyear):
        self.vname=vname
        self.vcountry=vcountry
        self.vele=vele
        self.varea=varea
        self.vyear=vyear

class Eruption:
    def __init__(self,vlist):
        self.vlist=vlist

    def findvc(self,country):
        li=[]
        for i in self.vlist:
            if i.vcountry.lower()==country.lower():
                li.append(i)
        if li==[]:
            return None
        else:
            return li

    def getvcat(self,name):
        stat=''
        for i in self.vlist:
            if i.vname.lower()==name.lower():
                if 2021-i.vyear<25 and 2021-i.vyear>1:
                    stat='High probability'
                if 2021-i.vyear<50 and 2021-i.vyear>25:
                    stat='Low probability'
                if i.vyear==2021:
                    stat='Active'
                else:
                    stat='unactive'
        if stat=='':
            return None
        else:
            return stat

testcase = int(input())
vli=[]
for i in range(testcase):
    name = input()
    country = input()
    elevation=int(input())
    area=int(input())
    Erup = int(input())
    vli.append(Volcano(name,country,elevation,area,Erup))
vc=input()
vn=input()

a=Eruption(vli)
Z=a.findvc(vc)
X=a.getvcat(vn)

if Z!= None:
    for i in Z:
        print(i.vname)
        print(i.vcountry)
        print(i.vyear)
else:
    print('No Matching records found.')

if X!= None:
    print(X)
else:
    print('No Volcano is available with the given name')

                
