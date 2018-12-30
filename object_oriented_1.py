###
###
# create own objects with own attributes and own methods"""""
#  class names have reserved upper case letters
# list, string, dictionaries are built-in objects and we use the python built-in methods on the objects.
# Like..... list_a.append() , tuple_a.index(). Syntax: object.method_name()

# In OOP, we create our own objects with own attributes and methods.

# class NameOfClass:
#    def__init__(self, param1, param2):
#        self.param1 = param1
#        self.param2 = param2
#
#    def some_method(self):
#        print(self.param1)

## Self - keyword:
## the self keyword indicates that the attributes and methods are connected only to the instances of this class.
## It is not a global attribute or method.

## the parameter name will be entered 3 times in the init method.


### the init method will be called each time an instance is created. All steps inside the init method will be executed, when the instance is created.
# The 'self' keyword connects the init method to the instance of the class.

# CLASS OBJECT ATTRIBUTE
# SAME FOR ANY INSTANCE OF A CLASS. HENCE WE DO NOT USE THE 'SELF' KEYWORD.
# defined before the INIT method.

# METHODS:
# METHODS ARE FUNCTIONS DEFINED INSIDE THE BODY OF THE CLASS.
# USED TO PERFORM OPERATIONS THAT SOMETIMES UTILIZES THE ATTRIBUTES DEFINED IN THE INIT METHOD