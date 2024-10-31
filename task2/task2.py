from pathlib import Path

def get_cats_info(path):
    lines = []
    cats_info = {}

# open file as "try...except" for reading file
    try:
        with open (Path(path), "r", encoding='utf-8') as fh:
            for el in fh.readlines():
        
# split line and add list elements to dict                     
                cats_info =  {'id': el.split(',')[0],
                            'name': el.split(',')[1],
                             'age': el[:-1].split(',')[2] if el[-1] == '\n' else el.split(',')[2]}
                
                lines.append(cats_info)    

#exception handling.    'FileNotFoundError',   'UnicodeDecodeError' or unknown error in other cases           
    except FileNotFoundError:
        print(f"File {path} does not exist")
    except  UnicodeDecodeError:    
        print("wrong format of file")
    except Exception as e:
        print(f"Unknown exception, {e}")

        
    return lines    

print(get_cats_info('task2.txt'))
