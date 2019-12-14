import sys
import os
import datetime
import stat
import shlex
from colorama import init, Fore, Back, Style

MY_ARGS = ['h',  'nn',  'on', 'oan', 'dn', 'ra']
HELP = "h        : help\nnn       : new note\non       : open last note\non[no]   : open that note\noan      : open all notes\ndn       : delete note/notes\nra       : read all notes"
x = datetime.datetime.now()
DATE = str(x.day)+"-"+str(x.month)+"-"+str(x.year)
PATH = os.environ["ProgramW6432"] + str('/hanApp/')
EXT = '.hanknc'
if os.path.exists(PATH):
    path, dirs, FILES = next(os.walk(PATH, topdown=True))
NOTES = []
DONE_NOTES = []


def getNotes():
    for file in FILES:
        if file.endswith('.hanknc'):
            NOTES.append(file)
        elif file.endswith('.hanknc-Done'):
            DONE_NOTES.append(file)


def createfile(control):

    cmdline = " ".join(map(shlex.quote, sys.argv[2:]))
    file = DATE
    notenumber = 1

    while os.path.exists(PATH+file+EXT):

        file = file+'-'+str(notenumber)
        notenumber = notenumber+1
    try:
        file = open(PATH+file+EXT, 'w')
        if control:
            file.write(input(Fore.RED + 'give me a note 📝 : \n'))
            print(Fore.GREEN + 'I took note ✔️ \n')
        else:
            file.write(cmdline)
            print(Fore.GREEN + 'I took note ✔️ \n')
    except:
        print(Fore.RED + 'houston we have a problem 😔\n')


def createfolder():
    try:
        os.mkdir(PATH)

    except OSError:
        pass
    else:
        print(
            Fore.GREEN + "Successfully created the directory for first use 🚀\n %s " % PATH)


def openfile(fileno):
    if fileno is not None:
        if len(NOTES) > int(fileno):
            file = open(PATH+os.listdir(PATH)[int(fileno)-1])
            print(file.read())
    elif len(NOTES) > 0:
        file = open(PATH+os.listdir(PATH)[0])
        print(file.read())
    else:
        print(Fore.BLUE + 'No Note 🔎')


def openAllNotes():
    index = 1
    for file in FILES:
        if file.endswith('.hanknc'):
            print('📋 : ', file, '👉 : ', index)
            index = index+1
    if index == 1:
        print(Fore.RED + 'No Notes 🔎')
    else:
        print(Fore.BLUE + 'All notes here 🔥')


def deleteNote(noteIndex):

    if noteIndex is None and len(FILES) > 1:
        for file in FILES:
            os.remove(PATH+file)
            print(Fore.GREEN + 'All Notes Deleted 😨')
    elif len(FILES) > 1:
        os.remove(PATH+os.listdir(PATH)[int(noteIndex)-1])
        print(Fore.RED + 'Note Deleted ❌')
    else:
        print(Fore.GREEN + 'no such note or no note 🤷‍♂️. ')


'''def MarkasDone(noteIndex):
   
    if len(FILES) > 1:
        os.rename(PATH+os.listdir(PATH)[int(noteIndex)-1],PATH+os.listdir(PATH)[int(noteIndex)-1]+'-Done')
        print(' ✔️ ✔️ Mark as Done, Well Done Boy ! ✔️ ✔️ ')
    else:
        print('no such note or no note 🤷‍♂️. ')'''


def ReadAllNotes():
    index = 1
    for file in FILES:

        print(Fore.GREEN, index, '. note : \n', open(PATH+file).read(), '\n')
        index = index+1


def help():
    print(Fore.GREEN + HELP)


def selector(arg):
    if arg == 'h':
        help()
    if arg == 'nn':
        if len(sys.argv) > 2:
            createfile(False)
        else:
            createfolder()
            createfile(True)
    if arg == 'on':
        if len(sys.argv) > 2:
            openfile(sys.argv[2])
        else:
            openfile(None)
    if arg == 'oan':
        openAllNotes()
    if arg == 'dn':
        if len(sys.argv) > 2:
            deleteNote(sys.argv[2])
        else:
            print(Fore.BLUE +
                  'please give me a note number 😨 or I will delete them all 😈')
            result = input(
                'give note number to delete, type "e" to delete all, type "q" to exit\n')
            if result == 'e':
                deleteNote(None)
            elif result.isdigit():
                deleteNote(result)
            else:
                exit
    '''if arg == 'mad':
        if len(sys.argv) > 2:
            MarkasDone(sys.argv[2])
        else:
            openfile(None)'''
    if arg == 'ra':
        ReadAllNotes()


def main():
    if os.path.exists(PATH):
        init()
        if len(sys.argv) > 1:
            if sys.argv[1] in MY_ARGS:
                getNotes()
                selector(sys.argv[1])
            else:
                print(Fore.GREEN + 'Wrong parameter 😩 , type "h" for help \n')
        else:
            print(Fore.GREEN + 'Wrong parameter 😩 , type "h" for help \n')
    else:
        createfolder()


if __name__ == "__main__":
    main()
