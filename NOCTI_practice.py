"""
This program reads a file of people and their date of birth
"""

#initializes variables
people = []
age_total = 0
people_count = 0
current_year = 2026
current_month = 3

with open("records1.txt","r") as file:
          people = file.readlines()

for person in people:
    person.strip()
    print(person)
    temp = person.split(",")
    temp = temp[1].strip()
    temp = temp.split("-")
    year = temp[0]
    year = int(year)
    people_count +=1
    #finds their age
    age = current_year - year
    age_total = age + age_total

average_age = age_total/people_count
print("Number of people: ", people_count, "The average age:", average_age)





  
