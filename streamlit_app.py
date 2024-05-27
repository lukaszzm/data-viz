# interactive map on a website
import streamlit as st
from streamlit_option_menu import option_menu # pip install streamlit-option-menu
import streamlit.components.v1 as components

with open('html/table.html', 'r')  as table_file, open("html/map.html", 'r') as map_file:
    table = table_file.read()
    map_r = map_file.read()

# Sidebar menu:
with st.sidebar:
    selected = option_menu(
        menu_title="Menu", 
        options=["Wprowadzenie, definicje", 'Mapa interaktywna', "Tabela danych", "Sytuacja w Polsce"],
        icons=['house', 'bi-file-text', 'bi-bar-chart', 'gear'],
        menu_icon="bi-menu-button", 
        default_index=0
    )

# st.image() instead of st.pyplot() now!
if selected == "Wprowadzenie, definicje":
    st.header("Zdrowie psychiczne w Polsce i na świecie", divider='rainbow')
    st.markdown("Obracając się w tematyce zdrowia i lekarzy, chcieliśmy zwrócić uwagę na problem, jakim jest zdrowie psychiczne, często niesłusznie pomijane przy rozmowach o kondycji ochrony zdrowia w krajach i na świecie. Do swojej analizy użyliśmy danych pochodzących ze stron internetowych, raportów i artykułów. Szczegółowe informacje przytaczane są w momencie pojawiania się informacji.");
    st.subheader("Analiza wybranych czynników i ich wpływ na liczbę samobójstw w krajach świata")
    st.markdown("Postanowiliśmy zacząć od zestawienia ze sobą wybranych czynników, zilustrowania wyników i próby zaobserwowania wzorców. Do analizy użyliśmy:")

    st.markdown(" - **health rank** - indeks opieki zdrowotnej według magazynu CEOWorld jako analiza statystyczna ogólnej jakości systemu opieki zdrowotnej, w tym infrastruktury opieki zdrowotnej; kompetencji pracowników służby zdrowia (lekarzy, personelu pielęgniarskiego i innych pracowników służby zdrowia), kosztów (USD rocznie na mieszkańca); dostępności leków wysokiej jakości i gotowości rządu.")
    st.link_button("Źródło", "https://worldpopulationreview.com/country-rankings/best-healthcare-in-the-world")

    st.markdown(" - **median income** - wskaźnik używany do określenia punktu środkowego rozkładu dochodów w danym kraju.")
    st.link_button("Źródło", "https://worldpopulationreview.com/country-rankings/median-income-by-country")

    st.markdown(" - **suicide rate** - współczynnik liczby samobójstw na 100 tysięcy mieszkańców w danym kraju.")
    st.link_button("Źródło", "https://worldpopulationreview.com/country-rankings/suicide-rate-by-country")

    st.markdown(" - **result** - nasz własny czynnik opracowany na podstawie poniższego wzoru:")

    st.latex(r'''
    result = (healthRank + medianIncome) / suicideRate
    ''')

    st.markdown("Przygotowane dane pochodzą z różnych źródeł i zbierane zostały w różnych okresach, "
                "dlatego ta analiza nie jest w sobie wiarygodna, daje jednak możliwość prezentacji poszczególnych wyników.")

elif selected == "Mapa interaktywna":
    st.header("Interaktywna mapa ukazująca rezultaty z podziałem na kraje", divider='rainbow')
    st.markdown("Zebrane informacje postanowiliśmy nanieść na mapę świata:")
    st.text("Najedź kursorem na wybrany kraj, żeby zobaczyć dokładny wynik. ")

    components.html(map_r, width=700, height=380)

    st.text("Ciemniejszy kolor oznacza wyższy rezultat* ")


elif selected == "Tabela danych":
    st.header("Tabela przedstawiająca wyniki", divider='rainbow')
    st.subheader("Ponadto, można przeglądać dane również w postaci listy. Klikając na wybrany parametr możemy odpowiednio posortować wyniki.")

    components.html(table, width=700, height=7600)

    st.markdown("Co możemy wyczytać z tych danych? Z pewnością pierwszym wnioskiem jest refleksja, "
                "że tak złożony problem jak zdrowie psychiczne i samobójstwa to zbyt złożony problem by wytłumaczyć go za pomocą dwóch czynników. "
                "Choć intuicja podpowiada, że w krajach z wysokimi dochodami i dobrą służbą zdrowia wskaźnik samobójstw będzie najniższy, **jest to złudne.**")
    st.markdown("Przykładem na to może okazać się Norwegia. Leżąca w skandynawskiej krainie szczęścia:")
    st.link_button("Norwegia - najszczęśliwszy kraj na ziemi [artykuł]", " https://www.national-geographic.pl/traveler/artykul/znamy-wyniki-world-happiness-report-2022-do-najszczesliwszego-kraju-dolecimy-z-polski-w-niecale-2-godziny-220318121627")

    st.markdown(", choć pozornie wydaje się miejscem idealnym, dane tego nie potwierdzają. Piąte miejsce od góry jeśli chodzi o dochód, piąte miejsce gdy mówimy o jakości służby zdrowia. I miejsce 109 na 148, gdy spojrzymy na państwa z najmniejszą ilością samobójstw. O tym problemie w Norwegii mówi się od lat:")
    st.link_button("Norwegia - wciąż więcej osób popełnia samobójstwo niż ginie na drogach [artykuł]", "https://www.mojanorwegia.pl/aktualnosci/kraj-nieszczesliwych-ludzi-w-norwegii-wciaz-wiecej-osob-popelnia-samobojstwo-niz-ginie-na-jezdni-15821.html")

    st.markdown("I choć sytuacja się poprawia, dane wciąż są bezlitosne.")

elif selected == "Sytuacja w Polsce":
    st.header("Jak to wygląda w Polsce?", divider='rainbow')
    st.markdown(" Z artykułów od dawna możemy usłyszeć, że sytuacja nie jest dobra. Na liście pod względem liczby samobójstw jesteśmy ledwo nad Norwegią, "
                "bo na 103 miejscu, z liczbą 11 samobójstw na 100 000 mieszkańców. "
                "To może prowadzić nas do refleksji, co w takim razie może mieć jeszcze istotny wpływ na liczbę samobójstw, "
                "oraz jak możemy dokładać starań aby ją skutecznie zmniejszać.")

    st.subheader("Liczba psychiatrów w Polsce")

    st.markdown("Choć ciężko dotrzeć do nowszych danych, możemy na podstawie dostępnych danych zauważyć, że sektor psychologii i psychiatrii w Polsce wymaga poprawy. "
                "Jak podaje fundacja GROW Space [4], średni czas oczekiwania na konsultację psychiatry dziecięcego w Polsce w roku 2023 wynosił 237 dni. "
                "Dla ilustracji, to 237 dni:")
    st.image('images/calendar.png')

    st.markdown("Jest to spowodowane między innymi niewystarczającą liczbą specjalistów. "
                "Według danych z [5], w Polsce w 2016 roku na 100 000 mieszkańców przypadało… 24 psychiatrów.")
    st.image('images/psychiatrists.png')

    st.markdown("Czy większa ich liczba polepszyłaby aktualną sytuację? Można tak sądzić. Czy jest o co walczyć? **Zdecydowanie.**")

    st.markdown("Poniższa grafika przedstawia liczbę prób samobójczych (2193) w Polsce wśród dzieci i młodzieży do 18 roku życia. Czarne punkty symbolizują próby, które okazały się skuteczne (146). [6]")
    st.image("images/suicides.png")

    st.markdown("Problem zdrowia psychicznego czy liczby samobójstw jest zbyt złożony aby wysunąć konkretne założenia co należałoby zmienić, aby sytuację naprawić, lecz można i należy dokładać wszelkich starań, bo każdy z nas pragnie żyć w zdrowym i szczęśliwym społeczeństwie.")

    st.subheader("Źródła:")

    st.markdown("1. [World Population Review - Healthcare](https://worldpopulationreview.com/country-rankings/best-healthcare-in-the-world)")
    st.markdown("2. [World Population Review - Median Income](https://worldpopulationreview.com/country-rankings/median-income-by-country)")
    st.markdown("3. [World Population Review - Suicide Rate](https://worldpopulationreview.com/country-rankings/suicide-rate-by-country)")
    st.markdown("4. [Grow Space](https://pulsmedycyny.pl/rekordowe-kolejki-do-psychiatrow-dzieciecych-w-jednej-z-placowek-na-wizyte-trzeba-poczekac-do-2030-r-1194540)")
    st.markdown("5. [Dane WHO](https://www.who.int/data/gho/data/themes/mental-health/suicide-rates)")
    st.markdown("6. [Grow Space 2](https://politykazdrowotna.com/artykul/rekordowa-liczba-samobojstw/1214006)")