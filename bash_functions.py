import os
import time
import string
import difflib
from stat import *

def touch( file_path ):
    if file_path.find("/")==-1:
        f_path=os.getcwd()+"/"+file_path
        if os.path.exists(f_path):
            a_time=time.time()
            m_time=time.time()
            os.utime(f_path,(a_time,m_time))
        else:
            open(f_path,'w')
    else:
        if file_path[0]=="/":
           if os.path.exists(file_path):
               a_time=time.time()
               m_time=time.time()
               os.utime(f_path,(a_time,m_time))
           else:
               list=file_path.split("/")
               file_name=list[len(list)-1]
               list.remove(list[len(list)-1])
               new_path='/'.join(list)
               if os.path.exists(new_path):
                   open(new_path+"/"+file_name,'w')
               else:
                   print "Cannot touch file,No such file or Directory"
        else:
            new_path=os.getcwd()+"/"+file_path
            if os.path.exists(new_path):
                a_time=time.time()
                m_time=time.time()
                os.utime(new_path,(a_time,m_time))
            else:
                file_dir=file_path.split("/")
                file_name=file_dir[len(file_dir)-1]
                file_dir.remove(file_dir[len(file_dir)-1])
                temp='/'.join(file_dir)
                if os.path.exists(os.getcwd()+"/"+temp):
                    open(os.getcwd()+"/"+temp+"/"+file_name,'w')
                else:
                    print "Cannot touch file,No such file or directory"
            

def head(file_path):
    if file_path.find("/")!=-1:
        if file_path[0]=="/":
            if os.path.exists(file_path):
                 f=open(file_path)
                 for i in range(10):
                     line=f.readline()
                     print line,
                     if(""==line):
                         break
                 f.close()
            else:
                print "No such file exists"
        else:
            new_path=os.getcwd()+"/"+file_path
            if os.path.exists(new_path):
                f=open(file_path)
                for i in range(10):
                    line=f.readline()
                    print line,
                    if(""==line):
                        break
                f.close()
            else:
                print "No such file exists"
    else:
        new_path=os.getcwd()+"/"+file_path
        if os.path.exists(new_path):
            f=open(new_path)
            for i in range(10):
                line=f.readline()
                print line,
                if(""==line):
                    break
            f.close()
        else:
            print "No such file exists"


def tail(file_path):
    if file_path.find("/")!=-1:
        if file_path[0]=="/":
            if os.path.exists(file_path):
                read_from_tail(file_path,10)
            else:
                print "No such file exists"
        else:
            new_path=os.getcwd()+"/"+file_path
            if os.path.exists(new_path):
                read_from_tail(new_path,10)
            else:
                print "No such file exists"
    else:
        new_path=os.getcwd()+"/"+file_path
        if os.path.exists(new_path):
            read_from_tail(new_path,10)
        else:
            print "No such file exists"

def read_from_tail(fname,lines):
    with open(fname) as f:
        lines=f.readlines()
        list_size=len(lines)
        if list_size < 10 :
            for a in lines:
                print a,
        else:
            list_ten=lines[-10:]
            for a in list_ten:
                print a,

                
def grep(pattern,g_path):
    if g_path[0]=="\"":
        grep_string(pattern,g_path)
    else:
        if g_path.find("/")==-1:
            if os.path.exists(os.getcwd()+"/"+g_path):
                grep_file(os.getcwd()+"/"+g_path,pattern)
            else:
                print "No such file exists"
        else:
            if g_path[0]=="/":
                if os.path.exists(g_path):
                    grep_file(g_path,pattern)
                else:
                    print "No such file exists"
            else:
                new_path=os.getcwd()+"/"+g_path
                if os.path.exists(new_path):
                    grep_file(new_path,pattern)
                else:
                    print "No such file exists"


def grep_string(pattern,str):
    str = str[1:-1]
    if str.find(pattern)!=-1:
        print str
        
def grep_file(file_path,pattern):
    with open(file_path) as file: # Use file to refer to the file object
        lines = file.readlines()
        for l in lines:
            if l.find(pattern)!=-1:
                print l,

def sed(command,path_name):
    command=command[1:-1]
    list=command.split("/")
    
    print list
    if len(list)==4 and list[0]=="s":
         if path_name.find("/")==-1:
            if os.path.exists(os.getcwd()+"/"+path_name):
                sed_helper(os.getcwd()+"/"+path_name,list[1],list[2])
            else:
                print "No such file exists"
         else:
            if path_name[0]=="/":
                if os.path.exists(path_name):
                    sed_helper(path_name,list[1],lsit[2])
                else:
                    print "No such file exists"
            else:
                new_path=os.getcwd()+"/"+path_name
                if os.path.exists(new_path):
                    sed_helper(new_path,list[1],list[2])
                else:
                    print "No such file exists"
    else:
        print "please refer to syntaxt of sed command"


        
def sed_helper(path_name,old_word,new_word):
     f = open(path_name,'r')
     filedata = f.read()
     f.close()
     newdata = filedata.replace(old_word,new_word)
     f = open(path_name,'w')
     f.write(newdata)
     f.close()
    

def tr(first,second,file_path):
    if file_path.find("/")==-1:
        if os.path.exists(os.getcwd()+"/"+file_path):
            tr_helper(second,os.getcwd()+"/"+file_path)
        else:
            print "No such file exists"
    else:
        if file_path[0]=="/":
            if os.path.exists(file_path):
                tr_helper(second,file_path)
            else:
                print "No such file exists"
        else:
            new_path=os.getcwd()+"/"+file_path
            if os.path.exists(new_path):
                 tr_helper(second,new_path)
            else:
                print "No such file exists"

def tr_helper(prop,file_path):
    myfile=open(file_path, 'r')
    data=myfile.read()
    myfile.close()
    str=""
    if prop=="[:lower:]":
        for c in data:
            if c in string.ascii_uppercase:
                str+=c.lower()
            else:
                str+=c
    else:
        for c in data:
            if c in string.ascii_lowercase:
                str+=c.upper()
            else:
                str+=c
    f=open(file_path,'w')
    f.write(str)
    f.close()
                    

                
                
def list_dir():
    path=os.getcwd();
    files = os.listdir(path)
    for name in files:
        print name

        
def change_dir(change_path):     
    if change_path!=".":
        try:
            os.chdir(change_path) 
        except OSError:
            print "No such path"

def pwd():
    print os.getcwd()

def clear_screen():
    print "\n"*100


def diff(file_name1,filename2):
    if file_name1[0]=="/" and filename2[0]=="/":
        if os.path.exists(file_name1) and os.path.exists(filename2):
            diff_helper(file_name1,filename2)
        else:
            print "No such file exists"
    else:
        print "Provide absolute path of files"
                
def diff_helper(file1,file2):
    f=open(file1,'r')
    f1=open(file2,'r') 
    str1=f.read()
    str2=f1.read()
    str1=str1.split() 
    str2=str2.split()
    d=difflib.Differ()
    diff=list(d.compare(str2,str1))
    print '\n'.join(diff)
                
