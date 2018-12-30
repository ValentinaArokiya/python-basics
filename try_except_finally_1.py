try:
    result = int(input("Please provide a number: "))

except:
    print("Whoops! That is not a number")

else:
    print("Thank you")

finally:
    print("End of try/except/finally")
    print("I will always run at the end")
    