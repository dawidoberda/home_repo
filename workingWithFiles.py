

# f = open('testowyPlik', 'r')
#
# print(f.name)
# print(f.mode) #zwraca tryb w w jakim otworzylismy plik
#
# f.close()

# with open('testowyPlik', 'r') as f: #preferowana metoda ktora zamyka za nas plik (rowniez jak wyskoczy jakis blad)
#     # f_content = f.read() #czyta caly plik
#     f_content = f.readline() #czyta pojedynczy wiersz (nastepny za kazdym kolejnym wywolaniem)
#     print(f_content)
#
#     for line in f:   #iteruje po wszystkich liniach w danym pliku
#         print(line, end='')


# with open('testowyPlik', 'r') as f:
#     file = f.read(10)
#     cursor_position = f.tell() # zwraca informacje gdzie znajduje sie kursor
#     print(file)
#
#     f.seek(0) #ustawia kursor w zadanej pozycji
#     file = f.read(10)
#     print(file)


with open('testowyDoZapisu', 'w') as w:
    w.write('Test')
    w.write('Test')