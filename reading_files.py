ourVariable = open(filename, mode)

#r    read mode
#w    write mode (creates a new file and overwrites an existing file)
#x    write mode (only for new files)
#a    append mode (creates a new file or adds content to the end of an existing file)
#available options are: rt, rb, wt, wb, xt, xb, at, and ab
#functions read(), readline(), and readlines() 
#finished? close the file ourVariable.close() 

myFile = open(‘sfoglitelle’, ‘wt’)
myFile.write(secretRecipe)
myFile.close()

#Sample paths from book:
#c:\folder1\filename.txt (MS-DOS disk path)
#/tmp/filename.txt (Unix-style disk path)
#\\COMPUTERNAME\folder\filename.txt (WINS network path)
#http://www.codio.com/filename.txt (a URL for a file on the web)
#ftp://user1@pass1:ftp.foo.com/folder1/filename.txt (a URL for an FTP address)
import sys

pathA= 'content/textfiles/parrot.txt'
pathB= 'content/textfiles/empty.txt'
pathC= 'content/textfiles/cheese.txt'

fileA= open(pathA, 'r')                # open file 1
fileB= open(pathB, 'r')                # open file 2

fd1= fileA.fileno()                    # get file descriptor 1
fd2= fileB.fileno()                    # get file descriptor 2

print ('File Descriptor A: '+str(fd1)) # print the fd number
print ('File Descriptor B: '+str(fd2)) # print the fd number

fileA.close()                          # close file 1, freeing fd1
print ('Closed FD A ['+str(fd1)+'].')

fileC= open(pathC, 'r')                # open file 3
fd3= fileC.fileno()                    # get file descriptor 3
print ('File Descriptor C: '+str(fd3)) # print the fd number

fileB.close()                          # close the file
fileC.close()                          # close the file