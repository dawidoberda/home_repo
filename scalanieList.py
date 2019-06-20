def main():
    pass

first = ['dawid', 'mateusz', 'Jan', 'michal']
last = ['oberda', 'zieba', 'kowalski', 'nowak']

fullname = zip(first, last)

print(fullname) #samo to w przypadku listy powstalej z zip zroci tylko miejsce w pamieci
print(list(fullname)) #tutaj dostaniemy polaczona liste gdzie 1 element z pierwszej listy jest polaczony z 1 elementem z drugiej itd.

# for name in fullname:
#     print('imie to {}, natomiast nazwisko to {}'.format(name[0], name[1])) #mozna uzyskac dostep do kazdego elementu z danej pary

print(__name__)

#ten fragment jest po to aby sprawdzic czy modul jest odpalany przez python czy importowany
#importowany modul bedzie mial zmienna __name__ rowno nazwie danego modulu a nie main
#co oznacza  ze dany modul bedzie mogl zachowywac sie inaczej w zaleznosci od tego czy zostal wywolany bezposrednio
# czy np go importujemy i np. nie chcemy aby czesc rzeczy sie wykonywala
if __name__ == '__main__':
    main()