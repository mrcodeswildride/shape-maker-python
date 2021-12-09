def make_line(size):
  line = ""
  for column in range(size):
    line = line + "* "
  print(line)

def make_square(size):
  for row in range(size):
    line = ""
    for column in range(size):
      line = line + "* "
    print(line)

def make_triangle(size):
  for row in range(size):
    line = ""
    for column in range(row + 1):
      line = line + "* "
    print(line)

print()

shape = input("Choose a shape [line/square/triangle]: ")
size = int(input("Enter a size [2-10]: "))
print()

if shape == "line":
  make_line(size)
elif shape == "square":
  make_square(size)
elif shape == "triangle":
  make_triangle(size)
else:
  print("Invalid shape.")
