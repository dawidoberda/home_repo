import unittest #modul ktory sluzy do testowania
import calc #musimy zaimportowac modul ktory testujemy

class TestCalc(unittest.TestCase): #klasa musi dziedziczyc po unittest.TestCase

    def test_add(self): # metoda testujaca musi zaczynac sie od test_
        self.assertEqual(calc.add(10, 5), 15)  #wykorzystujemy dziedziczone z TestCase sprawdzanie(szeczegoly w dok) tutaj sprawdza czy dwie liczby sa rowne
        self.assertEqual(calc.add(-1, 1), 0)   #test powinien byc tak napisany aby sprawdzal warunki brzegowe
        self.assertEqual(calc.add(-1, -1), -2)  #test powinien byc tak napisany aby sprawdzal warunki brzegowe


    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(-1, 1), -2)
        self.assertEqual(calc.substract(-1, -1), 0)


    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0) #Metoda1.tego uzywamy jak chcemy sprawdzic czy rzuca dany exception. Argumenty nalezy przekazac osobno

        with self.assertRaises(ValueError): #druga metoda przy uzyciu context menagera tutaj funkcje wywolujemy bezposrednio
            calc.divide(10,0)

if __name__ == '__main__': #to trzeba dac aby odpalic test z IDE
    unittest.main()