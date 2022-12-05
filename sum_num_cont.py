#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Created: Nov 8, 2022
# This program adds several numbers together using a 'continue' statement.
 
 
def main():
    loop_count = 0
    sum_num = 0
    # This is the input for how many numbers we adding and try catch.
    try:
        user_amount = int(input("How many numbers you wanna add?: "))
 
    except:
        print("Enter a whole number")
        print("Restarting...")
        return main()
 
    while True:
 
        if loop_count < user_amount:
            # Fixing all invalid inputs.
            try:
                user_num = int(input(f"What is the ({loop_count+1}) number?: "))
            except:
                print("Enter a whole number \n")
                print("Restarting...")
                return main()
            sum_num += user_num
            loop_count += 1
            # The continue statement! :D.
            continue
 
        if user_amount < 0:
            print("You must add 2 or more numbers.")
            print("Restarting...")
            return main()
 
            # This case is for when there is only 1 number.
        if user_amount == 1:
            print("You must add 2 or more numbers.\n")
            print("Restarting...")
            return main()
 
            # Output for the answer.
        if loop_count == user_amount:
            print(f"Your total sum of {loop_count} number(s) is '{sum_num}' \n")
            break
 
 
if __name__ == "__main__":
    main()