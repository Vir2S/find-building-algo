################################ First task ###################################


def func(num):
    if num % 10 == 0:
        return "zero"
    
    if num % 5 == 0:
        return "five"
    
    if num % 2 == 0:
        return "even"
    
    return "odd"


print(func(10))
print(func(8))
print(func(15))
print(func(9))


################################ Second task ###################################


def find_building(input_map):
    for row in input_map:
        for cell in row:
            if cell not in ["B", "E"]:
                return -1
    
    visited = set()
    
    def dfs(i, j):
        if (i, j) in visited:
            return False
        visited.add((i, j))
        if input_map[i][j] == "B":
            if i > 0:
                dfs(i - 1, j)
            if i < len(input_map) - 1:
                dfs(i + 1, j)
            if j > 0:
                dfs(i, j - 1)
            if j < len(input_map[0]) - 1:
                dfs(i, j + 1)
            return True
        else:
            return False
    
    building_count = 0
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if dfs(i, j):
                building_count += 1
    
    return building_count


print(find_building([["B", "B", "B"], ["B", "E", "B"], ["E", "E", "E"], ["E", "E", "B"], ["B", "E", "B"]]))
