# p_list = []
# for x in range(2,1000):
#     p=True
#     for y in range(2, x):
#         n= (x % y == 0)
#         if n==True:
#             print("{0}n'est pas un nombre premier car il est divisible par {1}".format(x, y))
#             p = False
#             break
#     if p == True:
#         p_list.append(x) 
# print(p_list)


p_list = []
for x in range(2,1000):

    p=True

    for y in range(2, x):
        # n= (x % y == 0)
        if x % y == 0:
            print("{0} n'est pas un nombre premier car il est divisible par: {1}".format(x, y))
            p = False
            break
       

    if p == True:
        p_list.append(x)
        
print(p_list)


















