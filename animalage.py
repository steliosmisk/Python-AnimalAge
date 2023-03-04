print("-- WELCOME TO ANIMAL AGE CALCULATOR --")
print("[1] Cat to Human Age")
print("[2] Dog to Human Age")
print("[3] Exit")

user_choice = int(input("Enter (1/2/3): "))

while user_choice in {1, 2}:
    try:
        if user_choice == 1:
            cat_age = int(input("Enter the cat's age: "))
            if cat_age == 1:
                human_age = 15
            elif cat_age == 2:
                human_age = 25
            else:
                human_age = 25 + (cat_age - 2) * 4
            print("Your cat's age is equivalent to", human_age, "human years!")
        else:
            dog_age = int(input("Enter the dog's age: "))
            if dog_age in {1, 2}:
                human_age = dog_age * 11
            else:
                human_age = 22 + (dog_age - 2) * 4
            print("Your dog's age is equivalent to", human_age, "human years!")
        break
    except ValueError:
        print("Please enter a valid age.")
