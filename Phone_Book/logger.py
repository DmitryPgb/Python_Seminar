from datetime import datetime
import output_style

def log_to_file(entry):
    b = output_style.style()
    if b == 1:
        with open('telephone.csv', 'a') as file:
            file.write(
                f'"{datetime.today()};{entry[0]};{entry[1]};{entry[2]};{entry[3]};"\n')
    
    if b == 2:
        with open('telephone.csv', 'a') as file:
            file.write(
                f'"{datetime.today()}\n;{entry[0]}\n;{entry[1]}\n;{entry[2]}\n;{entry[3]};"\n')

def ereading_file(param):
    with open('telephone.csv', 'r') as file:
        for line in file:
            sstroka = line
            print(line)

def read_all_files():
    with open('telephone.csv', 'r') as file:
        for line in file:
            print(line)