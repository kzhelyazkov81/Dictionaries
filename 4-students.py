students_dict = {}
command = input()

while ':' in command:
    info = command.split(':')
    name = info[0]
    id = info[1]
    course = info[2]
    if course not in students_dict.keys():
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()

course = ' '.join(command.split('_'))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')

