# GoL-BMC
Conway's Game of Life and Bounded Model Checking heavily inspired by Donald E. Knuth's The Art of Computer Programming, Volume 4, Fascicle 6: Satisfiability.

Skrypt wymaga SAT-solvera domylscie jest to 'kissat' natomiast z flaga '-s' mozna podac sciezke do wlasnego SAT-solvera.
Usage :

~~~
python3 gol-encoding.py -i daniel3.in
~~~
gdzie daniel3.in jest plikiem wejsciowym. Inne pliki wejsciowe rowniez posiadaja format .in i sa to miedzy innymi:
- cycl1.in - punkt staly
- daniel4.in - napis DANIEL w 4 ruchach czesciowo ustalona plansza
- galaxy8.in - galaktyka Koka z cyklem o dlugosci 4
- life3.in - napis LIFE w 3 ruchach
- star3.in - gwiazda z cyklem o dlugosci 3

Dla poszukiwania cyklu nalezy dodac flage '-c True'

~~~
python3 gol-encoding.py -i galaxy8.in -c True
~~~

### Brak SAT-solvera

Wyswietlanie wyniku:

~~~
python3 gol.py -i daniel3.out -s 28 -t 2
~~~
gdzie 's' wielkosc planszy, 't' liczba ruchow.
