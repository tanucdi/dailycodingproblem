
class Employee:
    def __init__(self,employeeid,employeename,department,salary,role):
        self.employeeid=employeeid
        self.employeename=employeename
        self.department=department
        self.salary=salary
        self.role=role
    
    def calculateincentive(self,dic):
        incentive=None
        for i in dic:
            if self.role.lower() == i.lower():
                incentive=self.salary*(dic[i]/100)
        if incentive==None:
            return None
        else:
            return incentive


def calculateEmployeeSalaryByRole(role,list1,dict1):
    l=[]
    c=0
    for i in list1:
        if i.role == role:
            c=1
            newinc=i.calculateincentive(d)
            i.salary = i.salary + newinc
            l.append(i)
    if c==0:
        return None
    else:
        return l

# n=int(input())
# d={}
# for i in range(n):
#     x=input()
#     y=int(input())
#     d[x]=y
# l=[]
# n=int(input())
# for i in range(n):
#     obj=Employee(int(input()),input(),input(),int(input()),input())
#     l.append(obj)
strrole = input()
# print(l)
d={'Manager':20,'dm':10,'la':10}
obj1 = Employee(101,'ashok','TD',20000,'Manager')
obj2 = Employee(102,'rajesh','HR',30000,'Manager')
obj3 = Employee(103,'rajesh','HR',40000,'dm')
obj4 = Employee(104,'rajesh','HR',50000,'la')
l=[obj1,obj2,obj3,obj4]

a1=l[0].calculateincentive(d)
if a1==None:
    print('Employee Not Found')
else:
    print(a1)

f1=calculateEmployeeSalaryByRole(strrole,l,d)

if f1==[] or f1==None:
    print('Employee Not Found.')
else:
    for i in f1:
        print(i.employeeid,i.employeename,i.salary)