def main(argv):
    try:
        directory = argv[1]
        if (os.path.exists(directory) == False):exit()
        if (os.path.isfile(directory) == True):exit()
       
    except:
        print("usage: " + argv[0] + " <directory>")
        return 0
    
    if (directory[-1:] != "/"):
        directory += "/"
    
    for i in os.listdir(directory):
        if (os.path.isdir(directory+i) == True):continue
        name , ext = os.path.splitext(directory+i)
        try:
            os.mkdir(directory+ext[1:])
        except:
            pass
        current = directory+i
        to = directory+ext[1:]+"/"+i
        os.rename(current,to)


if __name__ == "__main__":
    
    import os
    import sys

    main(sys.argv)
