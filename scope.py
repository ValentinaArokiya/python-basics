# variable names are stored in namespace
# variable names have a scope
# LEGB
# L: Local - assigned within a function. def
# E: Enclosing - Enclosing functions from inner to outer.
# G: Global - assigned at the top level of a module file. Or declared global.
# B: Built-in - Built-in modules


# GLOBAL
name = "This is a global string"

def greet():
    # ENCLOSING
    name = "Sammy"

    def hello():
        # LOCAL
        name = "Im Local"
        print("Hello " + name)

    hello()

greet()

# The outer most function call (greet()) gets executed first. greet() internally calls the hello()

