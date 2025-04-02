class Location:
    def __init__(self, address=None, city=None, state=None, postal_code=None, latitude=None, longitude=None):
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude
    
    # Getter functions
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def getState(self):
        return self.state
    def getPostalCode(self):
        return self.postal_code
    def getLatitude(self):
        return self.latitude
    def getLongitude(self):
        return self.longitude
    
    # Setter functions
    def setAddress(self, address):
        self.address = address
    def setCity(self, city):
        self.city = city
    def setState(self, state):
        self.state = state
    def setPostalCode(self, postal_code):
        self.postal_code = postal_code
    def setLatitude(self, latitude):
        self.latitude = latitude
    def setLongitude(self, longitude):
        self.longitude = longitude
    