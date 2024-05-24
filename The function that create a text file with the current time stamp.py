
from datetime import datetime


def create_timestamp():
    timestamp= datetime.now().strftime("%Y-%M-%D_%H-%M-%S")
    with open(f"The countent file.txt",'w') as file_write:
        file_write.write("The current time when the file is created is -" + timestamp)
create_timestamp()




