

def create(DB_Host, DB_User, DB_Pass, Delay, File_PATH, DB_Name):
    f = open(".env", 'w+')
    f.write(f"File_PATH={File_PATH}\n")
    f.write("#=============\n")
    f.write(f"Delay={Delay}\n")
    f.write("#=============\n")
    f.write(f"DB_Host={DB_Host}\n")
    f.write(f"DB_User={DB_User}\n")
    f.write(f"DB_Pass={DB_Pass}\n")
    f.write(f"DB_Name={DB_Name}\n")
    f.close()
