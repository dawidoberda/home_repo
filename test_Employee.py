import unittest
from unittest.mock import patch
from Employee import Employee


class TestEmployee(unittest.TestCase): #przyklad testowania klasy


    @classmethod
    def setUpClass(cls) -> None: #to odpala sie raz przy inicjalizacji danego modulu testowego
        pass

    @classmethod
    def tearDownClass(cls) -> None:   #to odpala sie raz przy zakonczeniu danego modulu testowego
        pass

    def setUp(self):   #to jest build in ktory odpala sie przed kazdym testem (kazdym jednym)
        self.emp_1 = Employee('Dawid', 'Oberda', 5000)
        self.emp_2 = Employee('Jan', 'Kowalski', 5510)

    def tearDown(self):   #to jest build in ktory odpala sie po kazdym tescie (kazdym jednym)
        pass

    def test_mail(self):

        self.assertEqual(self.emp_1.mail, 'Dawid.Oberda@gmail.com')
        self.assertEqual(self.emp_2.mail, 'Jan.Kowalski@gmail.com')

        self.emp_1.first = 'Mateusz'
        self.emp_2.last = 'Nowak'

        self.assertEqual(self.emp_1.mail, 'Mateusz.Oberda@gmail.com')
        self.assertEqual(self.emp_2.mail, 'Jan.Nowak@gmail.com')


    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Dawid Oberda')
        self.assertEqual(self.emp_2.fullname, 'Jan Kowalski')

        self.emp_1.first = 'Mateusz'
        self.emp_2.last = 'Nowak'

        self.assertEqual(self.emp_1.fullname, 'Mateusz Oberda')
        self.assertEqual(self.emp_2.fullname, 'Jan Nowak')

    def test_applyRaise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 5785.5)

    #Ten test polega na udawaniu jakiejsc rzeczy. np. strony internetowej i zwraca wartosci ktore mu podamy aby
    #sprawdzic dzialanie kodu a nie np. dostepnosc danej strony
    def test_monthly_schedule(self):
        with patch('Employee.requests.get') as mocked_get: #trzeba jako argument bezposrednio podac klase w ktorej jest to co testujemy
            # test jezeli request zwroci True
            mocked_get.return_value.ok = True #tutaj definiujemy jakie wartosci ma zwrocic
            mocked_get.return_value.text = 'Sucess' #tutaj definiujemy jakie wartosci ma zwrocic

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Oberda/May') #sprawdzanie czy zostanie wywolana odpowiednia strona
            self.assertEqual(schedule, 'Sucess') #przeprowadzamy test

            #test jezeli request zwroci false
            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Oberda/May')
            self.assertEqual(schedule, 'Bad Response')

if __name__ == '__main__':
    unittest.main()