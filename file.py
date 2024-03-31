import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file :
    for i in range(100): 
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.choice(range (40,100))
        height = random.choice(range (150,200))


        file.write("{},{},{}\n".format(name,weight,height))

    
with open("info.txt","r") as file2 :
    for line in file2:
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height)/100)**2)

        result = ""

        if bmi>=25 :
            result = "과체중"
        elif bmi>=18.5:
            result = "정상체중"
        else:
            result = "정상"

        print('\n'.join([
            "이름:{}",
            "몸무게:{}",
            "키:{}",
            "BMI:{}",
            "결과:{}"
            ]).format(name,weight,height,bmi,result))
        print()
        