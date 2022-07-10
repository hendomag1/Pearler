# >_<
import time
# Savings calculator
def main():
    print("Holiday Savings Calulator 1.0")
    print("By Ryan and Hendo\n")

    mode = input("Enter 'a' for advanced or 's' for simple: ")
    if mode == "a":
        advanced()
        landing()
    elif mode == "s":
        simple()
        landing()
    else:
        print("Invalid mode")
        main()

def advanced():
    place = input("Where are you planning to go? ")
    goal = int(input("How much do the tickets cost? ($) "))
    rate = float(input("What is the interest rate? (%) ")) 
    months = int(input("How many months until the thing? "))

    rate = rate/1200

    amountToSave = ((rate)/((1 + (rate))**(months) - 1))*(goal - (1 + rate)**(months))
    
    amountFormatted = "{:.2f}".format(amountToSave)

    print("To afford the trip to " + place + " in " + str(months) + " months, you will need to save $" + str(amountFormatted) + " per month.")
    
    time.sleep(2)
def simple():
    place = input("Where are you planning to go? ")
    goal = int(input("How much do the tickets cost? ($) "))

    rate = 1.5/1200

    months3 = 3
    months6 = 6
    months12 = 12
    months24 = 24

    amountToSave3 = ((rate)/((1 + (rate))**(months3) - 1))*(goal - (1 + rate)**(months3))
    amountToSave6 = ((rate)/((1 + (rate))**(months6) - 1))*(goal - (1 + rate)**(months6))
    amountToSave12 = ((rate)/((1 + (rate))**(months12) - 1))*(goal - (1 + rate)**(months12))
    amountToSave24 = ((rate)/((1 + (rate))**(months24) - 1))*(goal - (1 + rate)**(months24))

    
    amountFormatted3 = "{:.2f}".format(amountToSave3)
    amountFormatted6 = "{:.2f}".format(amountToSave6)
    amountFormatted12 = "{:.2f}".format(amountToSave12)
    amountFormatted24 = "{:.2f}".format(amountToSave24)

    print("Your Saving Options:")
    print("If you save $" + str(amountFormatted3) + " per month for 3 months, you will be able to travel to " + place + " in 3 months.")
    print("If you save $" + str(amountFormatted6) + " per month for 6 months, you will be able to travel to " + place + " in 6 months.")
    print("If you save $" + str(amountFormatted12) + " per month for 12 months, you will be able to travel to " + place + " in 12 months.")
    print("If you save $" + str(amountFormatted24) + " per month for 24 months, you will be able to travel to " + place + " in 24 months.")
    
    time.sleep(2)
def landing():
    choice = input("Would you like to use the calculator again? (y/n): ")
    if choice == "y":
        main()
    elif choice == "n":
        print("Goodbye!")
    else:
        print("wrong input donut")
        landing()
main()