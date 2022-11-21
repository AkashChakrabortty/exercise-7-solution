# Akash Chakrabortty
# 12011192-A
# 6th semester
# Regular

village_school = {"name": "Boalia High School",
                  "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {
    "name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}

managing_committee_caniddates = [{"name": "Sultan Ahmed", "age": 43, "occupation": "Service Holder", "designation": "General Member"}, {"name": "Jamsed Khan", "age": 45, "occupation": "Doctor", "designation": "Vice Chairman"}, {
    "name": "Jahangir Talukder", "age": 47, "occupation": "Doctor", "designation": "Chairman"}, {"name": "Josim Uddin", "age": 38, "occupation": "Farmar", "designation": "Vice Chairman"}]

# 0)output the data type of village_school
print('data type of village_school', type(village_school))
# 1)output the name of the above school
print('name of the above school', village_school['name'])
# 2)try to access "number_of_rooms" key of that school without getting any error
print("number_of_roomskey without error ", "number_of_rooms" in village_school)
# 3)change that schools establishment year and make it 1962
village_school['established'] = '1962'
print('after change established', village_school)
# 4)add school_details to village_school
village_school.update(school_details)
print('after add school_details to village_school ', village_school)
# *** PLEASE REMEMBER THAT AFTER ADDING 'school_details' to 'village_school' all items of 'school_details' are now available in 'village_school' dictionary

# 5)check the length of village_school after adding school_details to it
print('check the length', len(village_school))
# 6)add number_of_classrooms key with value 25 in village_school dictionary
village_school['number_of_classrooms'] = 25
print('add number_of_classrooms key ', village_school)
# 7)check the data type of village_school
print('data type of village_school', type(village_school))
# 8)loop through all the values of village_school and check if any list type data found there if found print the key name
for i in village_school:
    if type(village_school[i]) == list:
        print(i)
# 9)output how many members are there in the managing committee
print('members ',  len(school_details['managing_committee']))
# 10)check if 'Founder of Toto Company' exist in the managing committee if found then remove that person from the managing committee
index = 0
for i in school_details['managing_committee']:
    if (i.get('occupation') == 'Founder of Toto Company'):
        school_details['managing_committee'].pop(index)
    index += 1
# 11)output all the members occupation of the managing committee to check "Founder of Toto Company" is not there
print('11 ', school_details['managing_committee'])
# # 12)remove the last added item from the village_school (remember we've a built in function for that)
village_school.popitem()
print('12 ', village_school)
# 13)remove the founder of that school
village_school.pop('founder')
print('13 ', village_school)
# 14)set default value for founder key to "Robiul Islam"
village_school.update({'founder': 'Robiul Islam'})
print('14 ', village_school)
# 15)check for a doctor in the 'managing_committee_candidates' list and make sure he wants to be the 'Vice Chairman' of that school if so then add that person to the managing_committe of that school
for i in managing_committee_caniddates:
    if (i.get('occupation') == 'Doctor' and i.get('designation') == 'Vice Chairman'):
        school_details["managing_committee"].append(i)
# 16)output the member of managing_committee after update
print('16 ', school_details["managing_committee"])
# 17)wipe out all the prperties of village_school and make it empty
village_school.clear()
print('17 ', village_school)
print('\n')

students1 = {"shaon", "sufian", "sohrab",
             "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}

a = {8, 4, 3, 3, 2, 7, 5}
b = {1, 4, 9, 20, 34}

# 1)check the data type of students
print('data type of students[1]', type(students1))
# 2)check the length of students
print('length of students1[2]', len(students1))
# 3)add "sweety" to students
students1.add("sweety")
print('3', students1)
# 4)remove "risat" from students
students1.remove("risat")
print('4', students1)
# 5)try to safely remove "raihan" from students without facing any error
students1.discard("raihan")
print('5', students1)
# 6)add students2 to students1
students1.update(students2)
print('6', students1)
# 7)check is students2 is the subset of student1
print('7', students2.issubset(students1))
# 8)check is students1 is the superset of student2
print('8', students1.issubset(students2))
# 9)clear student1
print('9', students1.clear())
students1 = {"shaon", "sufian", "sohrab",
             "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}

# 10)print all the combined items of student1 and student2, without any duplication (without making any permanent change)
students1.update(students2)
print('10', students1)
# 10)print all the combined items of student1 and student2, with all common values of them (without making any permanent change)
students1.intersection_update(students2)
print('10', students1)
# 10)print all the combined items of student1 and student2, with all uncommon values of them (without making any permanent change)
students1 = {"shaon", "sufian", "sohrab",
             "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}
students1.symmetric_difference_update(students2)
print(students1)
