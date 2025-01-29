mon  = int(input("Temp for monday: "))
tue  = int(input("Temp for tueday: "))
wed  = int(input("Temp for wedday: "))
thurs  = int(input("Temp for thursday: "))
fri  = int(input("Temp for friday: "))
sat  = int(input("Temp for satday: "))
sun  = int(input("Temp for sunday: "))

print("Average temp for week days: {:.2f}".format((mon+tue+wed+thurs+fri+sat+sun)/7))
