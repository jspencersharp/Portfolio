#part 1
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]


# for data in students:
#     print data['first_name'], data['last_name']


#part 2

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentNames(arr):
    for students in students:
        print students['first_name'], students['last_name']

def showUsers(users):
    for role in users:
        counter=0
        print role
        for person in users[role]:
            counter = counter +1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)

studentNames(students)
showUsers(users)



# can't get part two to work... have spent too much time on this but getting error that students in line 37 is referenced before assignment. 