# Optimization-of-delivery-route-using-genetic-algorithm
System znajdowania najbardziej optymalnej trasy pomiędzy dziesięcioma miastami przy użyciu algorytmu genetycznego.


<p align="center">
   <img src="https://img.shields.io/badge/Engine-PyCharm%2023-B7F352" alt="Engine">
</p>

## About


Celem projekta jest zastosowanie algorytmu genetycznego w celu optymalizacji trasy dostaw dla przedsiębiorstwa kurierskiego, które posiada zestaw klientów z określonymi lokalizacjami i paczkami do dostarczenia. Głównym celem jest znalezienie optymalnej trasy, która minimalizuje łączny koszt lub czas dostawy. Algorytm genetyczny powinien być używany do efektywnego eksplorowania przestrzeni możliwych tras, uwzględniając ograniczenia i preferencje związane z dostawami, aby zaoferować przedsiębiorstwu kurierskiemu optymalne rozwiązanie logistyczne.
</br>

## Documentation

### Libraries
- `numpy`, `random`, `matplotlib`, `folium`

### Definicja danych
- Przygotowano macierze odległości między miastami, kosztów paliwa i ilości zużytego paliwa.
### Generowanie genotypu
- Tworzy losową trasę w postaci np. {5, 2, 6, 4, 1, 3, 7, 9, 10, 8}.
### Inicjalizacja populacji
- Tworzenie początkowej populacji o rozmiarze zmiennej SELF_SIZE
### Ocena funkcji docelowej
- Obliczenie efektywności trasy według odległości, kosztu i ilości paliwa.
### Ewolucja populacji
- Stworzenie algorytmu genetycznego obejmującego metody selekcji, krzyżowania i mutacji, oraz ocenę każdego osobnika.
### Optymalizacja
- Przeprowadzono kilka generacji, zastosowano ustawienia algorytmu genetycznego, takie jak liczba pokoleń, rozmiar turnieju oraz prawdopodobieństwo krzyżowania i mutacji.
### Wizualizacja wyników
- Wykorzystuje bibliotekę Folium do stworzenia interaktywnej mapy pokazującej miasta i optymalną trasę. 
## Developers

- Danyil Muzychenko (https://github.com/DanyilMuzychenko)
