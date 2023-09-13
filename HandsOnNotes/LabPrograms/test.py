# class RegistrationError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# class Grandfather:
#     def __init__(self, money):
#         self.money = money
#         # self.registered = False
    
#     def register(self):
#         ch1 = input("Do you wish to register the cash recieving from your Grandfather? (Y/N): ")
#         if ch1.upper() == "Y":
#             self.registered = True
#         else:
#             self.registered = False
    
#     def receive_inheritance(self):
#         if not self.registered:
#             raise RegistrationError("You must register to receive the inheritance.")
#         self.money += 5000000000  # 5 billion dollars
        
#     def display_inheritance(self):
#         print(f"Inherited {self.money} dollars from grandfather")


# class Father:
#     def __init__(self):
#         pass
#         self.villa = False
#         # self.registered = False
    
#     def register(self):
#         ch2 = input("Do you wish to register the inheriting Villa? (Y/N): ")
#         if ch2.upper() == "Y":
#             self.registered = True
#         else:
#             self.registered = False
    
#     def receive_inheritance(self):
#         if not self.registered:
#             raise RegistrationError("You must register to receive the inheritance.")
#             self.villa = False
#         self.villa = True
        
#     def display_inheritance(self):
#         if self.villa:
#             print("Inherited a villa from father")
#         else:
#             print("No inheritance received from father")


# class Mother:
#     def __init__(self):
#         self.agriculture_land = 0  # Acres
#         self.registered = False
    
#     def register(self):
#         ch3 = input("Do you wish to register the land recieving from your mother? (Y/N): ")
#         if ch3.upper() == "Y":
#             self.registered = True
#         else:
#             self.registered = False
    
#     def receive_inheritance(self):
#         if not self.registered:
#             raise RegistrationError("You must register to receive the inheritance.")
#         self.agriculture_land += 10  # Additional 10 acres
        
#     def display_inheritance(self):
#         print(f"Inherited {self.agriculture_land} acres of agriculture land from mother")


# class Lucky(Grandfather, Father, Mother):
#     def __init__(self):
#         Grandfather.__init__(self, 0)
#         Father.__init__(self)
#         Mother.__init__(self)
        
#     def register(self):
#         Grandfather.register(self)
#         Father.register(self)
#         Mother.register(self)
        
#     def receive_inheritance(self):
#         try:
#             Grandfather.receive_inheritance(self)
#             Father.receive_inheritance(self)
#             Mother.receive_inheritance(self)
#         except RegistrationError as e:
#             print(f"Error: {e}")
        
#     def display_inheritance(self):
#         Grandfather.display_inheritance(self)
#         Father.display_inheritance(self)
#         Mother.display_inheritance(self)


# # Create an instance of Lucky
# lucky = Lucky()

# # Register and receive inheritance
# lucky.register()
# lucky.receive_inheritance()

# # Display the inheritance details
# lucky.display_inheritance()

class RegistrationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class FamilyMember:
    def __init__(self, inheritance_type):
        self.registered = self.register(inheritance_type)
    
    def register(self, inheritance_type):
        ch = input(f"Do you wish to register for inheritance from {inheritance_type}? (Y/N): ").upper()
        return ch == "Y"


class Grandfather(FamilyMember):
    def __init__(self):
        super().__init__("Grandfather")
        self.money = 0
    
    def receive_inheritance(self):
        if not self.registered:
            raise RegistrationError("You must register to receive the inheritance.")
        self.money += 5000000000  # 5 billion dollars
        
    def display_inheritance(self):
        print(f"Inherited {self.money} dollars from grandfather")


class Father(FamilyMember):
    def __init__(self):
        super().__init__("Father")
        self.villa = False
    
    def receive_inheritance(self):
        if not self.registered:
            raise RegistrationError("You must register to receive the inheritance.")
        self.villa = True
        
    def display_inheritance(self):
        if self.villa:
            print("Inherited a villa from father")
        else:
            print("No inheritance received from father")


class Mother(FamilyMember):
    def __init__(self):
        super().__init__("Mother")
        self.agriculture_land = 0  # Acres
    
    def receive_inheritance(self):
        if not self.registered:
            raise RegistrationError("You must register to receive the inheritance.")
        self.agriculture_land += 10  # Additional 10 acres
        
    def display_inheritance(self):
        print(f"Inherited {self.agriculture_land} acres of agriculture land from mother")


class Lucky(Grandfather, Father, Mother):
    def __init__(self):
        Grandfather.__init__(self)
        Father.__init__(self)
        Mother.__init__(self)
        
    def receive_inheritance(self):
        try:
            super().receive_inheritance()  # Call receive_inheritance using MRO
        except RegistrationError as e:
            print(f"Error: {e}")
        
    def display_inheritance(self):
        super().display_inheritance()  # Call display_inheritance using MRO


# Create an instance of Lucky
lucky = Lucky()

# Register and receive inheritance
lucky.receive_inheritance()

# Display the inheritance details
lucky.display_inheritance()
