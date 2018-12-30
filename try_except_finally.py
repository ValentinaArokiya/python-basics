try:
    result = 10 + '10'

except TypeError:
    print("It looks like you aren't adding correctly")

except:
    print("All other exceptions")

else:
    print("Add went well")

finally:
    print("THE END")


