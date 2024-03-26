'''
while True:
        try:
            n = int(input("Please enter an integer:"))
            m = int(input("Please enter an integer:"))
            z = n / m
            break
        except Exception as e:
            print("Not an integer!Please again 123")
            print(e)
        except ValueError:
            print("Not zn integer! Please again 456")
        finally:
            print("You successsfully entered an integer!")
'''


try:
    klu1 = open("file.txt","w+")
    try:
        klu1.write("xyzThis is S17 Section CRT Class")
    finally:
        klu1.close()
except IOError:
    print("File not Found")
else:
    print("The file opened successfully")
    klu1.close()
