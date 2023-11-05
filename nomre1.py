grades = []
total_grades = 0
num_courses = 10
course_names = ["farsi", "zaban", "ejtemaii", "riazi", "fizik", "adabiat", "systemamel", "akhlagh", "shimi", "farsi"]

for i in range(num_courses):
    grade = int(input("inter your grade {course_names[i]} here : "))
    grades.append(grade)
    total_grades += grade

average = total_grades / num_courses


while average < 20:
    print("your grade not enoughe ")
    for i in range(num_courses):
        grade = int(input("add grade {course_names[i]} trying to add a grade : "))
        grades[i] = grade
        total_grades += grade - grades[i]
    average = total_grades / num_courses

print("exelent your win this bycicle")
print("bycicle")
    
    
