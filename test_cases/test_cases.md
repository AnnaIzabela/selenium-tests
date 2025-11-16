# Przypadki Testowe

## 1.1. Przypadki testowe strony logowania

### ID: 001 — Logowanie do konta bez podania danych
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości zalogowania bez podania danych  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik nie jest zalogowany  

**Kroki do reprodukcji:**  
1. Wejdź na stronę `http://example.com/login`  
2. Najedź kursorem na input login i kliknij Enter  
3. Najedź kursorem na input hasło i kliknij Enter  
4. Kliknij przycisk zaloguj  

**Oczekiwany rezultat:**  
1. Otwiera się strona logowania  
2. Pojawia się komunikat: „Pole 'login' jest wymagane”  
3. Pojawia się komunikat: „Pole 'hasło' jest wymagane”  
4. Przycisk zaloguj jest nieaktywny  

**Warunki końcowe:**  
- Brak możliwości zalogowania bez podania danych

---

### ID: 002 — Logowanie do konta bez podania loginu
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości logowania bez podania loginu  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik nie jest zalogowany  

**Kroki do reprodukcji:**  
1. Wejdź na stronę `http://example.com/login`  
2. W pole hasło wpisz hasło  
3. Pole login pozostaw puste  
4. Kliknij przycisk zaloguj  

**Oczekiwany rezultat:**  
1. Otwiera się strona logowania  
2. Hasło zostaje wpisane  
3. Pojawia się komunikat: „Pole 'login' jest wymagane”  
4. Przycisk zaloguj jest nieaktywny  

**Warunki końcowe:**  
- Brak możliwości zalogowania bez podania loginu  

---

### ID: 003 — Logowanie do konta bez podania hasła
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości zalogowania bez podania hasła  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik nie jest zalogowany  

**Kroki do reprodukcji:**  
1. Wejdź na stronę `http://example.com/login`  
2. W pole login wpisz login  
3. Pole hasło pozostaw puste  
4. Kliknij przycisk zaloguj  

**Oczekiwany rezultat:**  
1. Otwiera się strona logowania  
2. Login zostaje wpisany  
3. Pojawia się komunikat: „Pole 'hasło' jest wymagane”  
4. Przycisk zaloguj jest nieaktywny  

**Warunki końcowe:**  
- Brak możliwości zalogowania bez podania hasła  

---

### ID: 004 — Logowanie niepoprawnymi danymi
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości logowania po podaniu nieprawidłowych danych  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik nie jest zalogowany  

**Kroki do reprodukcji:**  
1. Wejdź na stronę `http://example.com/login`  
2. Wpisz niepoprawny adres email w login  
3. Wpisz niepoprawne hasło  
4. Kliknij przycisk zaloguj  

**Oczekiwany rezultat:**  
1. Otwiera się strona logowania  
2. Login i hasło zostają wpisane  
3. Po kliknięciu przycisku zaloguj pojawia się komunikat: „Login lub hasło jest nieprawidłowe”  
4. Logowanie niepoprawnymi danymi jest niemożliwe  

**Warunki końcowe:**  
- Brak możliwości zalogowania się niepoprawnymi danymi  

---

### ID: 005 — Logowanie poprawnymi danymi
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości zalogowania po podaniu prawidłowych danych  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik posiada konto  
- Użytkownik nie jest zalogowany  

**Kroki do reprodukcji:**  
1. Wejdź na stronę `http://example.com/login`  
2. Wpisz poprawny adres email w login  
3. Wpisz poprawne hasło  
4. Kliknij przycisk zaloguj  

**Oczekiwany rezultat:**  
1. Otwiera się strona logowania  
2. Login i hasło zostają wpisane  
3. Użytkownik zostaje prawidłowo zalogowany  
4. Przekierowanie do strony startowej, widoczna ikona użytkownika  

**Warunki końcowe:**  
- Zalogowanie do aplikacji, widoczna strona startowa z ikoną użytkownika  

---

## 1.2. Przypadki testowe podstrony dodawania samochodów

### ID: 006 — Dodawanie pojazdu bez podania danych
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości dodania pojazdu bez uzupełnienia danych  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik posiada konto  
- Użytkownik jest zalogowany  

**Kroki do reprodukcji:**  
1. Na pasku nawigacji kliknij „Baza pojazdów”  
2. Kliknij przycisk „Dodaj pojazd”  
3. W formularzu naciśnij przycisk dodaj  

**Oczekiwany rezultat:**  
1. Przekierowanie do podstrony vehicles  
2. Formularz „Dodaj nowy pojazd” otwiera się  
3. Przycisk dodaj jest nieaktywny  

**Warunki końcowe:**  
- Brak możliwości dodania pojazdu bez podania danych  

---

### ID: 007 — Dodawanie pojazdu bez uzupełnienia wymaganych pól
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości dodania pojazdu bez wypełnienia wymaganych pól  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik posiada konto  
- Użytkownik jest zalogowany  

**Kroki do reprodukcji:**  
1. Kliknij „Baza pojazdów”  
2. Kliknij przycisk „Dodaj pojazd”  
3. Wypełnij formularz pozostawiając wymagane pola puste  
4. Naciśnij przycisk dodaj  

**Oczekiwany rezultat:**  
1. Formularz otwiera się  
2. Pola zostają uzupełnione z wyłączeniem wymaganych  
3. Pojawia się komunikat: „Nazwa jest wymagana”  
4. Przycisk dodaj jest nieaktywny  

**Warunki końcowe:**  
- Brak możliwości dodania pojazdu bez uzupełnienia wymaganych pól  

---

### ID: 008 — Dodawanie pojazdu z wypełnieniem wyłącznie pól wymaganych
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości dodania pojazdu po uzupełnieniu wymaganych pól  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik posiada konto  
- Użytkownik jest zalogowany  

**Kroki do reprodukcji:**  
1. Kliknij „Baza pojazdów”  
2. Kliknij przycisk „Dodaj pojazd”  
3. Wypełnij tylko wymagane pola  
4. Naciśnij przycisk dodaj  

**Oczekiwany rezultat:**  
1. Formularz otwiera się  
2. Pola zostają uzupełnione  
3. Pojazd zostaje dodany do listy  
4. Komunikat: „Pomyślnie dodano pojazd”  

**Warunki końcowe:**  
- Możliwość dodania pojazdu, widoczność komunikatu  

---

### ID: 009 — Dodawanie pojazdu z nieistniejącym adresem
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości dodania pojazdu z nieistniejącymi danymi adresowymi  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik posiada konto  
- Użytkownik jest zalogowany  

**Kroki do reprodukcji:**  
1. Kliknij „Baza pojazdów”  
2. Kliknij przycisk „Dodaj pojazd”  
3. Wypełnij pola formularza losowymi danymi adresowymi  
4. Naciśnij przycisk dodaj  

**Oczekiwany rezultat:**  
1. Formularz otwiera się  
2. Pola zostają uzupełnione  
3. Pojazd zostaje dodany do listy  
4. Komunikat: „Pomyślnie dodano pojazd”  

**Warunki końcowe:**  
- Możliwość dodania pojazdu, widoczność komunikatu  

---

### ID: 010 — Dodawanie pojazdu z poprawnym adresem
**Autor:** AI  
**Środowisko:** Testowe  
**Przeglądarka:** Chrome 122.0.6261.129 (64-bit)  
**System:** Windows 10 22H2 190.454291  
**Cel:** Sprawdzenie możliwości dodania pojazdu z poprawnym adresem  

**Warunki wstępne:**  
- Uruchomiona przeglądarka  
- Użytkownik posiada konto  
- Użytkownik jest zalogowany  

**Kroki do reprodukcji:**  
1. Kliknij „Baza pojazdów”  
2. Kliknij przycisk „Dodaj pojazd”  
3. Wypełnij formularz poprawnymi danymi  
4. Naciśnij przycisk dodaj  

**Oczekiwany rezultat:**  
1. Formularz otwiera się  
2. Pola zostają uzupełnione  
3. Pojazd zostaje dodany do listy  
4. Komunikat: „Pomyślnie dodano pojazd”  

**Warunki końcowe:**  
- Możliwość dodania pojazdu, widoczność komunikatu  

---

**Uwagi:**  
- Testy mogą być uruchamiane na Chrome, Edge (124.0.2478.80), Firefox (125.0.3)  
- ID 009 i 010 w przyszłości będą rozszerzone o automatyczne sprawdzanie dokładności geokodowania
