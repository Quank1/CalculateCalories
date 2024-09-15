from importlib.metadata import PackageMetadata
import importlib.util
import os, sys

IfStart = True
list_lib = ['requests', 'BeautifulSoup4', "lxml"]
name_Path = 'myenv/'

def CheckLibrary(name):
    package_spec = importlib.util.find_spec(name)

    if package_spec == None:
        print(f"Бібліотека {name} не встановленна в віртуальне оточеня. Встановлення бібліотеки...")
        try:
            os.system(f'pip install {name}')
            print(f"Бібліотека {name} успішно встановленна!")
        except:
            print(f"Бібліотека {name} не встановленна!")
            IfStart = False
    else:
        print(f"Бібліотека {name} встановленна!")
        

def CreateVirtualEnvironment():
    if not os.path.exists(name_Path):
        print("Створення віртуального оточення...")
        try:
            os.system('python3 -m venv myenv')
            print("Віртуальне оточення створено!")
        except:
            print("Віртуальне оточення не створенно!")
        
        
def EnterVirtualEnvironment():
    if not os.path.exists(name_Path):
        CreateVirtualEnvironment()
    else:
        os.system("source myenv/bin/activate")

def StartProgram():

    try:
        if not os.path.exists('db/'):
            os.system('python3 CreateDB.py')
        os.system('clear')
        os.system('python3 CalcCalories/CalculateCalories.py')
    except:
        print("Проблеми з виконанням файлу...")
    




for lib in list_lib:
    CheckLibrary(lib)
CreateVirtualEnvironment()
EnterVirtualEnvironment()
StartProgram()