import os
def open_file(file_path):
    
    f = open(file_path, 'r')
    
    for line in f:
        if ':' in line:
            result = line.split(':', 1)[1].strip()
            print(result)
    
    f.close()

open_file('evenementSAE_15_2025.ics')