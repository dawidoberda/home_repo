import os
from datetime import datetime

print(os.getcwd()) #wyswietla current working directory
os.chdir('/home/kvothe/PycharmProjects') #zmienia aktualnie przegladany folder
print(os.getcwd())

print(os.listdir()) #wyswietla liste folderow w aktualnym folderze (mozna wywolac z konkretna sciezka jako argument)

os.mkdir('testowy') #tworzy folder ale nie potrafi stworzyc calej sciezki tylko jeden folder
os.makedirs('probny/sub-folder') # tworzy folder i wszystkie foldery po drodze (czyli najpierw probny pozniej sub-folder)

print(os.listdir())

os.rmdir('testowy') #usuwa pojedynczy folder, nie potrafi usunac calej sciezki
os.removedirs('probny/sub-folder') #usuwa folder i cala sciazke

print(os.listdir())

#os.rename('test.txt', 'demo.txt')#zmienia nazwe pliku na inny
#print(os.listdir())

print(os.stat('demo.txt')) #wyswietla informacje o pliku
print(os.stat('demo.txt').st_mtime) #mozna wywolac konkretna informacje (tutaj data modyfikacji jako datestamp)

mod_time = os.stat('demo.txt').st_mtime #zapisa daty ostatniej modyfikacji w celu konwersji
print(datetime.fromtimestamp(mod_time)) #konwersja stamptime na datetime format

# for dirpath, dirname, filename in os.walk(os.getcwd()): #zwraca cale drzewo plikow dla wskazanej lokacji tutaj cwd
#     print("Current directory Path:", dirpath)
#     print("Current directory name:", dirname)
#     print("Current file name:", filename)
#     print("")

print(os.environ.get('HOME')) #zwraca zmienne srodowiskowe (tutaj HOME)
file_path=os.path.join(os.environ.get('HOME'),'dawid.txt') #narzedzie do tworzenie sciezek do plikow(tworzac recznie mozna pominac np. /)
print(file_path)
base_name = os.path.basename(file_path) #zwraca sama nazwe pliku z danej sciezki
dir_name = os.path.dirname(file_path) # zwraca sciezke do pliku bez nazwy pliku
print('{} to basename tej sciezki'.format(base_name))
print('{} to czesc dir name tej sciezki'.format(dir_name))
print(os.path.exists(file_path)) #zwraca informacje czy dany plik istnieje
file_directory , file_extension = os.path.splitext(file_path) #zwraca sciezke do pliku oraz rozszerzenie
print(file_directory)
print(file_extension)