import random

class Pogadanka:
    def odpowiedz(wpis):
        if any(slowo in wpis.lower() for slowo in ["hej", "siema", "witam", "siema", "joł", "hejka", "dzień dobry"]):
            return random.choice(["No dzień dobry, jak tam dzień mija?", "No co tam u Ciebie słońce?", "Mój kebab był dobry, a jak tam Twój?", "Witam, jak dzień? Kupisz mi kebaba", "Co przeszkadzasz jem kebaba"])
        elif wpis.lower() in ["nie", "nie kupię", "nie kupie", "nje", "nic ci nie kupie", "nie kupie ci", "nie kupię", "nic ci nie kupię"]:
            return random.choice(["Niezgoda kebaba kupionego nie czyni, więc lepiej się popraw", "Jeszcze raz się nie zgodzisz to ja nie zgodzę się z twoim życiem",
                                  "To samo powiedziała Twoja mama jak się zapytałem czy jesteś jej dzieckiem"])
        elif len(wpis) > 50:
            return "Nie chce mi się tyle czytać. Lepiej nie marnuj energi na pisanie, zamiast tego chodź kup mi kebaba."
        elif any(slowo in wpis.lower() for slowo in ["sorry", "przepraszam", "wybacz", "sorki"]):
            return random.choice(["No uważaj sobie!", "Uważaj! Znam sumo!", "Chyba masz za wiele zębów kolego!"])
        elif any(slowo in wpis.lower() for slowo in ["chyba ty", "uspokój się", "wypierdalaj", "uważaj"]):
            return random.choice(["Nie", "Słuchaj, nie fajnie się zachowujesz", "Jesteś dziadem i tyle", "Skończysz jak sos mieszany- na moich majtach"])
        elif any(slowo in wpis.lower() for slowo in ["dobrze", "fajnie", "miło", "wspaniale", "super"]):
            return random.choice(["Lubię jak jest pozytywnie. Kupisz mi kebaba", "Jak masz taki dobry humor może kup mi kebsa", "Cieszę się! Ale ucieszę się bardziej jak kupisz mi kebsa!"])
        elif wpis.lower() in (["nudy", "nudno", "nudzę", "nudze"]):
            return random.choice(["To może kup mi kebaba dla rozrywki!", "Jak to możliwe, że taka śliczna osoba jak Ty się nudzi!", "Mi jak się nudzi to rzucam w wykładowców skarpetami!"])
        elif any(slowo in wpis.lower() for slowo in ["źle", "nie dobrze", "smutno"]):
            return random.choice(["A co się stało?", "Wszystko git?"])
        elif any(slowo in wpis.lower() for slowo in ["spierdalaj", "wypierdalaj"]):
            return random.choice(["Mnie nie zdenerwujesz. Jestem buddysta, smoczy wojownik.", "Oj spójrz tylko na siebie. Denerwujesz się",
                                  "Ale nerwus!", "Ciekawe, że tak mówisz"])
        elif any(slowo in wpis.lower() for slowo in ["a ty?", "a twój?", "co tam?", "a tobie?", "u "]):
            return random.choice(["Sylwkastycznie", "Fajnie", "Nie no git"])
        elif any("?" in wpis.lower() for wpis in wpis):
            return random.choice(["Tak", "Zdecydowanie tak", "JESZCZE JAK", "Oj nie nie", "NIE"])
        elif any(slowo in wpis.lower() for slowo in ["tak"]):
            return "Srak"
        else:
            return random.choice([
                "Wiedziałem, że jesteś dziwny, ale nie, że aż tak!",
                "Co Ty w ogóle do mnie piszesz",
                "Zamknij morde",
                "Ty tak do mnie?",
                "Nie mam pojęcia, o czym mówisz",
                "Hmm, ciekawe, że to napisałeś",
                "Powiedziałeś coś? Nic nie słyszę",
                "Czy to jest język, który próbujesz mówić?",
                "Mój kebab się przegrzewa od takich głupot",
                "Mój ulubiony kolor to kebab",
                "Masz jakieś plany na dzisiaj? Chcesz ze mną pójść spędzić romantyczne chwile?",
                "Pierdolisz farmazony",
                "Nie jestem pewien, czy to jest seksowne",
                "Twój tato musi być z zawodu złodziejem, bo ukradł wszystkie kebaby z Turcji i umieścił w twoich cudnych oczkach.",
                "Wiesz, że jestem botem, prawda? Za to nie jestem jak Ty debilem!",
                "Gdzie jest policja? Bo kradniesz właśnie moje serce. Całe szczęście nie kebsa",
                "Możesz opowiedzieć mi jakąś historię?",
                "Lubisz kebaby?",
                "Wyglądasz znajomo. Czy nie chodziliśmy razem na zajęcia? Mógłbym przysiąc, że wyczuwam między nami kebsa.",
                "Naprawdę cieszę się, że właśnie kupiłem ubezpieczenie na życie, bo kiedy cię zobaczyłem, moje serce stanęło.",
                "Chcę, żeby nasza miłość była jak sos mieszany. Zawsze ląduje mi na majtach",
                "Jakie są Twoje ulubione kebaby",
                "Trujesz dupe",
                "Czy jest coś, co chciałbyś mi zapytać? Jak nie to sobie idź",
                "Nudzi Ci się?",
                "Możemy porozmawiać o czymkolwiek, co Cię interesuje. Dobra jaja sobie robię"
            ])


