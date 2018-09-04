print("Enter your year of birth")
dob = input()


dob = float(dob)

# function to get current year
currentyear = 2018

age = currentyear - dob

# print
if(age < 18):
    print("You are a minor")

elif(age >=18 and age <=36):
    print("You are a youth")

else:
    print("You are an elder")


