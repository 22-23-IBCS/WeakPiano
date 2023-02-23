import random


class House:
    # constructor
    def __init__(self):
        self.rating = random.randint(1,10)
        self.visited = False
        
def next_best_house(matrix, i, j):
    # given location i, j
    # find the best house in the 4 directions and return location
    # directions are: (up, down, left, right)
    # up: matrix[i-1][j]
    # down: matrix[i+1][j]
    # left: matrix[i][j-1]
    # right: matrix[i][j+1]
    # should also check if i am going out of bounds
    # eg. if i=0, do not index matrix[i-1][j]
    # if the house has been visited, do not consider it
    
    best_rating = -1
    best_next_location = (i,j)
    next_locations = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for location in next_locations:
        
        
        # check if out of bounds
        # TODO
        # has the house been visited?
        # TODO
        # check whether the rating is better than the current best
        # TODO
        # update the best rating and best next location
        # TODO
    
        return next_location

def main():
    
    num=int(input("How many houses?\n"))
    
    n = 5
    m = 5
    
    # create 5x5 zero matrix
    house_matrix = [0] * n
    for i in range(n):
        house_matrix[i] = [0] * m
        
    # put houses in matrix
    for i in range(n):
        for j in range(m):
            house_matrix[i][j] = House()
        
    # start at the best house
    max_val = house_matrix[0][0].rating
    best_location = (0,0)
    for i in range(n):
        for j in range(m):
            rating = house_matrix[i][j].rating
            if rating > max_val:
                max_val = rating
                best_location = (i,j)
    
    num_visited = 0
    next_location = best_location
    path = []
    while num_visited < num:
        i = next_location[0]
        j = next_location[1]
        path.append(house_matrix[i][j].rating)
        house_matrix[i][j].visited = True
        next_location = next_best_house(house_matrix, i, j)
        
    # find the sum of the house matrix
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += house_matrix[i][j].rating
            
    house_average = sum / (n*m)
            
    if sum(path) / num > house_average:
        print("ideal path found")
        print(path)

if __name__ =="__main__":
    main()
