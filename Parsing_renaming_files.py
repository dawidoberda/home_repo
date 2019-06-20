import os

os.chdir('/home/kvothe/Pulpit/testowy')

print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    tittle, number = file_name.split('-')
    number = number.zfill(2) #to dodaje zero na poczatku tak aby zmienna miala 2 znaki. (jezeli ma dwa to nie doda)
    new_name = '{}-{}{}'.format(number, tittle, file_ext)
    #print(new_name)
    os.rename(f, new_name)