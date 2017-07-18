def lowerUpper():
    no_of_files = raw_input("Enter number of lines\n")
    for i in range (0, int(no_of_files)):
        lines = []
        line = raw_input("enter line\n")
        val = list(line)[-2 :][0]
        if (int(val) % 2 == 0):
            print (line.upper().split('.')[0][1:-1])
        else:
            print (line.lower().split('.')[0][1:-1])
        pass

if __name__=='__main__':
    lowerUpper()
