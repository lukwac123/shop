# Aplikacja Sklep zbudowana z użyciem framwork'a Django.

Użytkownicy sklepu mogą przeglądać katalog produktów dostępnych do sprzedaży, dodawać do koszyka. Po wybraniu produktów użytkownik może złożyć zamówienie i sfinalizować zakup przy pomocy płatności on-line. 

![shop_strona_glowna](https://github.com/user-attachments/assets/e6188527-bee8-4037-98a3-c2f47dbb0f01)
<sub>Rys. 1. Strona główna sklepu internetowego.</sub>

---
## Główne funkcje

- Przeglądanie katalogu produktów z filtrowaniem po kategoriach
- Szczegóły produktu ze zdjęciem i opisem
- Koszyk z możliwością edycji ilości
- Proces składania zamówienia
- Płatności online przez Stripe
- System kuponów rabatowych
- Panel administracyjny do zarządzania produktami i zamówieniami
- Eksport zamówień do PDF
- Zastosowanie klasowych widoków, własnych szablonów i middlewarów

---
## Struktura katalogów
| 📁 shop                  | Katalog projektu                                                       |
|:-------------------------|:-----------------------------------------------------------------------|
| 📁 shop/                 | Główna konfiguracja projektu Django                                    |
| 📁 cart/                 | Obsługa koszyka                                                        |
| 📁 coupons/              | Obsługa kuponów rabatowych                                             |
| 📁 orders/               | Obsługa zamówień i płatności                                           |
| 📁 payment/              | Integracja ze Stripe                                                   |
| 📁 products/             | Zarządzanie produktami i kategoriami                                   |
| 📁 templates/            | Szablony HTML dla aplikacji                                            |
| 📁 static/               | Pliki statyczne (CSS, JS, grafika)                                     |
| 📁 media/                | Pliki przesyłane przez użytkownika (zdjęcia produktów)                 |
| 📄 manage.py             | Główne narzędzie zarządzania Django                                    |
| 📄 requirements.txt      | Lista zależności                                                       |
| 📄 db.sqlite3            | Baza danych (domyślnie SQLite)                                         |
| 📄 README.md             | Opis aplikacji                                                         |

---
## Przebieg projektu:
1. Utworzenie projektu, środowiska wirtualnego, aplikacji w Pythonie oraz instalacja Django.
2. Utworzenie modeli katalogu produktów, dodanie ich do witryny administracyjnej oraz przygotowanie podstawowych widoków przeznaczonych do wyświetlania katalogu.
3. Opracowanie systemu koszyka dla sesji Django, co pozwoli użytkownikowi na zachowanie wybranych produktów w koszyku podczas przeglądania strony internetowej.
4. Zbudowanie formularza i funkcjonalności, które pozwalają na składanie zamówień.
5. Wysłanie do użytkownia asynchronicznego powiadomienia przez e-mail po złożeniu zamówienia.
6. Zarządzanie þłatnościami i zamówieniami
	* 6.1 Zintegrowanie projektu z bramką płatności Stripe.
    * 6.2 Przetwarzanie þłatności kartą kredytową przy użyciu serwisu Stripe.
    * 6.3 Powiadomienia o þłatności.
    * 6.4 Eksportowanie zamówienia do pliku CSV.
    * 6.5 Dynamiczne generowanie faktury do złożonego zamówienia w formacie PDF.
7. Utworzenie systemu kuponów rabatowych.
8. Opracowanie silnika rekomendacji produktów za pomocą Redis.
9. Internacjonalizacja sklepu internetowego.

---
## Źródło
_Django 4. Tworzenie nowoczesnych aplikacji internetowych w Pythonie_  
Autor: Antonio Melé  
Wydawnictwo Helion, 2023  
