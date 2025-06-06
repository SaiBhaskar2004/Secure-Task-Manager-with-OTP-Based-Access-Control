# SIMPLE TO DO LIST 
# USER ADD THEIR TASK ACCORDING TO THEIR CHRONOLOGICAL ORDER TO COMPLETE THEIR APPROPRIAATE TASK
# USER CAN ADD THEIR THEIR TASK NAME, DEAD LINE, TASK DETAILS, CLIENT DETAILS AND ETC
import random
print("\nnWelcome to Simple To Do List::\n")

user_id = []
pass_wd = []


task_name = []
task_details = []
task_deadline = []
client_details = []

def generate_otp():
    return str(random.randint(100000, 999999))

def verify_otp():
    otp = generate_otp()
    print(f"Your OTP is: {otp}")  
    user_otp = input("Enter the OTP sent to you: ")
    if user_otp == otp:
        return True
    else:
        print("Incorrect OTP. Access Denied.")
        return False



def login():
    userid = int(input("Enter Your User ID:: "))
    passwd = input("Enter Your Password:: ")
    if userid in user_id:
        index = user_id.index(userid)
        if pass_wd[index] == passwd:
            if verify_otp():
                print("Authentication Success:: ")
                main_func()
            else:
                print("OTP verification failed.")
        else:
            print("Wrong Password. Try Again!")
    else:
        print("User ID Not Found!")


def signup():
    userid = int(input("Enter Your User ID:: "))
    if userid in user_id:
        print("User ID already exists. Try logging in.")
        return
    passwd = input("Enter Your Password:: ")
    user_id.append(userid)
    pass_wd.append(passwd)
    print("Your credentials have been saved successfully. Continue to Login >>>")
    login()

def forgot():
    userid = int(input("Enter Your User ID:: "))
    if userid in user_id:
        if verify_otp():
            index = user_id.index(userid)
            passwd = input("Enter Your New Password:: ")
            pass_wd[index] = passwd
            print("Password Reset Successfully. Continue to Login >>>")
            login()
        else:
            print("OTP verification failed.")
    else:
        print("User ID not found.")


def main_func():
    name = input("Enter Your Name:: ")
    print(f"\nHello {name}! Welcome to Simple To Do List.\nLet us Add Your Task Details...\n")
    total_tasks = int(input("Enter How Many Tasks You Want To Enter:: "))
    for i in range(total_tasks):
        name1 = input("Enter The Task Name:: ")
        details = input("Enter The Task Details:: ")
        deadline = input("Enter The Task Deadline:: ")
        client = input("Enter The Client Name:: ")
        task_name.append(name1)
        task_details.append(details)
        task_deadline.append(deadline)
        client_details.append(client)
    display()
    operation()

def retrive_task():
    output = int(input("Enter Task Number To Retrieve Details:: "))
    if 0 <= output < len(task_name):
        print(f"\nTask #{output}: {task_name[output]}, {task_details[output]}, {task_deadline[output]}, {client_details[output]}\n")
    else:
        print("Invalid Task Number.")

def add_taskfunc():
    print("Enter New Task Details:")
    name1 = input("Enter The Task Name:: ")
    details = input("Enter The Task Details:: ")
    deadline = input("Enter The Task Deadline:: ")
    client = input("Enter The Client Name:: ")
    task_name.append(name1)
    task_details.append(details)
    task_deadline.append(deadline)
    client_details.append(client)
    print("Task Added Successfully.")
    display()

def remove_task():
    poptaskno = int(input("Enter Task Number To Remove:: "))
    if 0 <= poptaskno < len(task_name):
        task_name.pop(poptaskno)
        task_details.pop(poptaskno)
        task_deadline.pop(poptaskno)
        client_details.pop(poptaskno)
        print("Task Deleted Successfully.")
    else:
        print("Invalid Task Number.")

def update_details():
    update_no = int(input("Enter Task Index To Update:: "))
    if 0 <= update_no < len(task_name):
        data_type = input("Enter:\n0 --> Task Name\n1 --> Task Details\n2 --> Deadline\n3 --> Client Details\nChoice:: ")
        if data_type == '0':
            new_value = input("Enter New Task Name:: ")
            task_name[update_no] = new_value
        elif data_type == '1':
            new_value = input("Enter New Task Details:: ")
            task_details[update_no] = new_value
        elif data_type == '2':
            new_value = input("Enter New Deadline:: ")
            task_deadline[update_no] = new_value
        elif data_type == '3':
            new_value = input("Enter New Client Details:: ")
            client_details[update_no] = new_value
        else:
            print("Invalid Option.")
    else:
        print("Invalid Task Index.")

def display():
    print("\nYour Task List:\n")
    print("Task No\tTask Name\tTask Details\tDeadline\tClient")
    for k in range(len(task_name)):
        print(f"{k}\t{task_name[k]}\t{task_details[k]}\t{task_deadline[k]}\t{client_details[k]}")

def operation():
    while True:
        function_type = input("\nSelect an Option:\n0 --> Retrieve Task\n1 --> Add Task\n2 --> Delete Task\n3 --> Update Task\n4 --> View All Tasks\n5 --> Exit\nChoice:: ")
        match function_type:
            case '0':
                retrive_task()
            case '1':
                add_taskfunc()
            case '2':
                remove_task()
            case '3':
                update_details()
            case '4':
                display()
            case '5':
                print("Exiting Task Manager...")
                break
            case _:
                print("Invalid Selection.")

# Start authentication
cred_type = input("Enter:\n1 --> Login\n2 --> Sign Up\n3 --> Forgot Password\nChoice:: ")
match cred_type:
    case '1':
        login()
    case '2':
        signup()
    case '3':
        forgot()
    case _:
        print("Invalid Selection.")
