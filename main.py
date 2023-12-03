# there are 3 types of chars: full-stops, symbols, and numerical digits
# how do you identify a whole number, beyond just a digit? If you keep iterating along the number and until you find a non-numerical char, you have found the end of the number
# check each individual digit first to see if it's adjacent to a symbol or not

# first, identify the value of the number
# Then check each digit for a

file = [i.strip("\n") for i in open("day3.txt", "r").readlines()]
print(file[:5])
total = 0
cur_val = 0
is_part_num = False
is_full_num = False
for i in range(len(file)):
  for j in range(len(file[i])):
    if not file[i][j].isnumeric():
      cur_val = 0
      pass
    if file[i][j].isnumeric():
      if cur_val != 0:
        cur_val = cur_val * 10
      cur_val += int(file[i][j])

      # First check if the number is a full number (otherwise you're halfway through a number)
      if not file[i][j + 1].isnumeric():
        is_full_num = True

      # Then check is the number is a part number and there is a special character nearby
      #adj1 = file[i][j+1]
      #adj2 = file[i][j-1]
      #adj3 = file[i+1][j]
      #adj4 = file[i+1][j+1]
      #adj5 = file[i+1][j-1]
      #adj6 = file[i-1][j]
      #adj7 = file[i-1][j+1]
      #adj8 = file[i-1][j-1]
      #adjs = [adj1, adj2, adj3, adj4, adj5, adj6, adj7, adj8]
      adjs = []
