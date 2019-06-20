import csv

# with open('example', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     # next(csv_reader) # powoduje przeskoczenie jednej wartosci
#
#     for line in csv_reader:
#         print(line)

with open('example', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) # wczytuje kazdy wiersz jak slownik(klucz to header, wartosc to pole z csv)

    # for line in csv_reader:
    #     print(line)

    for line in csv_reader:
        print(line['Name']) #uzywajac DictReader mozemy szukac konkretnych kluczy

    with open('new_file.csv', 'w') as new_file:
        fieldnames = ['Name']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t') # tworzy obiekt do zapisywania do csv

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line) # zapisuje wiersz do pliku csv


# with open('example', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_file.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter = '\t') # tworzy obiekt do zapisywania do csv
#
#         for line in csv_reader:
#             csv_writer.writerow(line) # zapisuje wiersz do pliku csv