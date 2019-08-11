import os

try:
    boards = open('boards/BOARDS.txt').readlines()
    for board in boards:
        print('[+] Updating files for: '+board)
        board = board.replace('\n','')
        print('[+] Removing unnecessary files')
        for scrolledFile in ['todoScrolled.txt','busyScrolled.txt','doneScrolled.txt']:
            os.remove('boards/'+board+'/'+scrolledFile)

        print('[+] Writing new files')
        file = open('boards/'+board+'/lists.txt','w')
        file.write('Todo;0\nBusy;0\nDone;0\n')
        file.close()
        print()
        print()
        print('[+] Updating files for '+board+' completed.')
    input('[+] DONE')
except FileNotFoundError:
    input('[+] Your boards are already up to date.')


