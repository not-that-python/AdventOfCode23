file = [i.strip(" \n") for i in open("day2.txt", "r").readlines()]

# Part 1: Is it possible?
total = 0
for line in file:
  # identify the game's ID
  game_id = int((line.split(":")[0])[4:])
  valid_game = True
  # split up each record of the game
  records = [i.split(", ") for i in (line.split(": ")[1]).split("; ")]
  # for each record, find the values of red, green, and blue
  # and check the values of each colour
  for row in records:
    for val in row:
      val_items = val.split(" ")
      if val_items[1] == "red" and int(val_items[0]) > 12:
        valid_game = False
      if val_items[1] == "green" and int(val_items[0]) > 13:
        valid_game = False
      if val_items[1] == "blue" and int(val_items[0]) > 14:
        valid_game = False

  # if the game works, add game id to total
  if valid_game:
    #print(game_id)
    total += game_id

#print(total)

# Part 2: Fewest number of cubes
total = 0
for line in file:
  min_red = 0
  min_green = 0
  min_blue = 0
  # for each game, split up each record of the game
  records = [i.split(", ") for i in (line.split(": ")[1]).split("; ")]
  # for each record, if the value of red/green/blue is greater than the minimum, replace the value of the minimum with that value
  for row in records:
    for val in row:
      val_items = val.split(" ")
      if val_items[1] == "red" and int(val_items[0]) > min_red:
        min_red = int(val_items[0])
      if val_items[1] == "green" and int(val_items[0]) > min_green:
        min_green = int(val_items[0])
      if val_items[1] == "blue" and int(val_items[0]) > min_blue:
        min_blue = int(val_items[0])
  #print(f"minimum red: {min_red}, minimum green: {min_green}, minimum_blue: {min_blue}")
  power = min_red * min_green * min_blue
  total += power
#print(total)
