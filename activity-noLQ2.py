# Student Name: Dela Cruz Jerimie R.
# Course, Year, and Section: BSCS-3B
# Quiz No.: Quiz 2
# Date: October 14, 2024

# Storing student and classmate details in dictionaries
student = {
    "name": "Jerimie Dela Cruz",
    "address": "Municipality of Santiago, Ilocos Sur",
    "favNum1": 80,  
    "age": 22,  
    "allowance": float(500)  
}

classmate = {
    "name": "Michael John Macayan",
    "address": "City of Candon, Ilocos Sur",
    "favNum1": "69",  
    "age": 20,  
    "allowance": float(1000)  
}

# List to store the lengths of studentName and classmateName
name_lengths = [len(student["name"]), len(classmate["name"])]

# Function containing the IF...ELIF...ELSE logic from the original code
def check_location_and_name_length():
    # Check if both students are from Ilocos Sur
    if "Ilocos Sur" in student["address"] and "Ilocos Sur" in classmate["address"]:
        print(student["name"].upper() + " is from " + student["address"])
        print(classmate["name"].upper() + " is from " + classmate["address"])
    else:
        print(f"{student['name'].upper()} is not from Ilocos Sur")

    # Compare the lengths of their names
    if name_lengths[1] > name_lengths[0]:
        print(f"{classmate['name']} has a longer name than {student['name']} with {name_lengths[1]} letters over {name_lengths[0]} letters")
    else:
        print(f"{student['name']} has a longer name than {classmate['name']}")

    # Split names and check if any lives in Ilocos Sur
    sName_Split = student["name"].split(" ")
    cName_Split = classmate["name"].split(" ")

    if len(sName_Split) > 0 and len(cName_Split) > 0:
        print(f"One among {sName_Split[0]} or {cName_Split[0]} lives in Ilocos Sur")
    else:
        print("None of the students live in Ilocos Sur")

    # Print the sum of student and classmates ages
    print(f"The added age of {student['name']} and {classmate['name']} is {student['age'] + classmate['age']}")

    # Print the subtracted favorite numbers of Michael and Jerimie
    print(f"The subtracted value of favNum of {student['name']} and {classmate['name']} is {student['favNum1'] - int(classmate['favNum1'])}")

    # Calculate and print the combined weekly allowance
    combinedWeeklyAllowance = student['allowance'] + classmate['allowance']
    print(f"The weekly allowance of {student['name']} and {classmate['name']} is {combinedWeeklyAllowance:.2f} pesos")

# Calling the function at runtime
check_location_and_name_length()

# Create and extend a list with student and classmate names and addresses
classList = [student["name"], classmate["name"]]
classList_Ext = [student["address"], classmate["address"]]
classList.extend(classList_Ext)

# Print the classList items
for item in classList:
    print(item)

# Create a list of numerical variables and sort them
classNumbers = [student["age"], classmate["age"], student["favNum1"], int(classmate["favNum1"]), int(student["allowance"]), int(classmate["allowance"])]
classNumbers.sort(reverse=True)  # Reverse the sort

# Print sorted numerical variables
for number in classNumbers:
    print(number)

# Asking for user input for their name and passing it to quizTwo
user_name = input("Please enter your name: ")

# Define a function quizTwo to congratulate
def quizTwo(name):
    print(f"Congratulations on Quiz 2, {name}!")

# Call the function to congratulate
quizTwo(user_name)