# class RegistrationError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# class Grandfather:
#     def __init__(self, money):
#         self.money = money
#         print("You are about to recieve 5 million dollars from your Grandfather\n" + "Do you wish to Register? (Y/N)")
#         self.register()
    
#     def register(self):
#         ch = input()
#         if ch =="Y":
            
#             self.registered = True
#         else:
#             print("Think a bit more")
#             self.registered = False
#         # self.registered = True
    
#     def receive_inheritance(self):
#         if not self.registered:
#             raise RegistrationError("You must register to receive the inheritance.")
#         self.money += 5000000000  # 5 billion dollars
        
#     def display_inheritance(self):
#         print(f"Inherited {self.money} dollars from grandfather")


# class Father:
#     def __init__(self):
#         self.villa = True
#         self.registered = False
    
#     def register(self):
#         self.registered = True
    
#     def receive_inheritance(self):
#         if not self.registered:
#             raise RegistrationError("You must register to receive the inheritance.")
#         self.villa = True
        
#     def display_inheritance(self):
#         if self.villa:
#             print("Inherited a villa from father")
#         else:
#             print("No inheritance received from father")


# class Mother:
#     def __init__(self):
#         self.agriculture_land = 10  # Acres
#         self.registered = False
    
#     def register(self):
#         self.registered = True
    
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


# # Create an instance of Lucky and simulate registration and inheritance
# lucky = Lucky()
# lucky.receive_inheritance()

# # Display the inheritance details
# lucky.display_inheritance()

class RegistrationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Grandfather:
    def __init__(self, money):
        self.money = money
        self.registered = False
        print("You are about to recieve 5 million dollars from your Grandfather\n" + "Do you wish to Register? (Y/N)")
        self.register()
    
    def register(self):
        ch = input()
        if ch =="Y":
            return self.registered == True
        else:
            print("Think a bit more")
            return self.registered == False
        # self.registered = True
    
    def receive_inheritance(self):
        if self.registered==False:
            raise RegistrationError("You must register to receive the inheritance.")
        self.money += 5000000000  # 5 billion dollars
        
    def display_inheritance(self):
        print(f"Inherited {self.money} dollars from grandfather")


class Father:
    def __init__(self):
        self.villa = True
        self.registered = False
    
    def register(self):
        self.registered = True
    
    def receive_inheritance(self):
        if not self.registered:
            raise RegistrationError("You must register to receive the inheritance.")
        self.villa = True
        
    def display_inheritance(self):
        if self.villa:
            print("Inherited a villa from father")
        else:
            print("No inheritance received from father")


class Mother:
    def __init__(self):
        self.agriculture_land = 10  # Acres
        self.registered = False
    
    def register(self):
        self.registered = True
    
    def receive_inheritance(self):
        if not self.registered:
            raise RegistrationError("You must register to receive the inheritance.")
        self.agriculture_land += 10  # Additional 10 acres
        
    def display_inheritance(self):
        print(f"Inherited {self.agriculture_land} acres of agriculture land from mother")


class Lucky(Grandfather, Father, Mother): #multiple inheritance
    def __init__(self):
        Grandfather.__init__(self, 0)
        Father.__init__(self)
        Mother.__init__(self)
        
    def register(self):
        Grandfather.register(self)
        Father.register(self)
        Mother.register(self)
        
    def receive_inheritance(self):
        try:
            Grandfather.receive_inheritance(self)
            Father.receive_inheritance(self)
            Mother.receive_inheritance(self)
        except RegistrationError as e:
            print(f"Error: {e}")
        
    def display_inheritance(self):
        Grandfather.display_inheritance(self)
        Father.display_inheritance(self)
        Mother.display_inheritance(self)


# Create an instance of Lucky
lucky = Lucky()

# Register and receive inheritance
lucky.receive_inheritance()

# Display the inheritance details
lucky.display_inheritance()

