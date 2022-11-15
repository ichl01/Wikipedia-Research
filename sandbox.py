import random
lst = []
def createList(n):
    for i in range(n+1):
        lst.append(i)
    return(lst)
createList(268)
print(random.sample(lst, 5))