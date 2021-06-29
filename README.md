# GoL-BMC
Conway's Game of Life and Bounded Model Checking heavily inspired by Donald E. Knuth's The Art of Computer Programming, Volume 4, Fascicle 6: Satisfiability.

Skrypt wymaga SAT-solvera domyślnie jest to `kissat` natomiast z flaga `-s` można podac sciezke do własnego SAT-solvera.
Użycie :

~~~
python3 gol-encoding.py -i daniel3.in
~~~
gdzie daniel3.in jest plikiem wejściowym. Inne pliki wejściowe rownież posiadają format .in i są to między innymi:
- cycl1.in - punkt stał
- daniel4.in - napis DANIEL w 4 ruchach, częściowo ustalona plansza
- galaxy8.in - galaktyka Koka z cyklem o długości 4
- life3.in - napis LIFE w 3 ruchach
- star3.in - gwiazda z cyklem o długości 3
Dla poszukiwania cyklu należy dodać flagę `-c True`

~~~
python3 gol-encoding.py -i galaxy8.in -c True
~~~

### Brak SAT-solvera

Wyświetlanie wyniku:

~~~
python3 gol.py -i daniel3.out -s 28 -t 2
~~~
gdzie 's' wielkość planszy, 't' liczba ruchów.
