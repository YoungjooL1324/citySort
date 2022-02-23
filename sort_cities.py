#Author: Youngjoo Lee
#Date: 02/19/2022
#Purpose: Sort cities by given criterias
import citiesInOut
from quickSort import *

#SORTING BY CITY NAME

#Purpose: name comparing function, uses the compare strings function in quickSort
def compare_names(a, b):
    return compare_strings(a.name, b.name)

file_name = "world_cities.txt"
in_file = open(file_name, "r")

cityList = citiesInOut.cityList

sort(cityList, compare_names)


alpha_file = open("cities_alpha.txt", "w")
for city in cityList:
    alpha_file.write(str(city))
    alpha_file.write("\n")

alpha_file.close()


#SORTING BY CITY POPULATION
def compare_populations(a,b):
    return b.population <= a.population

sort(cityList, compare_populations)

population_file = open("cities_population.txt", "w")
for city in cityList:
    population_file.write(str(city))
    population_file.write("\n")

population_file.close()

#SORTING BY CITY LATITUDE
def compare_latitude(a,b):
    return compare_ints_floats(a.latitude, b.latitude)

sort(cityList, compare_latitude)

latitude_file = open("cities_latitude.txt", "w")
for city in cityList:
    latitude_file.write(str(city))
    latitude_file.write("\n")

latitude_file.close()
