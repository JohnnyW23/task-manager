from appModules.files import *
from appModules.objects import *
from time import sleep

try:
    file1 = 'To do list.txt'
    file2 = 'Tasks concluded.txt'
    fileExists(file1)
    fileExists(file2)

    print('''
\033[36mWelcome to the app!\033[m''')
    
    sleep(1)

    print('Loading...')

    sleep(1)

    optionsList = ['Add new task', 'Mark task as concluded', 'View current tasks',
                    'View concluded tasks', 'Delete current tasks', 'Delete concluded tasks',
                    'Instructions', 'Exit program']
    
    out = False

    while not out:

        sleep(1)

        option = appMenu(optionsList, 50, 35)

        while True:

            if option == 1:

                title(optionsList[0], 50, 33)
                task = taskValid(50)
                fileRegister(file1, task)
                break

            elif option == 2:
                title(optionsList[1], 50, 33)
                choice = fileMove(file1, file2)
                if choice:
                    lineDelete(file1, choice)
                break

            elif option == 3:
                title(optionsList[2], 50, 33)
                fileRead(file1)
                break

            elif option == 4:
                title(optionsList[3], 50, 33)
                fileRead(file2)
                break

            elif option == 5:
                title(optionsList[4], 50, 33)
                taskDelete(file1)
                break

            elif option == 6:
                title(optionsList[5], 50, 33)
                taskDelete(file2)
                break

            elif option == 7:
                instructions(50, 32)
                break

            elif option == 8:
                out = True
                break

            else:
                print(f'\033[31mThere is no {option} in the menu list!\033[m')
                option = readInt('\033[32mOption:\033[m ')

    exit(50, 33)

except KeyboardInterrupt:
    exit(50, 33)
