###Defining GLOBALS
tasks = []
def AddTask():
    newtask = input("New Task: ");
    tasks.append(newtask);
def DeleteTask():
    ListTasks();
    remtask = input("Remove Task: ");
    try:
        tasks.remove(remtask);
    except:
        print("Invalid Input, try again..")

def ListTasks():
    print("\n");
    print("..::To Do List::..");
    for i in tasks:
        print(i);
    print("\n");

###Main Func
if __name__ == "__main__":
    ###Creat a loop to run the app
    print("Welcome to the To-Do List App :)")
    while True:
        print("Please choose an option: ")
        print:("_________________________________________________")
        print("1.Add")
        print("2.Delete")
        print("3.List")
        print("4.Exit")
        choose = input("Option: ");
        print("\n");

        if (choose == "1"):
            AddTask();
        elif (choose == "2"):
            DeleteTask();
        elif (choose == "3"):
            ListTasks();
        elif (choose == "4"):
            break;
        else:
            print("Invalid Input, Restarting...")