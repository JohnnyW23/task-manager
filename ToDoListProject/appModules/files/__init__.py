def fileCreate(name):
	try:
		a = open(name, 'wt+')
		a.close()
	except:
		print('\033[31mERROR: Could not create new file.\033[m')
	else:
		print(f'\033[37mFile \033[33m{name}\033[37m created with success!\033[m')


def fileExists(name):
	try:
		a = open(name, 'rt')
		a.close()
	except FileNotFoundError:
		fileCreate(name)
	else:
		return True
	

def fileLineRead(name, line):
    with open(name, 'r') as file:
        for i, l in enumerate(file, 1):
            if i == line:
                return l


def lineDelete(name, choice):
    try:
        with open(name, 'r+') as file:
            lines = file.readlines()
            del lines[choice - 1]
            file.seek(0)
            file.truncate()
            file.writelines(lines)
    except FileNotFoundError:
        print(f'\033[31mFile "{name}" not found.\033[m')


def fileRead(name):
    from os.path import getsize

    try:
        a = open(name, 'rt')
    except:
        print('\033[31mERROR: Could not read file.\033[m')
    else:
        if getsize(name) == 0:
            print(f'\033[32m<No tasks registered in \033[33m"{name}"\033[32m>\033[m')
        else:
            lines = len(a.readlines())
            for l in range(1, lines + 1):
                task = fileLineRead(name, l)
                print(f'\033[31m{l}\033[m - {task}', end='')
    finally:
        a.close()


def fileRegister(name, task):
	try:
		a = open(name, 'at')
	except:
		print('\033[31mERROR: Could not open file.\033[m')
	else:
		try:
			a.write(f'{task}\n')
		except:
			print('There was an ERROR in data register.')
		else:
			print('\033[33mNew task added in your To Do List!\033[m')
			a.close()


def fileMove(name, name2):
    from ..objects import readInt
    from os.path import getsize
    from time import sleep

    with open(name, 'r+') as a:
        lines = a.readlines()
        if getsize(name) == 0:
            print(f'There are no tasks to be marked as completed (\033[33m"{name}"\033[m is empty)')
            register = False
            return register
        else:
            while True:
                choice = readInt('Which task do you want to mark as completed?\n[0] to interrupt\n')
                if choice == 0:
                    print('\033[33mOperation interrupted!\033[m')
                    a.close()
                    register = False
                    return register
                elif 1 <= choice <= len(lines):
                    transfer = lines.pop(choice - 1)
                    with open(name2, 'a') as b:
                        b.write(transfer)
                        print(f'Task \033[33m{choice}\033[m is done!')
                        sleep(1)
                    return choice
                else:
                    print('\033[31mChoose a valid option.\033[m')


def taskDelete(name):
    from ..objects import readInt
    from os.path import getsize

    with open(name, 'r+') as a:
        lines = a.readlines()
        if getsize(name) == 0:
            print(f'There are no tasks to delete (\033[33m"{name}"\033[m is empty)')
        else:
            while True:
                try:
                    choice = readInt(f'Which current task do you want to delete from \033[33m"{name}"\033[m?\n[0] to interrupt\n[999] to erase list\n')
                    if choice == 0:
                        print('\033[33mOperation interrupted!\033[m')
                        break
                    elif choice == 999:
                        while True:
                            dec = input(f'Are you sure you want to erase \033[33m"{name}"\033[m\n[Y/N]: ').upper().strip()
                            if dec == 'N':
                                print(f'\033[33m"{name}"\033[m not erased. Redirecting to main menu...')
                                break
                            elif dec == 'Y':
                                a.seek(0)
                                a.truncate()
                                print(f'\033[33m"{name}"\033[m erased with success!')
                                break
                            else:
                                print('\033[31mChoose a valid answer.\033[m')
                        break
                    elif 1 <= choice <= len(lines):
                        lineDelete(name, choice)
                        print(f'Task \033[33m{choice}\033[m deleted with success!')
                        break
                    else:
                        print('\033[31mChoose a valid option!\033[m')
                except IndexError:
                    print('\033[31mChoose a valid task index.\033[m')
