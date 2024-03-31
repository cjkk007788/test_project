dictionary = {

    "1번" : "1234",
    "2번" : "5678",
    "3번" : 1234,
}


dictionary["4번"] = "1234"

print(dictionary)

del dictionary["4번"]


print(dictionary)


for i,value in dictionary.items():
    print("키의 값 : {} 그리고 데이터{}".format(i,value))



