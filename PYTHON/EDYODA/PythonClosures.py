#1 Closure basic exapmle
'''
def print_message(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


another = print_message("Hello")
another()

OUTPUT => Hello 

'''

#2 Closure Example

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3) # Multiplier of 3

times5 = make_multiplier_of(5) # Multiplier of 5

print(times3(9))
# Output: 27

print(times5(3))
# Output: 15

print(times5(times3(2)))
# Output: 30