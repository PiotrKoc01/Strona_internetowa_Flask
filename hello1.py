from flask import Flask, render_template, flash, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wrozba import wrozba
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time






#rozpoczynamy integracje twojej matki
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#hasłooo
app.config['SECRET_KEY'] = 'hfijejsiovov'
#inicjacja bazy danych
db = SQLAlchemy(app)

#model do bazy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name

#Class Form
class HelloForm(FlaskForm):
    name = StringField('Podaj nick, aby przejsć do czatu', validators=[DataRequired(), Length(max= 40)] )
    submit = SubmitField('Ależ chcę poczatować o Sylwku, aż mnie świerzbi!')

#ś
#adresik
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<name>')

def user(name):
    return render_template('user.html',name=name)

#własna strona Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
#własna strona ertenal Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
#namepage
@app.route('/name', methods=['GET', 'POST'])
def name():
    name= None
    form = HelloForm()
    #walidacja
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if name.lower() in ["kurwa", "pizda", "jebany", "chuj", "cipa", "jebane", "chujowy", "jebac", "jebać"]:
            while True:
                flash("Weryfikacja nie przeszła po myśli, bo wygląda na to, że ktoś tu nie umie się zachować.")
                return render_template('przeklenstwa.html', name=name, form=form)
        flash("Weryfikacja nazwy przebiegła prawidłowo. Pamiętaj, aby zachować podstawowe zasady kultury na czacie. :3")

    return render_template('name.html', name=name, form=form)

@app.route('/wrozka')
def wrozka():
    while True:
        losowa_wrozba = random.choice(wrozba)
        return render_template('wrozka.html', wrozba=losowa_wrozba)

@app.route('/konkurs')
def konkurs():
    return render_template('konkurs.html')
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')
@app.route('/o_nas')
def o_nas():
    return render_template('o nas.html')
@app.route('/pogadanka')
def pogadanka():
    return render_template('pogadaj.html')
@app.route('/submit', methods= ["POST"])
def submit():
    input_text = request.form['input_text']
    odpowiedz = generate_response(input_text)
    return jsonify({'odpowiedz': odpowiedz})

def generate_response(wpis):
    if any(slowo in wpis.lower() for slowo in ["hej", "siema", "witam", "siema", "joł", "hejka", "dzień dobry"]):
        return random.choice(["No dzień dobry, jak tam dzień mija?", "No co tam u Ciebie słońce?",
                              "Mój kebab był dobry. Mam nadzieje, że masz dobry dzień", "Witam, jak tam życie w tym pierdolniku", "O a kto to przyszedł! Daj buziaka! Jak się czujesz?",
                              "Co przeszkadzasz jem kebaba"])
    elif wpis.lower() in ["nie", "nie kupię", "nie kupie", "nje"]:
        return random.choice(["Niezgoda kebaba kupionego nie czyni, więc lepiej się popraw",
                              "Jeszcze raz się nie zgodzisz to ja nie zgodzę się z twoim życiem",
                              "To samo powiedziała Twoja mama jak się zapytałem czy jesteś jej dzieckiem"])
    elif "czy" in wpis.lower() and "ja" in wpis.lower():

        wpis_splitted = wpis.split()
        wpis_splitted[-1] = wpis_splitted[-1].replace("?", "")
    #elif "czy" in wpis.lower():
        #wpis_splitted = wpis.split()


        return random.choice([f"Wydaje mi się, że Ty", f"to zdecydowanie {wpis_splitted[-1]}"])
    elif len(wpis) > 90:
        return "Nie chce mi się tyle czytać. Lepiej nie marnuj energi na pisanie, zamiast tego chodź kup mi kebaba."
    elif wpis.lower() in ["co?", "co"]:
        return random.choice([f"To nie jest tak, że ja Ciebie nie rozumiem. To Ty nie rozumiesz mnie", f'istnieje {random.randint(1,5)} powodów, abys siedział cicho', 'Pstro. Naprawdę zmieńmy temat', 'NIC'])
    elif "co" in wpis.lower() and "?" in wpis.lower():
        return random.choice(
            ["Irytuje mnie ten temat", "Nie chcę się wypowiadać, bo nie lubię przeklinać", "NIENAWIDZĘ TEGO",
             "Nie sądzę na ten temat nic pozytywnego", "KOCHAM"])
    elif "jak" in wpis.lower() and "?" in wpis.lower():
        return random.choice(["Dobrze", "Rewelacyjnie", "Niezbyt Sylwkastycznie ;(", "Nie no git, tylko się wywróciłem na chodniku", "Ból jest nie do zniesienia"])

    elif any(slowo in wpis.lower() for slowo in ["sorry", "przepraszam", "wybacz", "sorki"]):
        return random.choice(["No uważaj sobie!", "Uważaj! Znam sumo!", "Chyba masz za wiele zębów kolego!"])
    elif any(slowo in wpis.lower() for slowo in ["chyba ty", "uspokój się", "wypierdalaj", "uważaj", "nic ci nie"]):
        return random.choice(["Nie", "Słuchaj, nie fajnie się zachowujesz", "Jesteś dziadem i tyle",
                              "Skończysz jak sos mieszany- na moich majtach", "Ale mnie denerwujesz! Jak przeterminowany kebab (potem boli mnie brzuszek)"])
    elif any(slowo in wpis.lower() for slowo in ["dobrze", "fajnie", "miło", "wspaniale", "super"]):
        return random.choice(
            ["Lubię jak jest pozytywnie. Kupisz mi kebaba", "Jak masz taki dobry humor może kup mi kebsa",
             "Cieszę się! Ale ucieszę się bardziej jak kupisz mi kebsa!"])
    elif any(slowo in wpis.lower() for slowo in ["ile", "iloma"]):
        return random.choice([f'Nie lubię operacji na liczbach, wole na kebabach ale powiem {random.randint(1,100)}', f'Nie znam się na liczbach, ale to będzie koło {random.randint(1,100)}'])
    elif wpis.lower() in (["nudy", "nudno", "nudzę", "nudze"]):
        return random.choice(
            ["To może kup mi kebaba dla rozrywki!", "Jak to możliwe, że taka śliczna osoba jak Ty się nudzi!",
             "Mi jak się nudzi to rzucam w wykładowców skarpetami!"])

    elif any(slowo in wpis.lower() for slowo in ["źle", "nie dobrze", "smutno", "tak sobie", "średnio"]):
        return random.choice(["A co się stało?", "Wszystko git?"])
    elif any(slowo in wpis.lower() for slowo in ["spierdalaj", "wypierdalaj", "sam sie", "sam się"]):
        return random.choice(
            ["Mnie nie zdenerwujesz. Jestem buddysta, smoczy wojownik.", "Oj spójrz tylko na siebie. Denerwujesz się",
             "Ale nerwus!", "Ciekawe, że tak mówisz"])
    elif any(slowo in wpis.lower() for slowo in ["a ty?", "a twój?", "co tam?", "a tobie?", "u "]):
        return random.choice(["Sylwkastycznie", "Fajnie", "Nie no git", 'To samo co u Ciebie'])
    elif any(slowo in wpis.lower() for slowo in ["czemu", "dlaczego"]):
        return random.choice(["Wyjasnie Ci jak mi kupisz kebaba", "Kociej mordy dostaniesz", "Jezus jestes dociekliwy, jak turek, kiedy zamówiłem kebaba na ludzkim mięsie"])
    elif any("?" in wpis.lower() for wpis in wpis):
        return random.choice(["Tak", "Zdecydowanie tak", "JESZCZE JAK", "Oj nie nie", "NIE"])


    elif any(slowo in wpis.lower() for slowo in ["tak"]):
        return random.choice(["Srak", "tak to znaczy jak?"])
    else:
        return random.choice([
            "Wiedziałem, że jesteś dziwny, ale nie, że aż tak!",
            "Co Ty w ogóle do mnie piszesz",
            "Zamknij morde",
            "Ty tak do mnie?",
            "Nie mam pojęcia, o czym mówisz",
            "Smutno mi przez Ciebie",
            "Zasmucasz mnie",
            "Będzie mi przykro i to przez Ciebie",
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
            "Wyglądasz znajomo. Czy nie chodziliśmy razem na zajęcia? Mógłbym przysiąc, że wyczuwam między nami kebsa.",
            "Naprawdę cieszę się, że właśnie kupiłem ubezpieczenie na życie, bo kiedy cię zobaczyłem, moje serce stanęło.",
            "Chcę, żeby nasza miłość była jak sos mieszany. Zawsze ląduje mi na majtach",
            "Trujesz dupe",
            "Czy jest coś, co chciałbyś mnie zapytać? Jak nie to sobie idź",
            "Nudzi Ci się?",
            "Możemy porozmawiać o czymkolwiek, co Cię interesuje. Dobra jaja sobie robię"
        ])

if __name__ == '__main__':
    app.run(debug=True)