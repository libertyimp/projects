import datetime
name = input("Please enter your name: ")
age = int (input("Please enter your age: "))

today = datetime.date.today()
thisYear = today.year

anwser = thisYear - age + 100

print("Hello,", name, "you will be 100 years old in the year:", anwser)



