import os

for d in range(71):
    try:
        # Create target Directory
        os.mkdir(str(d))
        print("Directory " , d ,  " Created ") 
    except FileExistsError:
        print("Directory " , d ,  " already exists")
    