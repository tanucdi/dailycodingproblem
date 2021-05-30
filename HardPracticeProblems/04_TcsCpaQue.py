# # 5
# # Intel
# # Semiconductor company
# # 5
# # Mobileye
# # Movidius
# # Sigopt
# # WindRiver 
# # Intel Ireland
# # Financial Event Sponsor
# # Atos
# # IT Company
# # 3
# # Atos Syntel
# # Groupe Bull
# # EcoAct
# # Digital Sponsor
# # Sony Corporation
# # Multinational Conglomerate Company
# # 4
# # Sony pictures
# # Sony entertainment Network
# # Sony India
# # Sony europe
# # Media Event Sponsor
# # Microsoft Corporation
# # Technology Company
# # 3
# # Github
# # Linkedin
# # Yamoner
# # Promotial Partner
# # Activision
# # Video game Company
# # 4
# # Treyarch
# # infinity ward
# # Raven Software
# # Toys for bob
# # Digital Sponsor
# # Digital Sponsor

# class Sponsor:
#     def __init__(self,sponsorname,sponsorco,subsidiaries,sponsorcategory):
#         self.sponsorname=sponsorname
#         self.sponsorco=sponsorco
#         self.subsidiaries=subsidiaries
#         self.sponsorcategory=sponsorcategory

# def getSponsor(spobjl,spc):
#     l=[]
#     for i in spobjl:
#         if i.sponsorcategory.lower()==spc.lower():
#             l.append(i.sponsorname)
#     l.sort()
#     if l==[]:
#         return None
#     else:
#         return l

# def FindMaxSub(spobjl):
#     max=0
#     for i in spobjl:
#         if len(i.subsidiaries) > max:
#             s=i.sponsorname
#             max=len(i.subsidiaries)
#     return s

# testcase = int(input())
# slist=[]
# for i in range(testcase):
#     sname = input()
#     sco = input()
#     t=int(input())
#     l=[]
#     for i in range(t):
#         subs = input()
#         l.append(subs)
#     scat = input()
#     slist.append(Sponsor(sname,sco,l,scat))
# spocat=input()
# a=getSponsor(slist,spocat)
# b=FindMaxSub(slist)
# if a!= None:
#     for i in a:
#         print(i)
# else:
#     print('No matching record found.')
# print(b)