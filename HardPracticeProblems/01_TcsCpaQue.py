# #THIS QUESTION IS ASKED IN TCS CPA EXAM.
# #WE HAVE GIVEN INCENTIVES DEPENDS ON ROLE AND LAST INPUT IS A ROLE ON WHICH
# WE HAVE TO CALCULATE THE INCENTIVE THEN ADD THEM TO SALARY AND RETURN THE ID,NAME,NEW SALARY

class Employee:
    def __init__(self,employeeid,employeename,department,salary,role):
        self.employeeid=employeeid
        self.employeename=employeename
        self.department=department
        self.salary=salary
        self.role=role
    
    def calculateincentive(self,dict):
        for i in dict:
            if self.role == i:
                incentivepercentage=dict[i] 
                incentive=self.salary*(incentivepercentage/100)
                return incentive
        else:
            return None

# n=int(input())
d={}
# for i in range(n):
#     x=input()
#     y=int(input())
#     d[x]=y
l=[]
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

def calculateEmployeeSalaryByRole(role,list1,dict1):
    for i in list1:
        if i.role == role:
            newinc=Employee.calculateincentive(i,d)z
            newsalary = i.salary + newinc
            print(i.employeeid,i.employeename,newsalary)

calculateEmployeeSalaryByRole(strrole,l,d)
