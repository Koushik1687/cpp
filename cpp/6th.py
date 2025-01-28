import numpy

j =input ("enter some (max 10) students marks of computer : ")
marks = j.split()
sum_no=0
for i in marks:
    sum_no += int(i)
print(sum_no)
c= len(marks)
mean = sum_no/c
median = int(marks[int((c+1)/2)])
mode = (int(marks[int(c/2)])+int(marks[int((c/2)+1)]))/2
print(f"Mean = {mean}")
print(f"Median = {median}")
print(f"Mode = {mode}")