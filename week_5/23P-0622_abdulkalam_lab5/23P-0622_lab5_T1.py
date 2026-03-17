class Course:
    def __init__(self, name, creditshours, marks):
        self.name = name
        self.creditshours = creditshours
        self.marks = marks
        self.letter_grade = self.calculate_letter_grade()
        self.grade_point = self.calculate_grade_point()

    def calculate_letter_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 85:
            return "A-"
        elif self.marks >= 80:
            return "B+"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 70:
            return "B-"
        elif self.marks >= 65:
            return "C+"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def calculate_grade_point(self):
        grade_points = {
            "A": 4.0,
            "A-": 3.67,
            "B+": 3.33,
            "B": 3.0,
            "B-": 2.67,
            "C+": 2.33,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return grade_points[self.letter_grade]


class Student:
    def __init__(self, name, roll_number, department, semester, courses):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.semester = semester
        self.courses = courses

    def calculate_semester_gpa(self):
        total_quality_points = 0
        total_creditshours = 0

        for course in self.courses:
            total_quality_points += course.grade_point * course.creditshours
            total_creditshours += course.creditshours

        return total_quality_points / total_creditshours if total_creditshours != 0 else 0

    def print_transcript(self):
        print("=" * 70)
        print(f"{'NATIONAL UNIVERSITY OF COMPUTER & EMERGING SCIENCES (FAST)':^70}")
        print(f"{'OFFICIAL ACADEMIC TRANSCRIPT':^70}")
        print("=" * 70)

        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_number}")
        print(f"Department : {self.department}")
        print(f"Semester   : {self.semester}")
        print("-" * 70)

        print(f"{'Course Name':<25}{'Cr.Hrs':<10}{'Marks':<10}{'Grade':<10}{'G.Point':<10}")
        print("-" * 70)

        for course in self.courses:
            print(f"{course.name:<25}{course.creditshours:<10}{course.marks:<10}"
                  f"{course.letter_grade:<10}{course.grade_point:<10.2f}")

        print("-" * 70)

        semester_gpa = self.calculate_semester_gpa()
        print(f"{'Semester GPA':>55} : {semester_gpa:.2f}")
        print("=" * 70)


# ----------- Example Usage -------------

courses = [
    Course("Artifical intelligence ", 3, 92),
    Course("Complier Construction", 4, 81),
    Course("Software ENG", 3, 76),
    Course("Discrete Structures", 3, 88),
    Course("Big Data Analytics", 2, 73)
]

student = Student(
    name="Abdul kalam",
    roll_number="23P-0622",
    department="BS Computer Science",
    semester="Spring 2026",
    courses=courses
)

student.print_transcript()