file = [i.strip("\n") for i in open("day1.txt", "r").readlines()]

# Part 1: First and Last Digit
total = 0

for line in file:
  oneval = 0
  tenval = 0
  val = 0
  # iterate through the line forwards first
  for i in range(len(line)):
    try:
      tenval = int(line[i]) * 10
      break
    except:
      pass

  # then iterate through the line backwards
  for j in range(len(line)-1, -1, -1):
    try:
      oneval = int(line[j])
      break
    except:
      pass

  val = tenval + oneval
  total += val

print("Solution 1:", total)

# Part 2: Words Are Digits Too

total = 0
word_to_num = {"one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9}
words = list(word_to_num.keys())

# iterate through the line
for line in file:
  check_string = ""
  tenval = 0
  oneval = 0
  val = 0


  # iterate forwards first
  for i in range(len(line)):
    char = line[i]
    # check for numerical first
    try:
      tenval = int(char) * 10
      break
    except:
      pass
    # check for words next
    check_string = check_string + char.lower()
    word_num_check = False
    for word in words:
      if word in check_string:
        word_num_check = True
        tenval = word_to_num[word] * 10
    if word_num_check:
      check_string = ""
      break


  # then iterate backwards
  for j in range(len(line) - 1, -1, -1):
    char = line[j]
    # check for numerical first
    try:
      oneval = int(char)
      break
    except:
      pass
    # check for words next
    check_string = char.lower() + check_string
    word_num_check = False
    for word in words:
      if word in check_string:
        word_num_check = True
        oneval = word_to_num[word]
    if word_num_check:
      check_string = ""
      break

  val = tenval + oneval
  total += val

print("Solution 2:", total)