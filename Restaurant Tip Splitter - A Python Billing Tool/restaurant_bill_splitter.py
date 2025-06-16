print("Welcome to the Restaurant Tip Splitter!")
print("---------------------------------------")
print("Hi there! I'm Tip, your friendly assistant for splitting bills and calculating tips with ease :) \nPlease enter the required information to split your bill, and let’s make dining out a breeze!")
print("---------------------------------------")

try:
    total_bill = float(input("Please enter the total bill amount, which is the cost of the meal before the tip is added : "))
    if total_bill < 0:
        raise ValueError("Total bill cannot be negative.")
    
except ValueError as e:
    print(e if str(e) else "Invalid input. Please enter a numeric value.")
    exit(1)
    
try:
    tip_percentage = float(input("Please enter the tip percentage you would like to apply : "))
    if tip_percentage < 0:
        raise ValueError("Tip percentage cannot be negative.")
    
    
except ValueError as e:
    print(e if str(e) else "Invalid input. Please enter a numeric value.")
    exit(1)
    
try:
    people_count = int(input("How many individuals will be sharing the bill? : "))
    if people_count <=0:
        raise ValueError("Number of people cannot be zero or negative.")
    
except ValueError as e:
    print(e if str(e) else "Invalid input. Please enter a positive whole number.")
    exit(1)

def tip():
    tip_amount = total_bill * (tip_percentage / 100)
    return round(tip_amount,2)

def total_bill_after_adding_tip():
    total_bill_with_tip = total_bill + tip()
    return round(total_bill_with_tip,2)

def split_bill():
    amount_per_person = total_bill_after_adding_tip() / people_count
    return round(amount_per_person,2)
    
def checkout():
        print(f"======== \nRestaurant Tip Splitter \n======== \nTotal Bill: ${total_bill:.2f} \nTip Percentage: {tip_percentage:.2f}% \nTip Amount: ${tip():.2f} \nTotal Amount with Tip: ${total_bill_after_adding_tip():.2f} \nNumber of People: {people_count:.2f} \nAmount per Person: ${split_bill():.2f} \n========")

checkout()