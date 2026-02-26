while True:  #this is an infinite loop because the condition is always true
    number = int(input("enter the number: "))

    while number < 11100:  #here if the number is less then 10 then only it will go to the loop
        number -= 1  #this is the same as number = number - 1
        if number == 0:     #this is where the number is 1 then it will stop the loop and break out of it
         break  #beak for the rule
         #continue   #executes the next iteration of the loop, skipping any code below it in the current iteration        
        print(number)

    print("Loop ended")