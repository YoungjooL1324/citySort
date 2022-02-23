#Author: Youngjoo Lee
#Date: 02/21/2022
#Purpose: visualize the cities on a map


from cs1lib import *

WINDOW_HEIGHT = 360
WINDOW_WIDTH = 720
PIXELS_PER_DEGREE = 2 #There are 2 pixels for the graphics map for each degree of latitude/longitude
CITIES_RADIUS = 5
NUMBER_OF_CITIES = 20


desired_csv = "cities_alpha.txt"
in_file = open(desired_csv, "r")

desired_display = 1 #we start only wanting to show the first city
cities_list = []

for line in in_file:
    current_show = 0
    if current_show == desired_display:  #iterate through the file until we reach desired amount of cities
        break
    line = line.strip().split(",")
    city_x = (WINDOW_WIDTH // 2) + int(float(line[3]) * PIXELS_PER_DEGREE) #converts the longitude of city into position on graphics panel
    city_y = (WINDOW_HEIGHT // 2) - int(float(line[2]) * PIXELS_PER_DEGREE) #converts the latitude of city into position on graphics panel

    cities_list.append([city_x, city_y]) #add city to the list
    current_show += 1

in_file.close()

#Purpose: draw the city passed in by the parameter
def draw_cities(city_number):
        latitude = 0
        longitude = 1
        draw_circle(cities_list[city_number][latitude], cities_list[city_number][longitude], CITIES_RADIUS)


#Purpose: main function to be called in start_graphics
def main():
    img = load_image("world.png")
    draw_image(img, 0, 0)
    set_fill_color(1, 0, 0)

    global desired_display
    global cities_list

    for i in range(0, desired_display): #for each frame we only draw the desired amount of cities
        draw_cities(i)

    if desired_display < NUMBER_OF_CITIES: #we make sure to only display the number of cities called for by input
        desired_display += 1




start_graphics(main,  width = 720, height = 360, framerate = 1)
