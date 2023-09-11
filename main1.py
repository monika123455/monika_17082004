n=int(input("enter a year"))
if(n%400==0):
  print("leapyear")
elif(n%100==0):
  print("not leapyear")
elif(n%4==0):
  print("leapyear")
else:
  print("not aleap year")