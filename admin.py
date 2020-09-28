def show_roster(c_list, r_list):
    # ------------------------------------------------------------
    # Prompts admin to input course to display
    # Takes two argument: course list, roster list
    # Lets admin view students registered in selected course and number of students
    # Return True or False
    # ------------------------------------------------------------
    a_choice = input('Enter course, whose roster you would like to display').upper
    for i, j in enumerate(c_list):
        if j == a_choice:
            print("Current registered students:", r_list[i].sort())
            print('Number of students: ', len(r_list[i]))
        else:
            print("Course not in list")


def change_max_size(c_list, r_list, m_list):
    # ------------------------------------------------------------
    # Prompts admin to input course and the new max size
    # Takes three argument: course list, max size, registration list
    # Lets admin change the max size of a course
    # Returns nothing
    # ------------------------------------------------------------
    print('List of courses and max size: ').upper()
    for i in range(len(c_list)):
        print(c_list[i], m_list[i])
    choice = input('Enter course to change size')
    for i, j in enumerate(c_list):
        if j == choice:
            size = int(input("Enter new max size: "))
            while size < len(r_list[i]):
                print("New max size cannot be smaller than current enrollment")
                size = int(input("Enter new max size: "))
            else:
                m_list[i] = size
                print('New max size: ', size)
        else:
            print("Course not in list")
