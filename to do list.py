tasks=[]
def addtask():
    task=input("Enter a task:")
    tasks.append(task)
    print(task,"task is added.")


def deltask():
    distask()
    try:
        TaskToBeDel=int(input("Enter the task you want to delete:"))
        # TaskToBeDel value is equal to list indexes.
        if TaskToBeDel>=0 and TaskToBeDel<len(tasks):
            tasks.pop(TaskToBeDel)
            print("Task",TaskToBeDel,"has been removed.")
        else:
            print(" Task to be deleted is not found")
    except:
        print("Invalid input")


def distask():
    if not tasks:
        print("There are no tasks.")
    else:
        for i in tasks:
            print(i)

if __name__=="__main__":
    print("TO DO LIST")
    while True:
        print("\n")
        print("1.Add a task")
        print("2.Delete a task")
        print("3.Display tasks")
        print("4.Quit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            addtask()
        elif choice==2:
            deltask()
        elif choice==3:
            distask()
        elif choice==4:
            break
        else:
            print("Enter correct choice")