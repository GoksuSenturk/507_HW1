
showFile = open("./sonuc.txt", 'r')
lowest = None
for line in showFile:
    tokens = line.split(',')
    value = min(tokens[:1])
    if lowest == None:
        lowest = value #set lowest value to first number found
    if value < lowest:
        lowest = value

print("The lowest is", lowest)