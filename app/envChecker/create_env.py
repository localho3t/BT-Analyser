

def create():
    f = open(".env", 'w+')
    f.write("File_PATH=\n")
    f.write("#=============\n")
    f.write("DB_User=\n")
    f.write("DB_Pass=\n")
    f.write("DB_Host=\n")
    f.write("#=============\n")
    f.write("Delay=30\n")
    f.close()
