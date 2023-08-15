
#Functions go at the top
def shape_picker(question):
  shape_selected = input(question).strip().lower()
  if shape_selected == shapes[0]:
    length = input("What is the length of your shape?")

#Lists go under functions
shapes = ["square", "triangle", "rectangle", "circle", "parallelogram"]

#Use the function
shape_picker("Choose a shape: ")
