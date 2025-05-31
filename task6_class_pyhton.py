#Define a student class
class Student:
    #This funtion runs when we create a anew student
    def own(self):
        self.name = ""
        self.roll = ""
        self.contact = ""
        self.marks = 0.0

        #Function to input student details from the user
        def input_details(self):
            self.name = input("Enter student's name: ")
            self.roll = input("Enter roll number: ")
            self.contact = input("Enter contact number: ")
            self.marks = float(input("Enter marks: "))

            #Function to display student details
            def display_details(self):
                print("\n--- Student Details ---")
                print("Name           :",self.name)
                print("Roll Number    :",self.roll)
                print("Contact        :",self.contact)
                print("Marks          :",self.marks)

            #craete student object
            student1 = Student()

            #call the method to input details
            student1.input_details()

            #call the method to display details
            student1.display_details