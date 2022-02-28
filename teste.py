n = 9
def calcula(num):
    if num < 2:
        return num
    else:
        return calcula(num - 1) + calcula(num - 2)

print(calcula(n))        