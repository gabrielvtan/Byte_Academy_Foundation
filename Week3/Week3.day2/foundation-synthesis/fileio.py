import re
#INPUT FUNCTION
#While Input for first name is not done:
#Get first name, last, job, and salary
#Return List of instructors as each element being a string 
def get_input():
    instructor_list = []
    first = 0
    while first != "done":
        instructor_info = []
        first = input("First name: \n")
        if first == "done":
            break
        else:
            instructor_info.append(first)
            last = input("Last name: \n")
            instructor_info.append(last)
            job = input("Job: \n")
            instructor_info.append(job)
            salary = '${:.2f}'.format(float(input("Salary: \n")))
            instructor_info.append(salary)
            instructor_list.append(instructor_info)
    return (instructor_list)

# Write a file with each record as each line
# instructor_list = get_input()
def write_file(filename, instructor_list):
    with open(filename, 'w') as file_object:
        for line in instructor_list:
            record = '"{:<12}" "{:<12}" "{:<20}" {:<12}'.format(line[0],line[1],line[2],line[3])
            print(record, file = file_object)

write_file('instructors.txt',get_input())

def write_back_to_list(filename):   
    instructor_list = []
    with open(filename,'r') as file_object:
        pattern = '[\w.$]+[\s\w]+(?<!\n)'
        for line in file_object:
            result = re.findall(pattern,line)
            instructor_list.append(result)
    return instructor_list

#OUTPUT FUNCTION
#instructor_list = (write_back_to_list('instructors.txt'))
def output(instructor_list):
    boarder = "+------------+------------+--------------------+------------+"
    header = "| First Name | Last Name  | Job Title          | Salary     |"
    print(boarder)
    print(header)
    print(boarder)
    for instructor in range(len(instructor_list)):
        print("|{}|{}|{}|{}|".format(instructor_list[instructor][0],instructor_list[instructor][1],instructor_list[instructor][2],instructor_list[instructor][3]))
    print(boarder)
    

output(write_back_to_list('instructors.txt'))

    