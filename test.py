
valid_unit = False
while valid_unit == False:
  units = input("mm, cm, or M? ").lower().strip()
  if units != "mm" and units != "cm" and units != "m":
    print("Please enter mm, cm or M")
  else:
    print("program continues")