def upstar(star):
    newstar = list()
    for i in range(3*len(star)):
        if i//len(star) == 1:
            newstar.append(star[i%len(star)]+' '*len(star)+star[i%len(star)])
        else:
            newstar.append(star[i%len(star)]*3)
    return newstar
    
star = ['***','* *','***']
n = int(input())
while n>3:
    n = n//3
    star = upstar(star)

for i in star:
    print(i)
