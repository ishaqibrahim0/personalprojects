# --------------------------------------------------------------
# Author: Ishaq Ibrahim
# Date: November 3, 2019
#
# This program simulates registration system for schools.
# It inputs list of students and administrators for login
# Inputs classes offered, registration list for those classes and max size
# and processes Course scheduling(add, drop, max size, etc.)
# takes user type, ID, and pin from user.
# --------------------------------------------------------------

from student import add_course, drop_course, list_courses
from admin import show_roster, change_max_size


def main():
    # ------------------------------------------------------------
    # Calls proper processing based on user type
    # Take one argument: user type.
    # Update and guide user to proper registration system
    # Return nothing
    # ------------------------------------------------------------
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    admin_list = [('7001', '777'), ('8001', '888')]
    course_list = ['CSC121', 'CSC122', 'CSC221']
    max_size_list = [2, 2, 1]
    roster_list = [['1004', '1003'], ['1001'], ['1002']]

    print("Enter 1 if you are student")
    print(" 2 if you are admin")
    print("0 to quit: ")
    user_type = input('Please enter user type: ')
    while user_type in {'0', '1', '2'}:
        if user_type == '1':
            student_session(c_list=course_list, r_list=roster_list, m_list=max_size_list, s_list=student_list)
        elif user_type == '2':
            admin_session(c_list=course_list, r_list=roster_list, m_list=max_size_list, a_list=admin_list)
        elif user_type == '0':
            print('Exiting Registration system')
            break


def login(id_list):
    # ------------------------------------------------------------
    # Prompts user to input ID and pin
    # Take one argument: id_list.
    # Verify user in the list
    # Return True or False
    # ------------------------------------------------------------
    ID = input('Enter ID: ')
    pin = input("Enter PIN: ")
    s_login = (ID, pin)
    while s_login in id_list:
        return True
    else:
        return False


def student_session(c_list, r_list, m_list, s_list):
    # ------------------------------------------------------------
    # Prompts user to input their registration function
    # Take four arguments: course list, roster list, max size list and student list.
    # Allows verified users to select their registration method
    # Returns nothing
    # ------------------------------------------------------------
    print('student session')
    while login(id_list=s_list) is True:
        print('ID and Pin verified')
        choice = input('Enter 1 to add course\n'
                       '2 to drop course \n'
                       '3 to see your registered courses\n'
                       '0 to exit\n')
        if choice == '1':
            add_course(id, c_list, r_list, m_list)
        elif choice == '2':
            drop_course(id, c_list, r_list)
        elif choice == '3':
            list_courses(id, c_list, r_list)
        elif choice == '0':
            print("Student session ended")
            break


def admin_session(c_list, r_list, m_list, a_list):
    # ------------------------------------------------------------
    # Prompts user to select admin functions
    # Takes four arguments: course list, roster list, max size list and admin list
    # Verified admins can choose how they can edit courses
    # Returns nothing
    # ------------------------------------------------------------
    print('administrator session')
    while login(id_list=a_list) is True:
        print('ID and Pin verified')
        choice = input('Enter 1 to show class roster\n'
                       '2 to change max class size\n'
                       '0 to exit')
        if choice == '1':
            show_roster(c_list, r_list)
            choice = input('Enter 1 to show class roster\n'
                           '2 to change max class size\n'
                           '0 to exit')
        elif choice == '2':
            change_max_size(c_list, r_list, m_list)
            choice = input('Enter 1 to show class roster\n'
                           '2 to change max class size\n'
                           '0 to exit')
        else:
            print('Administrator session ended')
            break
    else:
        print("ID or pin incorrect")


main()
