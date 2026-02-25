age =int( input("enter your age:"))
#own_car = 'false'
own_car = input("Do you own a car? (true/false): ")

if (age>=18):
    if (own_car == 'true'):
        print("you can drive car")
    else:
        print("work hard for the car now")

else:
    print("your still young to drive a car")