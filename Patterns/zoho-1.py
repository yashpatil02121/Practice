# for n=4

#         1 2 3 4
#       8 7 6 5
#     9 10 11 12
#   16 15 14 13 

n = 4
x = 1
ascending = True
for i in range(n):
    print(" "*(n-i)*2,end="")
    if ascending:
        for j in range(n):
            print(x," ",end="")
            x+=1
            ascending = False
    else:
        x+=n-1
        for j in range(n):
            print(x," ",end="")
            x-=1
            ascending = True
        x+=n+1
    print("")