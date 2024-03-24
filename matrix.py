import numpy as np
#
# #I metoda
#
# a = np.arange(1,11)
# print(a)

# II metoda

wektor = []

licznik = 1

while len(wektor)<10:
    if licznik > 0:
        wektor.append(licznik)
    licznik +=1

wektor_numpy = np.array(wektor)
print(wektor_numpy)


#2. Stworzenie macierzy 3x3 wypełnionej zerami

# macierz = []
#
#
# for i in range(3):
#     wiersz = []
#     for j in range(3):
#         wiersz.append(0)
#     macierz.append(wiersz)
#
# macierz_numpy = np.array(macierz)
# print(macierz_numpy)

#3 tablica o rozmiarze 5x5, wypełniona losowymi liczbami całkowitymi
# z zakresu od 1 do 10

import random

macierz_3 = []

for i in range(5):
    wiersz = []
    for i in range(5):
        liczba = random.randint(1,10)
        wiersz.append(liczba)
    macierz_3.append(wiersz)


macierz_3_numpy = np.array(macierz_3)
print(macierz_3_numpy)

#4  tablicę o rozmiarze 4x4, wypełnij ją losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i wyświetl jej wartość.

macierz_4 = []

for i in range(4):
    wiersz_4 = []
    for j in range(4):
        liczba_4 = random.randint(0,1)
        wiersz_4.append(liczba_4)
    macierz_4.append(wiersz_4)

macierz_4_numpy = np.array(macierz_4)
print(macierz_4_numpy)


#Utwórz dwie jednowymiarowe tablice o rozmiarze 5, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i wykonaj na nich operacje dodawania, odejmowania i mnożenia

tablica_1 = np.array([random.randint(1,10) for i in range(5)])
tablica_2 = np.array([random.randint(1,10) for i in range(5)])

print(tablica_1)
print(tablica_2)

#dodawanie tablic
suma = tablica_1 + tablica_2
print(f"Suma: {suma}")

#odejmowanie tablic
różnica = tablica_1 - tablica_2
print(f"Różnica: {różnica}")

#mnożenie tablic
mnożenie = tablica_1 * tablica_2
print(f"Mnożenie: {mnożenie}")

#Utwórz dwa wektory o rozmiarze 7, wypełnij je losowymi liczbami i znajdź ich iloczyn skalarny.

wektor_1 = np.array([random.randint(1,9) for _ in range(7)])
wektor_2 = np.array([random.randint(1,9) for _ in range(7)])

print(f"Wektor 1: {wektor_1}")
print(f"Wektor 2: {wektor_2}")

iloczyn_skalarny = np.dot(wektor_1, wektor_2)
print(f"Iloczyn skalarny: {iloczyn_skalarny}")

#Utwórz dwie macierze o rozmiarach 2x2 i 2x3, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i pomnóż je.

matrix_1 = []

for i in range(2):
    vers = []
    for j in range(2):
        number = random.randint(1,10)
        vers.append(number)
    matrix_1.append(vers)
matrix_1_numpy = np.array(matrix_1)
print(f"Macierz 1: \n{matrix_1}")

matrix_2 = []

for x in range(2):
    vers_2 = []
    for y in range(3):
        number_2 = random.randint(1,10)
        vers_2.append(number_2)
    matrix_2.append(vers_2)

matrix_2_numpy = np.array(matrix_2)
print(f"Macierz 2: {matrix_2_numpy}")

iloczyn_macierzy = np.dot(matrix_1_numpy, matrix_2_numpy)
print(f"Iloczyn macierzy z zad. 7 {iloczyn_macierzy}")

#Utwórz macierz o rozmiarze 3x3, wypełnij ją losowymi liczbami całkowitymi z zakresu od 1 do 10 i znajdź jej odwrotność.

macierz_8 = []

for i in range(3):
    wiersz_8 = []
    for j in range(3):
        liczba_8 = random.randint(1,10)
        wiersz_8.append(liczba_8)
    macierz_8.append(wiersz_8)

macierz_8_numpy = np.array(macierz_8)
print(f"Macierz 8: \n{macierz_8_numpy}")
odw_macierz_8 = np.linalg.inv(macierz_8_numpy)
print(f"Odwrócona macierz z zad. 8: \n{odw_macierz_8}")

#Utwórz macierz 4x4, wypełnij ją losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i przetransponuj ją.

macierz_9 = []

for i in range(4):
    wiersz_9 = []
    for j in range(4):
        liczba_9 = random.randint(0,1)
        wiersz_9.append(liczba_9)
    macierz_9.append(wiersz_9)

macierz_9_numpy = np.array(macierz_9)
print(f"Macierz z zad 9: \n{macierz_9_numpy}")
macierz_9_T = macierz_9_numpy.T
print(f"Macierz transponowana z zad 9: \n{macierz_9_T}")


#Utwórz macierz o rozmiarze 3x4 i wektor o rozmiarze 4, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i pomnóż macierz przez wektor

wektor_10 = np.array([random.randint(1,10) for _ in range(4)])
print(f'Wektor z zad 10 {wektor_10}')

macierz_10 = np.array([[random.randint(1,10) for _ in range(4)] for _ in range(3)])
print(f" Macierz z zadania 10: \n{macierz_10}")

iloczyn_10 = np.dot(macierz_10, wektor_10)
print(f"Wynik zadania 10:\nIloczyn macierzy i wektora\n{iloczyn_10}")

#Utwórz macierz o rozmiarze 2x3 i wektor o rozmiarze 3, wypełnij je losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i pomnóż macierz przez wektor.

wektor_11 = np.array([random.randint(1,10) for _ in range(2)])
print(f"Wektor do zad 11:{wektor_11}")

macierz_11 = np.array([[random.randint(1,10) for i in range(2)] for j in range(3)])
print(f"Macierz do zad 11: \n{macierz_11}")

iloczyn_11 = np.dot(macierz_11, wektor_11)
print(f"Wynik iloczynu z zad 11: {iloczyn_11}")

#Utwórz dwie macierze o rozmiarze 2x2, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i wykonaj ich mnożenie pierwiastkowe.

macierz_1_12 = np.array([[random.randint(1,10) for i in range(2)] for j in range(2)])
print(f"Pierwsza macierz z zad 12 \n{macierz_1_12}")

macierz_2_12 = np.array([[random.randint(1,10) for i in range(2)] for j in range(2)])
print(f"Druga macierz z zad 12 \n{macierz_2_12}")

iloczyn_pierw = macierz_1_12 * macierz_2_12
print(f"Wynik mnożenia pierwiastkowego z zad 12: \n{iloczyn_pierw}")
iloczyn_skalarny = np.dot(macierz_1_12, macierz_2_12)
print(f"Wynik mnożenia skalarnego z zad 13: \n{iloczyn_skalarny}")

#Utwórz macierz 5x5, wypełnij ją losowymi liczbami całkowitymi z zakresu od 1 do 100 i znajdź sumę elementów macierzy.
sum = 0
macierz_14 = np.array([[random.randint(1,100) for i in range(5)] for j in range(5)])
print(f"Macierz 5x5 z zad 14:\n{macierz_14}")
suma_elem_macierz_14 = np.sum(macierz_14)
print(f"Suma elementów macierzy z zad 14: \n{suma_elem_macierz_14}")

#Utwórz dwie macierze o rozmiarze 4x4, wypełnij je losowymi liczbami całkowitymi z zakresu od 1 do 10 i znajdź ich różnicę.

macierz_15_1 = np.array([[random.randint(1,10) for i in range(4)] for j in range(4)])
macierz_15_2 = np.array([[random.randint(1,10) for i in range(4)] for j in range(4)])

print(f"Macierze 4x4 do zadania 15:\nPierwsza maicerz\n{macierz_15_1}\nDruga macierz{macierz_15_2}")
roznica_15 = macierz_15_1 - macierz_15_2
print(f"Różnica macierzy z zad 15:{roznica_15}")

#Utwórz macierz 3x3, wypełnij ją losowymi liczbami rzeczywistymi z zakresu od 0 do 1 i znajdź wektor kolumnowy zawierający sumę elementów każdego wiersza macierzy.

macierz = np.random.rand(3, 3)
print("Macierz 3x3:")
print(macierz)

wektor_sum = np.sum(macierz, axis=1, keepdims=True)
print("Wektor kolumnowy zawierający sumę elementów każdego wiersza macierzy:")
print(wektor_sum)

#Utwórz macierz o rozmiarze 3x4 z dowolnymi liczbami całkowitymi i utwórz macierz z kwadratami tych liczb.

macierz_17 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

macierz_kw_17 = np.square(macierz_17)
print(f"Macierz kwadratowa z macierzy:\n{macierz_17}\nWynosi:\n{macierz_kw_17}")

#Utwórz wektor o rozmiarze 4, wypełnij go losowymi liczbami całkowitymi z zakresu od 1 do 50 i znajdź wektor pierwiastków kwadratowych z tych liczb.

wektor_18 = np.array([random.randint(1,50) for i in range(4)])
print(f"Wektor o rozm. 4 z zad 18:\n{wektor_18}")
wektor_sqrt_18 = np.sqrt(wektor_18)
print(f"Wektor pierwiastków z zad 18: \n{wektor_sqrt_18}")
