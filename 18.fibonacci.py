import time
import turtle

c = turtle.Turtle()

# def fib (n):
    
#     if n==0 :
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)






def f(n):
    a=0
    b = 1
    for i in range(1, n):
        
        c=a+b
        a=b
        b=c
        
    return c


# x = int(input("entrez une valeaur"))
# fib_list = []

# for i in range (10):
#     fib_list.append(f(i))
#     print(f(i))

# print(fib_list)

def draw_square(t):
    for i in range(4):
        c.forward(t)
        c.left(90)



x = f(10)
for t in x:
    draw_square(t)






# t0= time.time()
# print(f(30))
# t1=time.time()
# print("time : {0}".format(t1-t0))



turtle.done()
