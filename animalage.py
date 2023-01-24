print("--WELCOME TO ANIMAL AGE CALCULATOR--")
print("[1] Cat to Human Age")
print("[2] Dog to Human Age")
print("[3] Exit")

user_choice = int(input("Enter (1/2/3): "))
while user_choice in {1, 2} and user_choice != 3:
    try:
        total_age = 0
        if user_choice == 1:
            cat_age = int(input("Enter the cat's age: "))
            if cat_age == 1:
                total_age = 15
            elif cat_age == 2:
                total_age = 25
            else:
                total_age = 25 + (cat_age - 2) * 4
        else:
            dog_age = int(input("Enter the dog's age: "))
            total_age = dog_age * 11 if dog_age in {1, 2} else 22 + (dog_age - 2) * 4
        print("Your pet's age is:", total_age, "human years!")
        break
    except ValueError:
        print("Please enter a valid age.") 

