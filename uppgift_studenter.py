data = {
    "studenter": [ ##Tuples
        ("Alice", {'ålder': 25, 'ämnen': ('matematik', 'fysik'), "aktiv": True}),
        ("Bob", {'ålder': 25, 'ämnen': ('biologi'), 'aktiv': False}),
        ("Charlie", {'ålder': 22, 'ämnen': ('matematik', 'biologi'), 'aktiv': True}),
        ("Diana", {'ålder': 24, 'ämnen': ('fysik'), 'aktiv': False}),
        ("Eve", {'ålder': 21, 'ämnen': ('matematik', 'fysik', 'biologi'), 'aktiv': True}),
    ],
    "kurser": {
        "matematik": {'studenter': {'Alice', 'Charlie', 'Eve'}},
        "fysik": {'studenter': {'Alice', 'Diana', 'Eve'}},
        "biologi": {'studenter': {'Bob', 'Charlie', 'Eve'}},
    }
}

active_students = []
for student in data['studenter']:
    name = student[0]
    details = student[1]
    if details['aktiv']:
        active_students.append(name)

active_students_tuple = tuple[active_students]
print(active_students)

active_subjects = set()

for student in data['studenter']:
    details = student[1]
    if details['aktiv']:
        subjects = details['ämnen']
        for subject in subjects:
            active_subjects.add(subject)

print(active_subjects)


active_per_course = {}
active_students_set = set(active_students)

for course_name, course_info in data['kurser'].items():
    course_students = course_info['studenter']
    active_in_course = course_students.intersection(active_students_set)
    active = len(active_in_course)
    active_per_course[course_name] = active

print(active_per_course)







# student1 = data["studenter"][0]
# student2 = data["studenter"][1]
# student3 = data["studenter"][2]
# student4 = data["studenter"][3]
# student5 = data["studenter"][4]

# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)