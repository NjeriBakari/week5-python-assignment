#!/usr/bin/env python3
"""
Assignment 1: Design Your Own Class! 🏗️
=====================================
This program demonstrates:
1. Custom class creation (Smartphone)
2. Attributes and methods
3. Constructor usage
4. Inheritance with Electronics base class
5. Encapsulation and polymorphism concepts
"""

from datetime import datetime
import random

# Base class demonstrating inheritance
class Electronics:
    """Base class for all electronic devices"""
    
    # Class variable (shared by all instances)
    total_devices = 0
    
    def __init__(self, brand, model, price, warranty_years=1):
        """Initialize electronic device"""
        # Public attributes
        self.brand = brand
        self.model = model
        self.price = price
        self.warranty_years = warranty_years
        
        # Protected attributes (indicated by single underscore)
        self._serial_number = self._generate_serial()
        self._manufacture_date = datetime.now().strftime("%Y-%m-%d")
        
        # Private attributes (indicated by double underscore)
        self.__is_on = False
        self.__power_consumption = 0
        
        # Increment class variable
        Electronics.total_devices += 1
        
        print(f"📱 New {self.__class__.__name__} created: {brand} {model}")
    
    def _generate_serial(self):
        """Protected method to generate serial number"""
        return f"SN{random.randint(100000, 999999)}"
    
    def power_on(self):
        """Turn on the device"""
        if not self.__is_on:
            self.__is_on = True
            self.__power_consumption = self._get_base_power_consumption()
            print(f"🔋 {self.brand} {self.model} is now ON")
        else:
            print(f"⚠️ {self.brand} {self.model} is already ON")
    
    def power_off(self):
        """Turn off the device"""
        if self.__is_on:
            self.__is_on = False
            self.__power_consumption = 0
            print(f"⚫ {self.brand} {self.model} is now OFF")
        else:
            print(f"⚠️ {self.brand} {self.model} is already OFF")
    
    def _get_base_power_consumption(self):
        """Protected method to get base power consumption"""
        return 50  # Base consumption in watts
    
    def get_device_info(self):
        """Get comprehensive device information"""
        status = "ON" if self.__is_on else "OFF"
        return {
            'brand': self.brand,
            'model': self.model,
            'price': self.price,
            'serial_number': self._serial_number,
            'manufacture_date': self._manufacture_date,
            'warranty_years': self.warranty_years,
            'status': status,
            'power_consumption': self.__power_consumption
        }
    
    def is_under_warranty(self):
        """Check if device is still under warranty"""
        # Simplified warranty check (assumes current date)
        return True  # For demonstration purposes
    
    def __str__(self):
        """String representation of the device"""
        return f"{self.brand} {self.model} (SN: {self._serial_number})"
    
    def __repr__(self):
        """Official string representation"""
        return f"Electronics('{self.brand}', '{self.model}', {self.price})"

# Derived class demonstrating inheritance
class Smartphone(Electronics):
    """Smartphone class inheriting from Electronics"""
    
    def __init__(self, brand, model, price, os, storage_gb, camera_mp, battery_mah, warranty_years=2):
        """Initialize smartphone with specific attributes"""
        # Call parent constructor
        super().__init__(brand, model, price, warranty_years)
        
        # Smartphone-specific attributes
        self.os = os
        self.storage_gb = storage_gb
        self.camera_mp = camera_mp
        self.battery_mah = battery_mah
        
        # Private smartphone attributes
        self.__contacts = []
        self.__apps_installed = ["Phone", "Messages", "Settings"]
        self.__battery_level = 100
        self.__screen_locked = True
        
        print(f"📱 Smartphone initialized with {storage_gb}GB storage and {camera_mp}MP camera")
    
    # Override parent method (polymorphism)
    def _get_base_power_consumption(self):
        """Override to provide smartphone-specific power consumption"""
        return 15  # Smartphones use less power than generic electronics
    
    def unlock_screen(self, passcode="1234"):
        """Unlock the smartphone screen"""
        if self.__screen_locked:
            if passcode == "1234":  # Simple passcode for demo
                self.__screen_locked = False
                print("🔓 Screen unlocked successfully!")
                return True
            else:
                print("❌ Incorrect passcode!")
                return False
        else:
            print("ℹ️ Screen is already unlocked")
            return True
    
    def lock_screen(self):
        """Lock the smartphone screen"""
        if not self.__screen_locked:
            self.__screen_locked = True
            print("🔒 Screen locked")
        else:
            print("ℹ️ Screen is already locked")
    
    def add_contact(self, name, phone_number):
        """Add a new contact"""
        if not self.__screen_locked:
            contact = {"name": name, "phone": phone_number}
            self.__contacts.append(contact)
            print(f"👤 Contact added: {name} - {phone_number}")
            return True
        else:
            print("🔒 Please unlock screen first!")
            return False
    
    def install_app(self, app_name):
        """Install a new app"""
        if not self.__screen_locked:
            if app_name not in self.__apps_installed:
                # Simulate storage check
                if len(self.__apps_installed) < (self.storage_gb // 4):  # Rough calculation
                    self.__apps_installed.append(app_name)
                    self.__battery_level -= 2  # Installing apps uses battery
                    print(f"📲 App installed: {app_name}")
                    return True
                else:
                    print("💾 Not enough storage space!")
                    return False
            else:
                print(f"ℹ️ {app_name} is already installed")
                return False
        else:
            print("🔒 Please unlock screen first!")
            return False
    
    def take_photo(self):
        """Take a photo using the camera"""
        if not self.__screen_locked:
            if self.__battery_level > 5:
                self.__battery_level -= 3
                photo_quality = "HD" if self.camera_mp >= 12 else "Standard"
                print(f"📸 Photo taken! Quality: {photo_quality} ({self.camera_mp}MP)")
                return f"{photo_quality}_photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            else:
                print("🔋 Battery too low to take photo!")
                return None
        else:
            print("🔒 Please unlock screen first!")
            return None
    
    def make_call(self, contact_name):
        """Make a phone call"""
        if not self.__screen_locked:
            contact = next((c for c in self.__contacts if c["name"].lower() == contact_name.lower()), None)
            if contact:
                if self.__battery_level > 10:
                    self.__battery_level -= 5
                    print(f"📞 Calling {contact['name']} at {contact['phone']}...")
                    return True
                else:
                    print("🔋 Battery too low to make call!")
                    return False
            else:
                print(f"❌ Contact '{contact_name}' not found!")
                return False
        else:
            print("🔒 Please unlock screen first!")
            return False
    
    def check_battery(self):
        """Check current battery level"""
        battery_status = "🔋" if self.__battery_level > 20 else "🪫"
        print(f"{battery_status} Battery Level: {self.__battery_level}%")
        return self.__battery_level
    
    def charge_battery(self, amount=50):
        """Charge the battery"""
        old_level = self.__battery_level
        self.__battery_level = min(100, self.__battery_level + amount)
        gained = self.__battery_level - old_level
        print(f"🔌 Charged! Battery: {old_level}% → {self.__battery_level}% (+{gained}%)")
    
    def get_contacts(self):
        """Get all contacts (read-only)"""
        if not self.__screen_locked:
            return self.__contacts.copy()  # Return copy to maintain encapsulation
        else:
            print("🔒 Please unlock screen first!")
            return []
    
    def get_installed_apps(self):
        """Get list of installed apps"""
        if not self.__screen_locked:
            return self.__apps_installed.copy()
        else:
            print("🔒 Please unlock screen first!")
            return []
    
    def get_smartphone_info(self):
        """Get comprehensive smartphone information"""
        base_info = super().get_device_info()
        smartphone_info = {
            'os': self.os,
            'storage_gb': self.storage_gb,
            'camera_mp': self.camera_mp,
            'battery_mah': self.battery_mah,
            'battery_level': self.__battery_level,
            'screen_locked': self.__screen_locked,
            'contacts_count': len(self.__contacts),
            'apps_installed': len(self.__apps_installed)
        }
        return {**base_info, **smartphone_info}
    
    def __str__(self):
        """String representation of smartphone"""
        return f"{self.brand} {self.model} ({self.os}, {self.storage_gb}GB, {self.camera_mp}MP)"

# Another derived class to demonstrate polymorphism
class Laptop(Electronics):
    """Laptop class inheriting from Electronics"""
    
    def __init__(self, brand, model, price, os, ram_gb, storage_gb, screen_size, warranty_years=3):
        super().__init__(brand, model, price, warranty_years)
        self.os = os
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.screen_size = screen_size
        self.__programs_running = []
        self.__cpu_usage = 0
    
    def _get_base_power_consumption(self):
        """Override for laptop-specific power consumption"""
        return 65  # Laptops use more power
    
    def run_program(self, program_name):
        """Run a program on the laptop"""
        if program_name not in self.__programs_running:
            self.__programs_running.append(program_name)
            self.__cpu_usage += random.randint(5, 15)
            print(f"💻 Running: {program_name} (CPU: {self.__cpu_usage}%)")
        else:
            print(f"ℹ️ {program_name} is already running")
    
    def close_program(self, program_name):
        """Close a running program"""
        if program_name in self.__programs_running:
            self.__programs_running.remove(program_name)
            self.__cpu_usage = max(0, self.__cpu_usage - random.randint(5, 15))
            print(f"❌ Closed: {program_name} (CPU: {self.__cpu_usage}%)")
        else:
            print(f"ℹ️ {program_name} is not running")
    
    def get_system_info(self):
        """Get laptop system information"""
        base_info = super().get_device_info()
        laptop_info = {
            'os': self.os,
            'ram_gb': self.ram_gb,
            'storage_gb': self.storage_gb,
            'screen_size': self.screen_size,
            'cpu_usage': self.__cpu_usage,
            'running_programs': len(self.__programs_running)
        }
        return {**base_info, **laptop_info}

def demonstrate_classes():
    """Demonstrate the classes and their capabilities"""
    print("🏗️ " + "="*60)
    print("        ASSIGNMENT 1: CLASS DESIGN DEMONSTRATION")
    print("="*65)
    
    # Create Electronics instances
    print("\n📱 Creating Smartphone...")
    phone = Smartphone(
        brand="TechPro", 
        model="X15 Pro", 
        price=899.99, 
        os="Android 14", 
        storage_gb=256, 
        camera_mp=48, 
        battery_mah=4500
    )
    
    print("\n💻 Creating Laptop...")
    laptop = Laptop(
        brand="CompuTech", 
        model="PowerBook Pro", 
        price=1299.99, 
        os="Linux Ubuntu", 
        ram_gb=16, 
        storage_gb=512, 
        screen_size="15.6 inches"
    )
    
    print(f"\n📊 Total Electronics Created: {Electronics.total_devices}")
    
    # Demonstrate polymorphism (same method, different behavior)
    print("\n🔋 Demonstrating Polymorphism - Power Consumption:")
    phone.power_on()
    laptop.power_on()
    
    # Demonstrate encapsulation
    print("\n🔒 Demonstrating Encapsulation - Smartphone Operations:")
    phone.check_battery()
    phone.take_photo()  # Should fail - screen is locked
    phone.unlock_screen()
    phone.add_contact("Alice Smith", "+254712345678")
    phone.add_contact("Bob Johnson", "+254798765432")
    phone.install_app("WhatsApp")
    phone.install_app("Instagram")
    photo = phone.take_photo()
    if photo:
        print(f"📁 Photo saved as: {photo}")
    
    phone.make_call("Alice Smith")
    phone.check_battery()
    
    # Demonstrate inheritance
    print("\n🏗️ Demonstrating Inheritance - Device Information:")
    print("\n📱 Smartphone Info:")
    smartphone_info = phone.get_smartphone_info()
    for key, value in smartphone_info.items():
        print(f"   {key}: {value}")
    
    print("\n💻 Laptop Info:")
    laptop_info = laptop.get_system_info()
    for key, value in laptop_info.items():
        print(f"   {key}: {value}")
    
    # Demonstrate method overriding
    print("\n⚡ Demonstrating Method Overriding - Power Consumption:")
    base_electronics = Electronics("Generic", "Device", 99.99)
    base_electronics.power_on()
    
    # Interactive demonstration
    print("\n" + "="*60)
    print("🎮 INTERACTIVE DEMONSTRATION")
    print("="*60)
    
    while True:
        print("\nChoose an action:")
        print("1. 📱 Smartphone operations")
        print("2. 💻 Laptop operations") 
        print("3. 📊 Show device statistics")
        print("4. 🔋 Charge phone battery")
        print("5. ❌ Exit")
        
        try:
            choice = input("Enter choice (1-5): ").strip()
            
            if choice == '1':
                print("\nSmartphone Operations:")
                print("a. Install app")
                print("b. Take photo") 
                print("c. Make call")
                print("d. Lock/unlock screen")
                
                sub_choice = input("Choose (a-d): ").strip().lower()
                
                if sub_choice == 'a':
                    app_name = input("Enter app name: ").strip()
                    phone.install_app(app_name)
                elif sub_choice == 'b':
                    phone.take_photo()
                elif sub_choice == 'c':
                    contact_name = input("Enter contact name: ").strip()
                    phone.make_call(contact_name)
                elif sub_choice == 'd':
                    if phone.get_smartphone_info()['screen_locked']:
                        phone.unlock_screen()
                    else:
                        phone.lock_screen()
            
            elif choice == '2':
                print("\nLaptop Operations:")
                program = input("Enter program to run: ").strip()
                laptop.run_program(program)
            
            elif choice == '3':
                print(f"\n📊 Device Statistics:")
                print(f"Total devices created: {Electronics.total_devices}")
                print(f"Phone battery: {phone.check_battery()}%")
                print(f"Phone contacts: {len(phone.get_contacts())}")
                print(f"Phone apps: {len(phone.get_installed_apps())}")
            
            elif choice == '4':
                amount = input("Enter charge amount (default 50): ").strip()
                amount = int(amount) if amount.isdigit() else 50
                phone.charge_battery(amount)
            
            elif choice == '5':
                print("👋 Thanks for exploring the class demonstration!")
                break
            
            else:
                print("❌ Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Demonstration ended by user.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    demonstrate_classes()