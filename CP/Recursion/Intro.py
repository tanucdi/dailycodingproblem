#RECURSION
#THERE IS ALWAYS A BASE CASE FOR RECURSION WHICH WILL TERMINATE THE RECURSION

def call(n):
    if n==5:
        return 
    call(n+1)
    print(n)

call(1)


''' 
output - 
4
3
2
1
'''

''' 
AFTER FUNCTIONN GETS RETURN 
IT RETURN BACK LIKE CALL(4) -> CALL(3) -> CALL(2) -> CALL(1) -> EXIT
so call(4) prints 4
call(3) print(3)
and so on.
'''