# keep asking for user input until the correct input is provided - using While loop:

while True:
    try:
        result = int(input("Please provide a number: "))

    except:
        print("Whoops! That is not a number")
        continue
    else:
        print("Thank you")
        break

    finally:
        print("End of try/except/finally")
        print("I will always run at the end")
