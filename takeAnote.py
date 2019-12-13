import sys
import os
import datetime
import stat
MY_ARGS = ['h',  'nn',  'on', 'oan', 'mad', 'mada']
HELP = "h        : help\nnn       : new note\non       : open all notes\non[no]   : open that note\nmad      : mark as done all \nmad [no] : mark as done"
x = datetime.datetime.now()
DATE = str(x.day)+"-"+str(x.month)+"-"+str(x.year)
PATH = os.getcwd() + str('/hanApp/')
EXT = '.hanknc'
path, dirs, FILES = next(os.walk(PATH))


def createfile():
    file = DATE
    notenumber = 1
    print(PATH+file+EXT)
    print(os.path.exists(PATH+file+EXT))
    while os.path.exists(PATH+file+EXT):

        file = file+'-'+str(notenumber)
        notenumber = notenumber+1
    try:
        file = open(PATH+file+EXT, 'w')
        file.write(input('give me a note 📝 : \n'))
        print('I took note ✔️ \n')
    except:
        print('houston we have a problem 😔\n')


def createfolder():
    try:
        os.mkdir(PATH)
    except OSError:
        pass
    else:
        print("Successfully created the directory for first use 🚀\n %s " % PATH)


def openfile(fileno):
    if fileno is not None:
        file = open(PATH+os.listdir(PATH)[int(fileno)-1])
        print(file.read())
    else:
        file = open(PATH+os.listdir(PATH)[0])
        print(file.read())


def openAllNotes():

    index = 1
    for file in FILES:
        print('📋 : ', file, '👉 : ', index)
        index = index+1
    if index == 1:
        print('No Notes 🔎')
    else:
        print('All notes here 🔥')


def deleteNote(noteIndex):

    if noteIndex is None and len(FILES) > 1:
        for file in FILES:
            os.remove(PATH+file)
            print('All Notes Deleted 😨')
    elif len(FILES) > 1:
        os.remove(PATH+os.listdir(PATH)[int(noteIndex)-1])
        print('Note Deleted ❌')
    else:
        print('no such note or no note 🤷‍♂️. ')


def MarkasDone(fileIndex):
    pass


def ReadAllNotes:
    pass


def help():
    print(HELP)


def selector(arg):
    if arg == 'h':
        help()
    if arg == 'nn':
        createfolder()
        createfile()
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
            print('please give me a note number 😨 or I will delete them all 😈')
            result = input(
                'give note number to delete, type "e" to delete all, type "q" to exit\n')

            if result == 'e':
                deleteNote(None)
            elif result.isdigit():
                deleteNote(result)
            else:
                exit
    if arg == 'mad':
        if len(sys.argv) > 2:
            MarkasDone(sys.argv[2])
        else:
            openfile(None)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in MY_ARGS:
            selector(sys.argv[1])
        else:
            print('Wrong parameter 😩 , type "h" for help \n')
    else:
        print('Wrong parameter 😩 , type "h" for help \n')


if __name__ == "__main__":
    main()
