# Aplikacja Sklep zbudowana z użyciem framwork'a Django.

Użytkownicy sklepu mogą przeglądać katalog produktów dostępnych do sprzedaży, dodawać do koszyka. Po wybraniu produktów użytkownik może złożyć zamówienie i sfinalizować zakup przy pomocy płatności on-line. 

![shop_strona_glowna](https://github.com/user-attachments/assets/e6188527-bee8-4037-98a3-c2f47dbb0f01)
<sub>Rys. 1. Strona główna sklepu internetowego.</sub>

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
