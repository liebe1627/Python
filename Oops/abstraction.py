from abc import ABC,abstractmethod

class TV(ABC):
    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

class TVRemote(TV):
    def turnOn(self):
        print("Turned on the tv")
    
    def turnOff(self):
        print("Turned off the TV")


# TV tv = new TVRemote()

tv = TVRemote()
tv.turnOff()
tv.turnOn()