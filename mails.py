import smtplib #biblioteka potrzebna do pracy z mailami
from email.message import EmailMessage #biblioteka do bardziej zawansowanej pracy z mailami
import imghdr #biblioteka do pracy nad zdjeciami

#Przyklad do gmail
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #context menager do olaczenia z serwerem poczty
#     smtp.ehlo() #to trzeba wywolac na poczatku
#     smtp.starttls() #otwiera zaszyfrowane polaczenie
#     smtp.ehlo() #to trzeba wywolac jeszcze raz po wlaczeniu szyfrowania
#
#     smtp.login('*', '*') #logujemy do konta
#
#     subject = 'Temat testowy'
#     body = 'tekst testowej wiadomosci'
#
#     msg = f'Subject: {subject}\n\n{body}' #tak tworzy sie wiadmosc w podstawowym trybie
#
#     smtp.sendmail('*', '*', msg) #wysylanie maila (nadawca,odbiorca,wiadmosci)

# #Przyklad do localhost (serwer do debugu)
# with smtplib.SMTP('localhost', 1025) as smtp:
#     subject = 'Temat testowy'
#     body = 'tekst testowej wiadomosci'
#
#     msg = f'Subject: {subject}\n\n{body}' #tak tworzy sie wiadmosc w podstawowym trybie
#
#     smtp.sendmail('dawidoberda@gmail.com', 'dawidoberda@gmail.com', msg) #wysylanie maila (nadawca,odbiorca,wiadmosci)

message = EmailMessage() #tworzymy obiekt wiadomosci
message['Subject'] = 'Temat wiadomosci' #ustalamy temat
message['From'] = 'dawidoberda@gmail.com' #mozemy w tym obiekcie ustalic nadawce
message['To'] = 'dawidoberda@gmail.com' #mozemy w tym obiekcie ustalic odbiorce, aby wyslac do wiecej niz jednego odbieorcy:
    #tworzymy liste i pozniej piszemy tak: message['To'] = ', '.join(nazwaListy)
message.set_content('Tekst wiadomosci testowej !!') #ustalamy tresc wiadomosci

#mozna tez zmienic formatowanie tresci wiadomosci za pomoca html
message.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML mail!</h1>
    </body>
</html>
""", subtype='html')

with open('content.png', 'rb') as f:
    file_data = f.read() #wczytujemy zdjecie.
    file_type = imghdr.what(f.name) #wczytujemy typ pliku (jpg, png .. )
    file_name = f.name #zwraca nazwe pliku

message.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name) #dodaje zalacznik do wiadomosci
#aby wczytac wiece wiadomosci wystarczy to powielic z innym plikiem albo calosc umiescic w petli

with open('trasa.pdf', 'rb') as f_pdf:
    pdf_data = f_pdf.read()
    pdf_name = f_pdf.name

message.add_attachment(pdf_data, maintype='application', subtype='octet-stream', filename=pdf_name) #aby wyslac pdf

#Bardziej zawansowane wysylanie maili
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #context menager do olaczenia z serwerem poczty
    #ten jest juz zakodowany
    smtp.login('*', '*') #logujemy do konta

    smtp.send_message(message) #wysylanie maila (nadawca,odbiorca,wiadmosci)