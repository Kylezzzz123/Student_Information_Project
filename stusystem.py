filename = 'student.txt'
import os      # to import drive
def main():
    while True:
        menu()
        choice = int(input("Please select your choice: "))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input("Are you sure to quite? y/n: ")
                if answer == 'y' or answer == 'Y':
                    print("Thanks!")
                    break
                else: 
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def menu():
    print('------------------------------------------Student Information Management System-----------------------')
    print('------------------------------------------------------Function menu--------------------------------------------------------')
    print('\t\t\t\t\t\t1.Input Student information')
    print('\t\t\t\t\t\t2.Search Student information')
    print('\t\t\t\t\t\t3.Delete Student information')
    print('\t\t\t\t\t\t4.Edit Student information')
    print('\t\t\t\t\t\t5.Sort Student information')
    print('\t\t\t\t\t\t6.Calculate Student information')
    print('\t\t\t\t\t\t7.Show Student information')
    print('\t\t\t\t\t\t0.Quit')
    print('---------------------------------------------------------------------------------------------------------------------------')

def insert():
    student_list = []
    while True:
        id = input ("Please input ID(eg. 1001): ")
        if not id:
            break
        name = input("Please input name: ")
        if not name:
            break
        try:
            english = int(input("Please input English score: "))
            python = int(input("Please input Python score: "))
            java = int(input("Please input Java score: "))
        except: 
            print("Invalid, not integer type, please input again! ")
            continue
        student = {                 # create a library to save information
            'id' : id,
            'name' : name,
            'english' : english,
            'python' : python,
            'java' : java
        }
        student_list.append(student)
        answer = input("Do you want to add? y/n: ")
        if answer == 'y':
            continue
        else:
            break
    # save() function to save information    
    save(student_list)
    print("Student information saved!!!")

def save(lst):
    stu_txt = open(filename, 'a+')  # a+ is to create file if it doesn't exist and open it in append mode
    for item in lst:
        stu_txt.write(str(item)+'\n')  # for loop is to get every element from student_list, and then write it into the list
    stu_txt.close()
                
def search():
    pass

def delete():
    while True:
        student_id = input("Please input stduent ID to remove: ")
        if student_id != '':   # If the input is not blank, move forward, if input it blank, print("No student information"), then break
            if os.path.exists(filename):    # use import os to check if the file exsits
                with open(filename, 'r') as file:   # with open is to open file, you don't need to use close() to close the file
                    student_old = file.readlines()  # readlines is to generate list automatally 
            else:   # else if file is not exit
                student_old = []   #create a list and make it blank []
            flag = False    # mark if remove, blank list is False, it means student_old is not a blank list, and then continue 
            if student_old:
                with open(filename, 'w') as wfile:
                    d={}
                    for item in student_old:
                        d= dict(eval(item))   # tranform string to dict in order to match the student_id, because student_id is string
                        if d['id'] != student_id:   
                            wfile.write(str(d)+ '\n') # write the ID number into file, it means to cover the student information
                        else:
                            flag = True   # mark it is deleted already, it means the the ID number won't be writen into the file, in other words, the ID number is deleted
                    if flag == True: 
                        print(f"ID {student_id} has been deleted")
                    else:
                        print(f'Cannot find {student_id} informatioon')
        else:
            print("No student information")
            break                                   
        show()  # show all student information after deleted  
        answer = input("Want to continue to delete? y/n: ")
        if answer =='y':
            continue
        else:
            break
                
def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass




if __name__ =='__main__':
    main()