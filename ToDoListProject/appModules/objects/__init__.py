def readInt(msg):
	while True:
		try:
			n = int(input(msg))
			return n
		
		except (ValueError, TypeError):
			print('\033[31mERROR! Please, type a valid INTEGER number.\033[m')
			
		except KeyboardInterrupt:
			print('\n\033[31mUser preferred to not type any number.\033[m')
			break


def lin(len=30):
	print('–' * len)


def title(txt, len=30, color=0):
	from time import sleep

	lin(len)
	print(f'\033[{color}m{str(txt.strip()).center(len)}\033[m')
	lin(len)
	sleep(1)


def appMenu(list, len=30, color=0):
	print()
	title('TO DO LIST APPLICATION v1.0', len, color)
	c = 1
	
	for item in list:
		print(f'\033[33m{c}\033[m – \033[36m{item}\033[m')
		c += 1
		
	lin(len)
	opc = readInt('\033[32mOption: \033[m')
	return opc


def taskValid(length=60):
	while True:
		task = input('Type a task to be registered:\n')
		if len(task) > length:
			print('\033[31mYour entry must have a max limit of 50 characters!\033[m')
		else:
			return task


def instructions(len=30, color=0):
    from time import sleep

    title('Instructions', len, color)
    print('\033[33m', end='')
    print('WELCOME TO THE "TO DO LIST APPLICATION v1.0"!'.center(50))
    print('\033[m', end='')
    print('''
Created by: \033[36mDavi Nascimento\033[m
            February 2024
''')
	
    sleep(0.5)

    print('''->  The user must choose an option from the menu to
    execute one of the commands below.
''')

    sleep(0.5)
	
    print('''1 - ADD NEW TASK:
    User adds a new task in your to do list. The
    entry for registering the task must have a
    max limit of 50 characters. The new task is 
    stored in a file text named "To do list.txt".
''')

    sleep(0.5)
	
    print('''2 - MARK TASK AS CONCLUDED:
    User chooses one of the current tasks to be
    marked as a concluded task. The task is
    transfered from the file "To do list.txt" to
    the file "Tasks concluded.txt". If user don't
    wish to mark any task, typing "0" will
    interrup the operation.
''')

    sleep(0.5)
	
    print('''3 - VIEW CURRENT TASKS:
    The interface displays the content of "To do
    list" to the user. If the list is empty, the
    interface displays a message warning that
    there are no tasks registered in the list.
''')

    sleep(0.5)
	
    print('''4 - VIEW CONCLUDED TASKS:
    The interface displays the list of all
    concluded tasks to the user. If list is
    empty, the interface displays a message
    warning that there are no concluded tasks
    registered in the list.
''')

    sleep(0.5)
	
    print('''5 - DELETE CURRENT TASKS:
    User chooses one of the current tasks to be
    deleted from "To do list.txt". If user don't
    wish to delete any task, typing "0" will
    interrupt the operation. If user wishes to
    erase the list, just type "999". If list is
    empty, the interface displays a message
    warning that there are no tasks registered in
    the list.
''')

    sleep(0.5)
	
    print('''6 - DELETE CONCLUDED TASKS:
    User chooses one of the concluded tasks to be
    deleted from "Tasks concluded.txt". If user
    don't wish to delete any task, typing "0"
    will interrupt the operation. If user wishes
    to erase the list, just type "999". If list
    is empty, the interface displays a message
    warning that there are no tasks registered in
    the list.
''')

    sleep(0.5)
	
    print('''7 - INSTRUCTIONS:
    Displays the current menu with instructions
    about all the commands in the application.
''')

    sleep(0.5)
	
    print('''8 - EXIT PROGRAM:
    Exits the application and shuts down the
    program.''')


def exit(len=30, color=0):
	from time import sleep

	title('Exiting program...', len, color)
	sleep(1)
	print('\033[36mThank you and come back!\033[m')
	print()
