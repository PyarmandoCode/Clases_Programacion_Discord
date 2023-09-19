# for i in range(1,11):
#     if i % 2==0:
#         continue
#     print(i)


for i in range(1,11):
    if i % 3 ==0:
        print(f"{i} es divisible por 3")
        continue
    if i % 5 ==0:
        print(f"{i} es divisible por 5")
        continue
    print(i)
