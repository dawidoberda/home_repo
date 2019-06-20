
try:
    f = open('testowyDoZapisu')
    if f.name() == 'testowyDoZapisu':
        raise Exception        #mozemy sami wywolywac wyjatki (przy np. specyficznej nazwie pliku
except FileNotFoundError as e: #mozemy przekazac blad do zmiennej i pozniej ja wyswietlic
    print(e)
except Exception:
    print('Error !!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finnally...')

