import random   # For randomly placing initial agents.
import os
import time

class Conways:
    def __init__(self, agents, gridsize) -> None:   # Class constructor.
        self.initial_agent = agents
        
        self.grid_size = gridsize

        self.grid = [[0 for i in range(self.grid_size)] for j in range(self.grid_size)]


    def initProvided(self, liveCells):  # To generate the grid when initial state of agents are given.
        # liveCells is a array which contains touples containing x and y index of the agent
        # liveCells : [(2,1), (6,5)]    # liveCells would be array of this type.

        ### Iterate over liveCells and assign a value 1 to corresponding cells in grid array.

        ### for i in liveCells
        ###     self.grid[liveCell_elementPosition] = 1

        pass

    def initRandom(self):   # To generate the grid when initial state of agents are not given randomly.
        liveCells = []    # Array containing location of liveCells in format same as mentioned in initProvided function for liveCells.
        for i in range(self.initial_agent):     # Adding initial_agent number of agents.
            added = False   # If agent is not added yet hence added = False
            while not added:    # Till agent is not added
                x = 0
                y = 0
                ### Randomly assign x and y a integer between 0 and gridsize-1.
                ### x = random_integer_between(0,gridsize-1)
                ### similarly for y.
                
                if (x,y) not in liveCells:  # Checking if randomly generated livecell in not already in the liveCell array.

                    ### Add the tuple (x,y) to liveCells array.
                    ### liveCells.add_to_array((x,y))
                    ### As we have added the agent now what to do with 'added' variable
                    ### added = ??
                    pass

        self.initProvided(liveCells)    # Calling initProvided to generate array.


    def getSurrounding(self, x,y):  # This function returns the value of 8 cells surrounding the given cell and the cell itself in grid.
        # We want our arena (grid) infinite for the agents irrespective of what the size of grid array is.
        # We can do the same by connecting the ends of the grid with the start of the grid.
        # A good analogy would be to connect the two ends of the paper, then an ant walking on the paper would thing that the paper is of infinite length
        # We would be doing same now.
        # when asked element at index -1 we would return the element at the end of the array
        # And when we would be asked for element at index >= size of the array we would start returning elements from the start of the array
        # This way our grid would be infinite.
        # We would do same now to return neighbouring elements of a given cell.
        surr = []   # array which would contain the neighbour cells in format same as mentioned in initProvided function for liveCells.
        for i in range(x-1, x+2):   # Iterating over the neighbouring elements.
            for j in range(y-1, y+2):   # Iteratingn over the neighbouring elements.

                ### append the element accordingly as mentioned above.

                ### surr.add_element_to_list(grid[neighbour_element_as_explained_above])
                pass
        return surr

    def getSurroundliveCells(self, x, y):   # Function returns the number of live cells i.e. grid[cell] == 1, from neighbouring cells.
        surr = self.getSurrounding(x,y)    # Get surrounding cells.
        count = 0   # Counter to count the liveCells
        for i in surr: # Iterating over the surr array
            ### Check whether the i cell is live or not and if so increment the counter.

            ### if i is live
            ###     increment the count
            pass
        

        ### Check if the cell itself is live if so reduce the count by 1.
        
        ### if grid[this_cell] == 1
        ###     reduce count by 1

        return count

    def getNextGen(self):   # Get the new generation grid from the current state of the grid.
        gen = [[0 for i in range(self.grid_size)] for j in range(self.grid_size)]   # Grid to update
        
        for i in range(self.grid_size):     # Iterating over whole grid
            for j in range(self.grid_size):     # Iterating over whole grid
                neigh = self.getSurroundliveCells(i,j)     # Getting number of surrounding live cells.

                ### Now we would change the value of current cell based on the number of live neighbour i.e. "neigh" variable
                ### if neigh < 2 change current cell to 0
                ### if neigh = 2 keep the current state i.e. self.grid[i][j]
                ### if neigh = 3 change current cell to 1
                ### else change current cell to 0

                ### if neigh < 2
                ###    gen[i,j] = 0
                
                ### And same for other cases
                pass

        return gen

    def evolve(self):   # Function to evlove current state to next generation.
        self.grid = self.getNextGen()



#__main__
noAgent = int(input("Enter Number of Agents : "))
gridSize = int(input("Enter grid size: "))
itera = int(input("Enter Number of Iterations"))

con = Conways(noAgent, gridSize)

con.initRandom()

for i in con.grid:
    for j in i:
        print("#", end="") if j == 1 else print(".",end="")
    print()

for i in range(itera):
    con.evolve()
    time.sleep(0.4)
    os.system("cls") # For linux/Mac use "clear"
    
    for i in con.grid:
        for j in i:
            print("#", end="") if j == 1 else print(".",end="")
        print()