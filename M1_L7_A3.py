english_marks = int(input("Enter your English marks: "))
maths_marks = int(input("Enter your Maths marks: "))
hindi_marks = int(input("Enter your Hindi marks: "))
science_marks = int(input("Enter your Science marks: "))
social_science_marks = int(input("Enter your Social Science marks: "))

total_marks = english_marks + maths_marks + hindi_marks + science_marks + social_science_marks
average_marks = total_marks // 5
print("Average marks: ", average_marks)
print("Total marks: ", total_marks)
valid_range = range(0, 101)

if average_marks not in valid_range:
    print("Average marks are out of valid range (0-100). Please check the input marks.")

elif average_marks in range(90, 101):
    print("Grade: A1")

elif average_marks in range(80, 90):
    print("Grade: A2")

elif average_marks in range(70, 80):
    print("Grade: B1")

elif average_marks in range(60, 70):
    print("Grade: B2")

elif average_marks in range(50, 60):
    print("Grade: C1")

elif average_marks in range(40, 50):
    print("Grade: C2")

else:
    print("Grade: D")

