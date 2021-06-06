''' DOUBLE UNDERSCORE METHODS i.e  DUNDER METHODS
it is used for-
-> operator overloading - YOU WANT TO USE THE OPERATOR (FOR EG. +) FOR YOUR CUSTOM USED DEFINED CLASS.
-> for making the code syntax genric across all the objects

how dunder methods are called-

__init__ = when object is created

def __add__(self,other) = when we use obj1 + obj 2, it gets called and obj2 passed as an second argument(other).

__sub__ = when we use obj1 - obj2

__mul__ = when we use obj1 * obj2

__str__ =  when we use print it gets called  '''