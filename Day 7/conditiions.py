def main():  #def to definde the valirable dei
    x, y = 355, 55

    if x > y:
        print("x is greater than y")
    
    else:
        print("y is greater than x")

main()  #call the function to run it.



#elif case

x = 150

if x > 100:
    print("x is greater than 100")
elif x > 50:
    print("x is greater than 50 but less than or equal to 100")
elif x == 50:
    print("x is exactly 50")
else:
    print("x is less than 50") 


#onemore example

#marks = 100
#input from user

marks = float(input("Enter your marks: "))

if marks > 100:
    print("Grade: A+")

elif marks > 90:
    print("Grade: A")

elif marks > 70:
    print("Grade: B")

elif marks > 50:
    print("Grade: C")

elif marks > 40:
    print("Grade: D")

else:
    print("Grade: E")