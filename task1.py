#function to find category

def find_category(bmi):
    if(bmi<18.5):
        cate='underweight'
    elif(bmi>18.5 and bmi<24.9):
        cate='healthy'
    else:
        cate='overweight'
    return cate

#function to calculate bmi

def calc_bmi(weight,height):
    bmi_found=weight/((height)**2)
    return bmi_found

name=input("Enter your name : ")
weight=float(input("Enter your weight(in kilograms) : "))
height=float(input("Enter your height(in Metres) : "))

#call to bmi function 

bmi=round(calc_bmi(weight,height),2)
category=find_category(bmi)

print("Calculating BMI ...")
print('\033[1m'+name+'\033[0m'+", your BMI is "+'\033[1m'+str(bmi)+'\033[0m')
print("And your category is "+'\033[1m'+'\033[96m'+category+'\033[96m'+'\033[0m')