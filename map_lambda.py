power = lambda x : x*x
filter = lambda x: x<3

a =[1,2,3,4,5] 

new_list = list(map(power,a))
for i in range(5):
    print(new_list[i])
