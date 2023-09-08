#python program to check if year is a leap year of not

year=2000
#To get (integer input)from the user
#year=int(input("Enter a year:"))

#divided by100means century year (ending with 00)
#century year divided by400 is leap year
if(year %400==0)and (year %100==0):
  print ("{0}is a leap year".format (year))

#not divided by 4 is a leap year
elif(years %4==0)and(year %100!=0):
  print ("{0}is a leap year".format (year))

#if not divided by both 400(century year)and 4(not century year)
#year is not leap year
else:
  print("{0} is not leap year ".format (year))

