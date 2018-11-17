#!/usr/bin/python
import os
import sys
from bash_functions import *

def main():
    while(True):
        working_directory=os.getcwd()
        text=raw_input(working_directory+"$")
        command=text.split(" ")
        if command[0]=="head":
            if len(command)!=2:
                print "command syntax:head filename"
            else:
                head(command[1])
                
        elif command[0]=="tail":
            if len(command)!=2:
                print "command syntax:tail filename"
            else:
                tail(command[1])
                
        elif command[0]=="sed":
            if len(command)!=3:
                print "command syntax:sed 's/<old>/<new>/' filename"
            else:
                sed(command[1],command[2])

                
        elif command[0]=="pwd":
            if len(command)==1:
                pwd()
            else:
                print "command syntax:pwd"
                
        elif command[0]=="cd":
            if len(command)!=2:
                print "command syntax:cd dir1/dir2/...."
            else:
                change_dir(command[1])
                
        elif command[0]=="touch":
            if len(command)!=2:
                print "command syntax:touch filename"
            else:
                touch(command[1])
                
        elif command[0]=="grep":
            if len(command)!=3:
                print "command syntax:grep pattern filename/string"
            else:
                grep(command[1],command[2])
                
        elif command[0]=="cls":
            if len(command)!=1:
                print "command syntax:cls"
            else:
                clear_screen()
                
                
        elif command[0]=="ls":
            if len(command)!=1:
                print "command syntax:ls"
            else:
                list_dir()
                
        elif command[0]=="tr":
            if len(command)!=5:
                print "command syntax:tr [:upper:]/[:lower:]  [:lower:]/[:upper:] < filename"
            else:
                if command[1]=="[:upper:]" or command[1]=="[:lower:]" or command[2]=="[:lower:]" or command[2]=="[:upper:]":
                    tr(command[1],command[2],command[4])
                else:
                    print "check syntax of command"

                    
        elif command[0]=="exit":
            if len(command)!=1:
                print "command syntax:exit"
            else:
                sys.exit()

                
        elif command[0]=="diff":
            if len(command)!=3:
                print "command syntax:diff file 1 file2"
            else:
                diff(command[1],command[2])

                
        elif command[0]=="exit":
            if len(command)!=1:
                print "syntax:exit"
            else:
                sys.exit()
        else:
            print "Invalid command"
        
if __name__=='__main__':
    main()
