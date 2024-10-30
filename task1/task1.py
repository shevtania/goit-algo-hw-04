from pathlib import Path

def total_salery(path):
    lines = []
    sum = 0
    average = 0

    try:
        with open (Path(path), "r", encoding='utf-8') as fh:
            for el in fh.readlines():
                if el[-1] == '\n':
                    lines.append(el[:-1].split(','))
                else:
                    lines.append(el.split(','))  
          
    except FileNotFoundError:
        print(f"File {path} does not exist")
    except  UnicodeDecodeError:    
        print("wrong format of file")
    except Exception as e:
        print(f"Unknown exception, {e}")

    for el in lines:
        sum += int(el[1])
    average = sum / len(lines)    

    return  sum, int(average)

print(total_salery('task1.txt'))