#!/usr/bin/env python3
"""
Activity 2: Polymorphism Challenge! 🎭
=====================================
This program demonstrates polymorphism through a transportation system
where different vehicles implement the same methods differently.

Key Concepts Demonstrated:
1. Method Overriding (same method name, different implementations)
2. Polymorphic behavior through inheritance
3. Abstract base concepts
4. Interface consistency across different classes
"""

from abc import ABC, abstractmethod
import random
import time

# Abstract base class defining the interface
class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, name, max_speed, fuel_type, capacity):
        self.name = name
        self.max_speed = max_speed  # in km/h
        self.fuel_type = fuel_type
        self.capacity = capacity  # passenger capacity
        self.current_speed = 0
        self.is_moving = False
        self.fuel_level = 100  # percentage
        self.distance_traveled = 0
    
    @abstractmethod
    def move(self):
        """Abstract method - must be implemented by all subclasses"""
        pass
    
    @abstractmethod
    def stop(self):
        """Abstract method - must be implemented by all subclasses"""
        pass
    
    @abstractmethod
    def make_sound(self):
        """Abstract method - each vehicle makes different sounds"""
        pass
    
    def accelerate(self, speed_increase):
        """Common method that can be overridden"""
        if self.is_moving:
            old_speed = self.current_speed
            self.current_speed = min(self.max_speed, self.current_speed + speed_increase)
            print(f"⚡ {self.name} accelerated: {old_speed} → {self.current_speed} km/h")
        else:
            print(f"❌ {self.name} is not moving. Call move() first!")
    
    def get_info(self):
        """Get vehicle information"""
        status = "Moving" if self.is_moving else "Stopped"
        return {
            'name': self.name,
            'type': self.__class__.__name__,
            'max_speed': self.max_speed,
            'current_speed': self.current_speed,
            'fuel_type': self.fuel_type,
            'capacity': self.capacity,
            'status': status,
            'fuel_level': f"{self.fuel_level}%",
            'distance_traveled': f"{self.distance_traveled:.1f} km"
        }
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

# Concrete vehicle classes demonstrating polymorphism

class Car(Vehicle):
    """Car class with specific movement behavior"""
    
    def __init__(self, name, max_speed=180, capacity=5):
        super().__init__(name, max_speed, "Gasoline", capacity)
        self.gear = 1
        self.doors = 4
    
    def move(self):
        """Car-specific movement implementation"""
        if not self.is_moving:
            self.is_moving = True
            self.current_speed = 30
            print(f"🚗 {self.name} is driving on the road at {self.current_speed} km/h")
            self.make_sound()
        else:
            print(f"🚗 {self.name} is already driving!")
    
    def stop(self):
        """Car-specific stopping implementation"""
        if self.is_moving:
            print(f"🛑 {self.name} is braking and coming to a stop...")
            time.sleep(0.5)
            self.current_speed = 0
            self.is_moving = False
            print(f"🚗 {self.name} has stopped and parked.")
        else:
            print(f"🚗 {self.name} is already stopped!")
    
    def make_sound(self):
        """Car-specific sound"""
        sounds = ["Vroom vroom! 🏎️", "Beep beep! 📯", "Engine purring... 🚗"]
        print(f"🔊 {random.choice(sounds)}")
    
    def shift_gear(self, gear):
        """Car-specific method"""
        if 1 <= gear <= 6 and self.is_moving:
            self.gear = gear
            print(f"⚙️ {self.name} shifted to gear {gear}")
        else:
            print(f"❌ Cannot shift to gear {gear}")

class Plane(Vehicle):
    """Airplane class with specific movement behavior"""
    
    def __init__(self, name, max_speed=900, capacity=200):
        super().__init__(name, max_speed, "Jet Fuel", capacity)
        self.altitude = 0
        self.is_airborne = False
    
    def move(self):
        """Plane-specific movement implementation"""
        if not self.is_moving:
            print(f"✈️ {self.name} is taxiing to the runway...")
            time.sleep(1)
            print(f"✈️ {self.name} is taking off...")
            self.is_moving = True
            self.is_airborne = True
            self.current_speed = 250
            self.altitude = 1000
            print(f"✈️ {self.name} is flying at {self.current_speed} km/h, altitude {self.altitude}m")
            self.make_sound()
        else:
            print(f"✈️ {self.name} is already flying!")
    
    def stop(self):
        """Plane-specific stopping implementation"""
        if self.is_moving:
            print(f"🛬 {self.name} is beginning descent...")
            self.altitude = 0
            print(f"🛬 {self.name} is landing on runway...")
            time.sleep(1)
            self.current_speed = 0
            self.is_moving = False
            self.is_airborne = False
            print(f"✈️ {self.name} has landed and is at the gate.")
        else:
            print(f"✈️ {self.name} is already on the ground!")
    
    def make_sound(self):
        """Plane-specific sound"""
        sounds = ["WHOOOOSH! 🌪️", "Jet engines roaring! ✈️", "Turbulence rumbling... 🌩️"]
        print(f"🔊 {random.choice(sounds)}")
    
    def climb_altitude(self, target_altitude):
        """Plane-specific method"""
        if self.is_airborne:
            self.altitude = target_altitude
            print(f"📈 {self.name} climbed to {target_altitude}m altitude")
        else:
            print(f"❌ {self.name} must be airborne to change altitude!")

class Boat(Vehicle):
    """Boat class with specific movement behavior"""
    
    def __init__(self, name, max_speed=60, capacity=50):
        super().__init__(name, max_speed, "Diesel", capacity)
        self.anchor_down = True
    
    def move(self):
        """Boat-specific movement implementation"""
        if not self.is_moving:
            if self.anchor_down:
                print(f"⚓ Raising anchor for {self.name}...")
                self.anchor_down = False
                time.sleep(0.5)
            print(f"🚤 {self.name} is sailing across the water...")
            self.is_moving = True
            self.current_speed = 25
            print(f"⛵ {self.name} is cruising at {self.current_speed} km/h")
            self.make_sound()
        else:
            print(f"⛵ {self.name} is already sailing!")
    
    def stop(self):
        """Boat-specific stopping implementation"""
        if self.is_moving:
            print(f"🛑 {self.name} is slowing down...")
            self.current_speed = 0
            self.is_moving = False
            print(f"⚓ Dropping anchor for {self.name}...")
            self.anchor_down = True
            print(f"⛵ {self.name} is anchored at port.")
        else:
            print(f"⛵ {self.name} is already anchored!")
    
    def make_sound(self):
        """Boat-specific sound"""
        sounds = ["Splash splash! 🌊", "Foghorn: HOOOONK! 📯", "Waves lapping... 🌊"]
        print(f"🔊 {random.choice(sounds)}")
    
    def drop_anchor(self):
        """Boat-specific method"""
        if not self.anchor_down and not self.is_moving:
            self.anchor_down = True
            print(f"⚓ Anchor dropped for {self.name}")
        else:
            print(f"⚓ Anchor is already down or boat is moving!")

class Bicycle(Vehicle):
    """Bicycle class with specific movement behavior"""
    
    def __init__(self, name, max_speed=40, capacity=2):
        super().__init__(name, max_speed, "Human Power", capacity)
        self.pedaling = False
        self.gear = 1
    
    def move(self):
        """Bicycle-specific movement implementation"""
        if not self.is_moving:
            print(f"🚴 Starting to pedal {self.name}...")
            self.is_moving = True
            self.pedaling = True
            self.current_speed = 15
            print(f"🚴 {self.name} is cycling at {self.current_speed} km/h")
            self.make_sound()
        else:
            print(f"🚴 {self.name} is already cycling!")
    
    def stop(self):
        """Bicycle-specific stopping implementation"""
        if self.is_moving:
            print(f"🛑 Applying brakes to {self.name}...")
            self.current_speed = 0
            self.is_moving = False
            self.pedaling = False
            print(f"🚴 {self.name} has stopped.")
        else:
            print(f"🚴 {self.name} is already stopped!")
    
    def make_sound(self):
        """Bicycle-specific sound"""
        sounds = ["Ring ring! 🔔", "Whoosh of wind! 💨", "Chain clicking... ⚙️"]
        print(f"🔊 {random.choice(sounds)}")
    
    def ring_bell(self):
        """Bicycle-specific method"""
        print(f"🔔 Ring ring! {self.name} is signaling!")

class Train(Vehicle):
    """Train class with specific movement behavior"""
    
    def __init__(self, name, max_speed=300, capacity=500):
        super().__init__(name, max_speed, "Electric", capacity)
        self.cars = 8
        self.station = "Central Station"
    
    def move(self):
        """Train-specific movement implementation"""
        if not self.is_moving:
            print(f"🚂 All aboard! {self.name} is departing from {self.station}...")
            time.sleep(1)
            print(f"🚂 {self.name} is accelerating on the tracks...")
            self.is_moving = True
            self.current_speed = 80
            print(f"🚃 {self.name} is traveling at {self.current_speed} km/h on the railway")
            self.make_sound()
        else:
            print(f"🚃 {self.name} is already traveling!")
    
    def stop(self):
        """Train-specific stopping implementation"""
        if self.is_moving:
            print(f"🛑 {self.name} is approaching the next station...")
            print(f"🚂 Brakes engaging for {self.name}...")
            time.sleep(1)
            self.current_speed = 0
            self.is_moving = False
            print(f"🚃 {self.name} has arrived at the station. Doors opening...")
        else:
            print(f"🚃 {self.name} is already at the station!")
    
    def make_sound(self):
        """Train-specific sound"""
        sounds = ["Choo choo! 🚂", "TOOT TOOT! 📯", "Clackety-clack on tracks... 🛤️"]
        print(f"🔊 {random.choice(sounds)}")
    
    def change_station(self, new_station):
        """Train-specific method"""
        if not self.is_moving:
            self.station = new_station
            print(f"🚉 {self.name} is now at {new_station}")

def demonstrate_polymorphism():
    """Demonstrate polymorphism with different vehicles"""
    print("🎭 " + "="*60)
    print("        ACTIVITY 2: POLYMORPHISM CHALLENGE")
    print("="*65)
    print("Same methods, different behaviors!