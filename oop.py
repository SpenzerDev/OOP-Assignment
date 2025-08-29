class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now on!"
    
    def power_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now off!"
    
    def check_storage(self):
        return f"Storage: {self.storage}GB"
    
    def check_battery(self):
        return f"Battery: {self.battery}mAh"
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}mAh)"


# GamingPhone inherits from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu
    
    def game_mode(self):
        return f"Game mode activated with {self.gpu} GPU!"
    
    # Override the __str__ method
    def __str__(self):
        return f"{self.brand} {self.model} Gaming Phone ({self.storage}GB, {self.battery}mAh, {self.gpu})"


# Demo
if __name__ == "__main__":
    # Create regular smartphone
    phone1 = Smartphone("Apple", "iPhone 14", 128, 3200)
    print(phone1)
    print(phone1.power_on())
    print(phone1.check_battery())
    print()
    
    # Create gaming phone
    phone2 = GamingPhone("ASUS", "ROG Phone", 256, 6000, "Adreno 660")
    print(phone2)
    print(phone2.power_on())
    print(phone2.game_mode())
    print(phone2.check_storage())