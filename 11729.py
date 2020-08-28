def move(init, final, plate):
    if plate == 1:
        print(init,final)
    else:
        move(init, 6-init-final, plate-1)
        print(init,final)
        move(6-init-final,final,plate-1)

n = int(input())
print(2**n-1)
move(1,3,n)