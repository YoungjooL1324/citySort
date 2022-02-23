#Author: Youngjoo Lee
#Date: 02/19/2022
#Purpose: Read in and prase the input file


from city import City

cityList = [] #list with all the city objects

file_name = "world_cities.txt"

in_file = open(file_name, "r") #file to be read

#goes through each line in the passed in file
for line in in_file:
    line = line.strip()
    line = line.split(",") #cleans the lines
    currentCity = City(line[0], line[1], line[2], line[3], line[4], line[5]) #creates new city object with info from current line
    cityList.append(currentCity)#appends the city to the city list

in_file.close()

out_file = open("cities_out.txt", "w") #creates the file to write out the information to

for city in cityList:
    out_file.write(str(city)) #write out the city on a line in the text file using string method of City class
    out_file.write("\n") #to add new line after each city

out_file.close()





