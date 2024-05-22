## First create message for new user welcoming them to program
print ("Hello and Welcome to the Tip Calculator! Please input the complete bill and I will generate the tip.")

## Have user input the total amount for the bill
bill = float(input("Total bill amount: $"))

## Ask how much tip you would like to leave
tip_amount = float(input("How much of a tip would you like to leave? .10, .15, or .20?  "))

## Generate the tip based on tip_amount
tip = float(bill * tip_amount)

## Ask if they want to split the bill
split_bill = input("Did you want to split the bill? ")
if split_bill == "yes":
    split_yes = (int(input("How many ways do you want to split? ")))
    split_tip = float(bill * tip_amount / split_yes)
    print("Each person should tip ${:0.2f}".format(split_tip))
elif split_bill == "no":
    print("Your tip will be ${:0.2f}.".format(tip))