from pathlib import Path

def total_salery(path):
    lines = []
    sum = 0 # sum of salery
    average = 0 # average salary

# open file with employees information as "try ... except"   

    try:
        with open (Path(path), "r", encoding='utf-8') as fh:
            for el in fh.readlines():  # reading file as one line at a time
                if el[-1] == '\n':     
                    lines.append(el[:-1].split(',')) # split line with coma and add it in the list of lists
                else:
                    lines.append(el.split(','))  
          
    except FileNotFoundError:
        print(f"File {path} does not exist")
    except  UnicodeDecodeError:    
        print("wrong format of file")
    except Exception as e: # catch unknown errors
        print(f"Unknown exception, {e}")

# calculate sum and average salery
    for el in lines:
        sum += int(el[1])
    average = sum / len(lines)    

    return  sum, int(average)

print(total_salery('task1.txt'))