"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    # Create Course Instance
    course1 = cc.Course(name, crn, seats, status)

    # Register Students
    for student in students:
        # Create registration instance for each student
        registration = cc.Register(student, course1.get_crn())
        # Check if class is open
        if course1.get_status() == "open":
            # update seats left
            course1.update_seat_count()
            # display registration info
            print("\nStudent Name:", registration.get_name())
            print("Course Name:", course1.get_name())
            print("CRN:", course1.get_crn())
            print("Seats left:", course1.get_seats())
            print()
        else:
            # display message after registration closes
            print(
                "Sorry "
                + registration.get_name()
                + ", registration is closed for "
                + course1.get_name()
            )


main()
