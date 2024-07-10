

import  os
def calculate_map_coordinates(center_x, center_z, grid_size, map_size):

    half_grid_size = grid_size // 2
    map_centers = []

    # Calculate starting point for the grid
    start_x = center_x - (half_grid_size * map_size)
    start_z = center_z - (half_grid_size * map_size)

    # Iterate through each row and column to generate map centers
    for i in range(grid_size):
        map_centers.append([])
        for j in range(grid_size):
            map_x = start_x + i * map_size
            map_z = start_z + j * map_size
            
            map_centers[i].append((map_x, map_z))

    return map_centers

try:
    os.remove("mapcalc/coordinate.txt")
except:
    print("no  coordinates file skipping...")

# Example usage:
center_x = int(input("center x?  : "))
center_z =  int(input("center z?  : "))
grid_size =  int(input("grid size?: "))
map_size =  int(input("map size?  : "))
with  open("mapcalc/coordinate.txt","w") as f:
    for i in range(grid_size):
        f.write("t\n")



map_coordinates = calculate_map_coordinates(center_x, center_z, grid_size, map_size)

with open("mapcalc/coordinate.txt","r") as file:
    data = file.readlines()

    
rowcount = 0
for row in map_coordinates:
    data[rowcount] = str(row)+"\n"
    rowcount+=1
    
    
with open('mapcalc/coordinate.txt', 'w') as file:
    file.writelines(data)


        
