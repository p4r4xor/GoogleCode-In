import threading
import zipfile
import sys
import optparse
from colorama import Fore
from colorama import Style
out=sys.stdout
n1=0
n2=0
def extractfile(zfile,password):
    global out,n1,n2
    n2+=1
    out.write(Fore.RED+"\r[+] Scanning(%s/%s)"%(n2,n1)+Style.RESET_ALL)

    out.flush()
    try:
        zfile.extractall(pwd=password)
        print "\nFound Password!: "+Fore.YELLOW+password+Style.RESET_ALL
        sys.exit(0)
    except Exception:
        pass
def main():
    parser=optparse.OptionParser('usage: %s [options]'%sys.argv[0])
    parser.add_option('-z',dest='zip_name',type='string',help="specify zip file")
    parser.add_option('-d',dest='dict_name',type='string',help="specify dictitonary file")
    options,argvs =parser.parse_args()
    if(options.dict_name==None):
        options.dict_name="d:/dict.txt"
    if(options.zip_name==None):
        print parser.usage
        sys.exit(0)
    elif(options.zip_name!=None):#crack
        #print options
        zip_name=options.zip_name
        print "Given Zip file: "+Fore.YELLOW+zip_name+Style.RESET_ALL
        dict_name=options.dict_name
        zfile=zipfile.ZipFile(zip_name)
        dfile=open(dict_name,'r')
        global n1
        lines=dfile.readlines()
        n1=len(lines)
        for line in lines:
            password=line.strip('\n')
            extractfile(zfile,password)
        try:
                for c in password_dict:
                    d_file.write(c+'\n')
        except:
            pass
        d_file.close()
        #print "[+]write dict file %s done!"%options.dict_name
if __name__=='__main__':
    main()