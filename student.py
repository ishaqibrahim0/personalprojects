def add_course(id, c_list, r_list, m_list):
    # ------------------------------------------------------------
    # Prompts student to input course they would like to add
    # Takes four argument: id, course list, roster list, max size list
    # Lets students registered for a course
    # Return nothing
    # ------------------------------------------------------------
    print('List of courses: ', c_list)
    course = input("Enter course you want to add: ").upper()
    if course in c_list:
        for i, j in enumerate(c_list):
            if j == course:
                if id in r_list[i]:
                    print("You are already enrolled in that course")
                else:
                    if len(r_list[i]) < m_list[i]:
                        print("You are registered for the course")
                        r_list[i].append(id)
                    else:
                        print("Class already full")
    else:
        print("Course not found")


def drop_course(id, c_list, r_list):
    # ------------------------------------------------------------
    # Prompts student to input course they would like to drop
    # Takes four argument: id, course list, roster list
    # Lets students drop a course theyre registered for
    # Return nothing
    # ------------------------------------------------------------
    d_course = input('Please enter course Id to drop: ').upper()
    for i, j in enumerate(c_list):
        if j == d_course:
            if id in r_list[i]:
                print("Course Dropped")
                r_list[i].remove(id)
            else:
                print("Error: You are not enrolled the course")
        else:
            print('Course not found')


def list_courses(id, c_list, r_list):
    # ------------------------------------------------------------
    # Prompts student to view course they are registered for
    # Takes three argument: id, course list, roster list
    # Lets students view they're current courses
    # Return nothing
    # ------------------------------------------------------------
        for i, j in range(len(c_list)):
            if id in r_list[i]:
                print("Courses registered", c_list[i])
                count = r_list[i].count(id)
                print("Number of courses registered: ", count)
