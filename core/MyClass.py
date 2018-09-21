class MyClass:
    variable = "blah"

    def __init__(self, config_name="default"):
        if config_name == "default":
            self.config_name = self.__class__.__name__
        else:
            self.config_name = config_name

    def function(self):
        print("This is a message inside the class." + self.config_name)

# myobjectx = MyClass()
# print(myobjectx.variable)
