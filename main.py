# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#LEAP YEAR rules: on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

if year%4!=0:
  print("Not leap year.")
else:
  if year%100==0:
    if year%400!=0:
      print("Not leap year.")
    elif year%400==0:
      print("Leap year.")
  elif year%100!=0:
    print("Leap year.")



