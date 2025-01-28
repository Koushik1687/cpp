cnt = int(input("enter your hight n centimeter: "))

inch = cnt/2.54

foot = int(inch//12)
f_inch = inch %12
print ("convert to inch: {:.2f}".format(inch))
print (f"convert to foot: {foot}, {f_inch:0.2f}")