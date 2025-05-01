class Device:
    """Base class for electronic devices"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False
    
    def power_on(self):
        """Turn the device on"""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")
            
    def power_off(self):
        """Turn the device off"""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")


class Smartphone(Device):
    """Smartphone class that inherits from Device"""
    
    def __init__(self, brand, model, screen_size, storage):
        # Call the parent class constructor
        super().__init__(brand, model)
        
        # Smartphone specific attributes
        self.screen_size = screen_size  # in inches
        self.storage = storage  # in GB
        self.apps = []
        self.battery = 100  # battery percentage
    
    def make_call(self, number):
        """Make a phone call to a number"""
        if self.is_on:
            print(f"Calling {number} from {self.brand} {self.model}...")
            self.battery -= 5
        else:
            print("Phone is off. Turn it on first.")
    
    def install_app(self, app_name):
        """Install a new app on the smartphone"""
        if self.is_on:
            self.apps.append(app_name)
            print(f"{app_name} has been installed on {self.brand} {self.model}.")
            self.battery -= 2
        else:
            print("Phone is off. Turn it on first.")
    
    def check_battery(self):
        """Check the current battery level"""
        print(f"Battery level: {self.battery}%")
    
    def charge(self, minutes):
        """Charge the smartphone battery"""
        charge_amount = minutes // 2  # 2 minutes = 1% battery
        self.battery = min(100, self.battery + charge_amount)
        print(f"Battery charged to {self.battery}%")


# Create smartphone objects
iphone = Smartphone("Apple", "iPhone 13", 6.1, 128)
galaxy = Smartphone("Samsung", "Galaxy S22", 6.8, 256)

# Use the smartphones
print(f"Created a {iphone.brand} {iphone.model} with {iphone.storage}GB storage")
print(f"Created a {galaxy.brand} {galaxy.model} with {galaxy.storage}GB storage")

iphone.power_on()
iphone.install_app("Instagram")
iphone.install_app("TikTok")
iphone.make_call("555-1234")
iphone.check_battery()

galaxy.power_on()
galaxy.install_app("YouTube")
galaxy.charge(30)  # Charge for 30 minutes
galaxy.check_battery()
galaxy.power_off()
