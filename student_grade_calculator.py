# 1. Takes a student's name as input...............

name = input("Enter student name:")

# 2.Takes marks for 3 subjects.....................

sub1 = float(input("Marks for sub 1:"))
sub2 = float(input("Marks for sub 2:"))
sub3 = float(input("Marks for sub 3:"))

# 3. Calculates....................................

total = sub1 + sub2 + sub3
average = total/3

# Determines the grade using.......................

if average >= 80 and average <= 100:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"



# Displays the result using a formatted string (f-string)..........


print("\n........Student Result........")
print(f"Student name: {name}")
print(f"Total marks: {total}")
print(f"Average marks: {average:2f}")
print(f"Grade: {grade}")