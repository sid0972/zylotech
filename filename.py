def read_contents():
    fileNameConcat = []
    contentsConcat = []
    no_of_files = raw_input("Enter the number of files? \n")
    for i in range(0, int(no_of_files)):
        fn = raw_input("Enter filename\n")
        fileNameConcat.append(fn)
        contents = raw_input("enter contents\n")
        contentsConcat.append(contents)
        pass

    print fileNameConcat[0].split('.')[0] + fileNameConcat[1]
    for elem in contentsConcat:
        print elem.replace("$","")


if __name__ == '__main__':
    read_contents()
