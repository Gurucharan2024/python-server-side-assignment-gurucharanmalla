# input student names
students=[]
n= int(input("How many Students you want?\n"))

for i in range(n):
    name=input(f"Enter the name of student{i+1}:")
    students.append(name)


    #writting names in file
    with open("students.txt","w") as f:
        for student in students:
            f.write(student + "\n")
            
    #Read and display file contacts
    print("\n Stored contents are:")
    with open("students.txt" ,"r") as f:
        for student in students:
            print(f.read())        



            