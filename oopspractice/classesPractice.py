class Phone:
    #class variable
    phone_version = "S10"
    brand_name = "Samsung"
    user_name = ""

    #right now I can change this by calling it bellow
    # but there is way we can stop this 
    # model = "S10+"
    #custom getter and setter always
    def get_model(self):
        # return self.model
        return "S10+"
    
    # def set_model(self,val):
    #     self.model = "S10+, "+ val 

    #Constructor
    def __init__(self,user_name):
        self.user_name = user_name

    #class method
    def BootLogo(self):
        print("SAMSUNG",self.phone_version)



Dhananjay = Phone("Dhananjay's Phone")
# Dhananjay.phone_version = "Iphone 11 pro Max"
Dhananjay.set_model("iphone")
print(Dhananjay.get_model())

# Dhananjay.BootLogo()

#getter and setter