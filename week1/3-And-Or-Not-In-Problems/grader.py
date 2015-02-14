student_result=int(input("Student points: "))

if 0 <= student_result <= 50:
    print("Weak result-2")
elif 51 <= student_result <= 60:
    print("Poor result-3")
elif 61 <= student_result <= 70:
    print("Good result-4")
elif 71 <= student_result <= 80:
    print("Very good result-5")
elif 81 < student_result < 100:
    print("Excellent-6")
elif 100 == student_result:
    print("Verry Excellent!!-7")
else:
    print("Enter valid number in range 0-100")
