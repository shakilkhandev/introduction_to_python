# Create a list of areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]




# Change this command


#areas_copy = areas #this will point the same list and if update on copied it will change the original . 
# so need to write like below if want to make a copy of the list named "areas"  y using list() function .

areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
