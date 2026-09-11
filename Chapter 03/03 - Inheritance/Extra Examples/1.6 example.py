class Camera:
    def take_photo(self):
        print("Photo Captured")


class Battery:
    def charge(self):
        print("Battery Charging")


class SmartPhone(Camera, Battery):
    def call(self):
        print("Calling...")


phone = SmartPhone()

phone.take_photo()
phone.charge()
phone.call()