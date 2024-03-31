list_a = [1,2,3,4,5,6]

min_l = min(list_a)


print(min_l)

list_reversed = reversed(list_a)

print("list_reversed:",list(list_reversed))

for i, value in enumerate(list_a):
    print("{}번째의 값{}".format(i,value))




