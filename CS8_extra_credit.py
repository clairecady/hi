def show_city(city):
    mapping = {0: '🧑', 1: '🧛', 2: '🚧'}
    for row in city:
        for cell in row:
            emoji = mapping[cell]
            print(emoji, end=' ')
        print()

def vampirize(coordinate, city):
    row, col = coordinate
    height, width = len(city), len(city[0])
    if row > 0 and city[row - 1][col] == 0:
        city[row - 1][col] = 1
    if row < height - 1 and city[row + 1][col] == 0:
        city[row + 1][col] = 1
    if col > 0 and city[row][col - 1] == 0:
        city[row][col - 1] = 1
    if col < width - 1 and city[row][col + 1] == 0:
        city[row][col + 1] = 1

def next_day(city):
    height, width = len(city), len(city[0])
    new_city = [[cell for cell in row] for row in city]  
    for row in range(height):
        for col in range(width):
            if city[row][col] == 1:
                vampirize((row, col), new_city)  

    return new_city

def days_remaining(city):
    day = 0
    while True:
        print(f"Day: {day}")
        show_city(city)
        print()

        new_city = next_day(city)

        if new_city == city:  
            return day, city

        day += 1
        city = new_city
