#Author: Youngjoo Lee
#Date: 02/19/2022
#Purpose: City class

class City:

    #Purpose: constructor method to store object in memory, and assign instance variables
    def __init__(self, countryCode, name, region, population, latitude, longitude):
        self.countryCode = countryCode #string
        self.name = name #string
        self.region = str(region) #string
        self.population = int(population) #int
        self.latitude = float(latitude) #float
        self.longitude = float(longitude) #float


    #Purpose: string method that will return information about the city object
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

