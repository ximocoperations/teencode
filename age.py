# This is a python program that compares user age

#Obtain user year of birth and store it in variable dateOfBirth

dateOfBirth=eval(input('Please enter year of Birth :'))
#initialize today's date
yearNow = 2019

#calculate user age 

user_Age=yearNow-dateOfBirth
print(user_Age)

#carryout the check

if(user_Age < 18):
    print('Your '+str(user_Age)+ " years old  and"+' a minor')
elif(user_Age > 18 and user_Age <36):
     print('Your '+str(user_Age)+ " years old  and"+' a youth')
else:
     print('Your '+str(user_Age)+ " years old  and"+' an elder')
    
