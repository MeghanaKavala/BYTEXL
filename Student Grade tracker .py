class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print("Student already exists.")

    def add_grade(self, student_name, grade):
        if student_name in self.students:
            self.students[student_name].add_grade(grade)
        else:
            print("Student not found.")

    def calculate_average_grade(self, student_name):
        if student_name in self.students:
            average_grade = self.students[student_name].calculate_average_grade()
            print(f"Average grade for {student_name}: {average_grade}")
        else:
            print("Student not found.")

    def generate_grade_report(self):
        print("Grade Report:")
        for student_name, student in self.students.items():
            average_grade = student.calculate_average_grade()
            print(f"{student_name}: Average Grade - {average_grade}")


# Function to handle user input
def main():
    tracker = GradeTracker()

    while True:
        print("\n1. Add Student")
        print("2. Add Grade")
        print("3. Calculate Average Grade")
        print("4. Generate Grade Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            tracker.add_student(name)
        elif choice == "2":
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(name, grade)
        elif choice == "3":
            name = input("Enter student name: ")
            tracker.calculate_average_grade(name)
        elif choice == "4":
            tracker.generate_grade_report()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
