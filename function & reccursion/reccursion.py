def fac(num):
    if num == 1 or num == 0:
        return 1
    return num * fac(num-1)

num = int(input("Enter the num : "))

print(fac(num))