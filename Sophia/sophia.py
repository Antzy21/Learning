import time
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def display(wait = 0,
            text = '',
            AEyes=' OO',
            SEyes='oo ',
            Amouth=' u ',
            Smouth=' u ',
            ArArm = ' __',
            AlArm = '__ ',
            SrArm = ' __',
            SlArm = '__ ',
            distance = 5):
    max_distance = 5
    clear()

    pic='''
        '''+(max_distance-distance)*' '+'  ___   '+2*distance*' '+'.===.'+'''
        '''+(max_distance-distance)*' '+' /'+AEyes+'\\'+2*distance*' '+' //'+SEyes+'\\\\'+'''
        '''+(max_distance-distance)*' '+' \\'+Amouth+'/'+2*distance*' '+'/^\\'+Smouth+'/^\\'+'''
        '''+(max_distance-distance)*' '+ArArm+'|'+AlArm+2*distance*' '+SrArm+'|'+SlArm+'''
        '''+(max_distance-distance)*' '+'   |   '+2*distance*' '+'   |'+'''
        '''+(max_distance-distance)*' '+'  / \\ '+2*distance*' '+'   /_\\'+'''
        '''+(max_distance-distance)*' '+' /   \\'+2*distance*' '+'  /   \\'
    print(pic)
    print(text)

    if wait > 0:
        time.sleep(wait)

def blink(repeats = 2, text = ''):
    display(1.5, text)
    for x in range(repeats):
        display(.2, text, AEyes=' --')
        display(1.5, text)
        display(.2, text, SEyes='-- ')
        display(1.5, text)

def wink():
    display(2)
    display(2, AEyes=' O-')
    display(2, AEyes=' O-', SEyes = 'OO ', Smouth=' O ')
    display(2, SEyes = '^^ ', Smouth=' U ')

def hug():
    for x in reversed(range(5)):
        display(.2, distance=x)
    display(.5, AlArm = '___', ArArm = '   ', SrArm = '___', SlArm = '   ', distance=x)
    display(2, AEyes=' ^^', SEyes='^^ ', Amouth=' U ', Smouth=' U ', AlArm = '___', ArArm = '   ', SrArm = '___', SlArm = '   ', distance=x)
    display(.5, AlArm = '___', ArArm = '   ', SrArm = '___', SlArm = '   ', distance=x)
    for x in range(5):
        display(.2, distance=x)

def kiss():
    display(2)
    display(2, Smouth='*  ')
    display(1)
    display(2, Amouth="*.*")
    display(1, Amouth=" U ")
    display(2, Amouth='  *')
    display(2, AEyes = ' ^^', Amouth=' U ', SEyes = '^^ ', Smouth=' U ')
    display()

def wave(repeats=3):
    display(2)
    for x in range(repeats):
        display(.5, SrArm = ' \\_', Amouth=' U ')
        display(.5, SrArm = ' /_', Amouth=' U ')
    display(1, Amouth=' U ', Smouth=' U ')
    for x in range(repeats):
        display(.5, ArArm = ' \\_', Amouth=' U ', Smouth=' U ')
        display(.5, ArArm = ' /_', Amouth=' U ', Smouth=' U ')
    display(1, Amouth=' U ', Smouth=' U ')

def dance(repeats=7):
    for x in range(repeats):
        display(.5, SrArm = ' \\_', ArArm = ' \\_', SlArm = '_\\', AlArm = '_\\ ')
        display(.5, SrArm = ' /_', ArArm = ' /_', SlArm = '_/ ', AlArm = '_/ ')

def god_mode():
    i = 0

    clear()
    display()

    AEyes=' OO'
    SEyes='oo '
    Amouth=' u '
    Smouth=' u '
    ArArm = ' __'
    AlArm = '__ '
    SrArm = ' __'
    SlArm = '__ '
    distance = 5

    choices = ''' 1: Anthony's eyes
 2: Sophia's eyes
 3: Anthony's mouth
 4: Sophia's mouth
 5: Anthony's left arm
 6: Anthony's right arm
 7: Sophia's left arm
 8: Sophia's right arm
 9: Distance between each other

 0: Exit God Mode'''

    while True:
        clear()
        display(0, '', AEyes, SEyes, Amouth, Smouth, ArArm, AlArm, SrArm, SlArm, distance)

        print(' Welcome to God Mode! Here you can customise what we look like!\n')
        print(choices)
        print('\n It is recommended to keep each part 3 characters long.')
        i = input(' What to customise? ')

        if i == '1':
            AEyes = input(" Anthony's eyes:")
        elif i == '2':
            SEyes = input(" Sophia's eyes:")
        elif i == '3':
            Amouth = input(" Anthony's mouth:")
        elif i == '4':
            Smouth = input(" Sophia's mouth:")
        elif i == '5':
            AlArm = input(" Anthony's left arm:")
        elif i == '6':
            ArArm = input(" Anthony's right arm:")
        elif i == '7':
            SlArm = input(" Sophia's left arm:")
        elif i == '8':
            SrArm = input(" Sophia's right arm:")
        elif i == '9':
            try:
                distance = int(input(" Distance between eachother:"))
                if distance <=0:
                    distance = 0
                    print(' The distance must be a positive number!')
            except:
                distance = 5
                print(' The distance must be a positive number!')
        elif i == '0':
            break
        else:
            print('\n Oops! Please enter a valid number. Try again once this message is gone.\n')
            time.sleep(3)

def play():

    play = True
    points = 0
    t = '\n         Meet Anthony and Sophia!'
    blink(text = t)

    i = 1
    while play == True:
        if points >= 10:
            G_mode = ' \n 6: God Mode'
        else:
            G_mode = ''

        clear()
        display()

        choices = ' 1: Wave \n 2: Dance \n 3: Hug \n 4: Wink \n 5: Kiss '+G_mode+'\n \n 0: Exit'
        print(choices)
        i = input('\n What to do? ')
        if i == '1':
            wave()
            points += 1
        elif i == '2':
            dance()
            points += 1
        elif i == '3':
            hug()
            points += 1
        elif i == '4':
            wink()
            points += 1
        elif i == '5':
            kiss()
            points += 1
        elif i == '6' and points >= 5:
            god_mode()
        elif i == '0':
            if points >= 5:
                e = input('\n Warning! Once you exit you will loose access to God Mode, and you must earn it again next time\n Continue with exit? (Y/N): ')
                if e == 'Y':
                    play = False
            else:
                play = False
        else:
            print('\n Oops! Please enter a valid number. Try again once this message is gone.\n')
            time.sleep(3)

play()
