x = int(input("Please enter age: "))
if x <=0:
    print("Invalid")
elif x <12:
    print("Infant")
elif x <18:
    print("Child")
elif x <20:
    print("teen")
elif x<45:
    print("Adult")
else: print("Old")