import random
import os

# ANSI escape codes for text formatting
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

europaen_countries = {
  "Albanien": "Tirana",
  "Andorra": "Andorra la Vella",
  "Österreich": "Wien",
  "Weißrussland": "Minsk",
  "Belgien": "Brüssel",
  "Bosnien und Herzegowina": "Sarajevo",
  "Bulgarien": "Sofia",
  "Kroatien": "Zagreb",
  "Zypern": "Nikosia",
  "Tschechische Republik": "Prag",
  "Dänemark": "Kopenhagen",
  "Estland": "Tallinn",
  "Finnland": "Helsinki",
  "Frankreich": "Paris",
  "Deutschland": "Berlin",
  "Griechenland": "Athen",
  "Ungarn": "Budapest",
  "Island": "Reykjavik",
  "Irland": "Dublin",
  "Italien": "Rom",
  "Lettland": "Riga",
  "Liechtenstein": "Vaduz",
  "Litauen": "Vilnius",
  "Luxemburg": "Luxemburg",
  "Malta": "Valletta",
  "Moldawien": "Chisinau",
  "Monaco": "Monaco",
  "Montenegro": "Podgorica",
  "Niederlande": "Amsterdam",
  "Nordmazedonien": "Skopje",
  "Norwegen": "Oslo",
  "Polen": "Warschau",
  "Portugal": "Lissabon",
  "Rumänien": "Bukarest",
  "Russland": "Moskau",
  "San Marino": "San Marino",
  "Serbien": "Belgrad",
  "Slowakei": "Bratislava",
  "Slowenien": "Ljubljana",
  "Spanien": "Madrid",
  "Schweden": "Stockholm",
  "Schweiz": "Bern",
  "Türkei": "Ankara",
  "Ukraine": "Kyiv",
  "Vereinigtes Königreich": "London",
  "Vatikanstadt": "Vatikanstadt"
}

all_world = {
  "Albanien": "Tirana",
  "Andorra": "Andorra la Vella",
  "Österreich": "Wien",
  "Weißrussland": "Minsk",
  "Belgien": "Brüssel",
  "Bosnien und Herzegowina": "Sarajevo",
  "Bulgarien": "Sofia",
  "Kroatien": "Zagreb",
  "Zypern": "Nikosia",
  "Tschechische Republik": "Prag",
  "Dänemark": "Kopenhagen",
  "Estland": "Tallinn",
  "Finnland": "Helsinki",
  "Frankreich": "Paris",
  "Deutschland": "Berlin",
  "Griechenland": "Athen",
  "Ungarn": "Budapest",
  "Island": "Reykjavik",
  "Irland": "Dublin",
  "Italien": "Rom",
  "Lettland": "Riga",
  "Liechtenstein": "Vaduz",
  "Litauen": "Vilnius",
  "Luxemburg": "Luxemburg",
  "Malta": "Valletta",
  "Moldawien": "Chisinau",
  "Monaco": "Monaco",
  "Montenegro": "Podgorica",
  "Niederlande": "Amsterdam",
  "Nordmazedonien": "Skopje",
  "Norwegen": "Oslo",
  "Polen": "Warschau",
  "Portugal": "Lissabon",
  "Rumänien": "Bukarest",
  "Russland": "Moskau",
  "San Marino": "San Marino",
  "Serbien": "Belgrad",
  "Slowakei": "Bratislava",
  "Slowenien": "Ljubljana",
  "Spanien": "Madrid",
  "Schweden": "Stockholm",
  "Schweiz": "Bern",
  "Türkei": "Ankara",
  "Ukraine": "Kyiv",
  "Vereinigtes Königreich": "London",
  "Vatikanstadt": "Vatikanstadt",
  "Afghanistan": "Kabul",
  "Ägypten": "Kairo",
  "Algerien": "Algier",
  "Angola": "Luanda",
  "Antigua und Barbuda": "Saint John's",
  "Äquatorialguinea": "Malabo",
  "Argentinien": "Buenos Aires",
  "Armenien": "Jerewan",
  "Aserbaidschan": "Baku",
  "Äthiopien": "Addis Abeba",
  "Australien": "Canberra",
  "Bahamas": "Nassau",
  "Bahrain": "Manama",
  "Bangladesch": "Dhaka",
  "Barbados": "Bridgetown",
  "Belize": "Belmopan",
  "Benin": "Porto-Novo",
  "Bhutan": "Thimphu",
  "Bolivien": "Sucre",
  "Botsuana": "Gaborone",
  "Brasilien": "Brasília",
  "Brunei": "Bandar Seri Begawan",
  "Burkina Faso": "Ouagadougou",
  "Burundi": "Gitega",
  "Cabo Verde": "Praia",
  "Chile": "Santiago de Chile",
  "China": "Peking",
  "Costa Rica": "San José",
  "Côte d'Ivoire": "Yamoussoukro",
  "Dominica": "Roseau",
  "Dominikanische Republik": "Santo Domingo",
  "Dschibuti": "Dschibuti",
  "Ecuador": "Quito",
  "El Salvador": "San Salvador",
  "Eritrea": "Asmara",
  "Fidschi": "Suva",
  "Gabun": "Libreville",
  "Gambia": "Banjul",
  "Ghana": "Accra",
  "Grenada": "Saint George's",
  "Guatemala": "Guatemala-Stadt",
  "Guinea": "Conakry",
  "Guinea-Bissau": "Bissau",
  "Guyana": "Georgetown",
  "Haiti": "Port-au-Prince",
  "Honduras": "Tegucigalpa",
  "Indien": "Neu-Delhi",
  "Indonesien": "Jakarta",
  "Irak": "Bagdad",
  "Iran": "Teheran",
  "Israel": "Jerusalem",
  "Jamaika": "Kingston",
  "Japan": "Tokio",
  "Jemen": "Sanaa",
  "Jordanien": "Amman",
  "Kambodscha": "Phnom Penh",
  "Kamerun": "Yaoundé",
  "Kanada": "Ottawa",
  "Kasachstan": "Nur-Sultan",
  "Katar": "Doha",
  "Kenia": "Nairobi",
  "Kirgisistan": "Bischkek",
  "Kiribati": "South Tarawa",
  "Kolumbien": "Bogotá",
  "Komoren": "Moroni",
  "Kongo": "Brazzaville",
  "Demokratische Republik Kongo": "Kinshasa",
  "Nordkorea": "Pjöngjang",
  "Südkorea": "Seoul",
  "Kosovo": "Pristina",
  "Kuba": "Havanna",
  "Kuwait": "Kuwait City",
  "Laos": "Vientiane",
  "Lesotho": "Maseru",
  "Liberia": "Monrovia",
  "Libyen": "Tripolis",
  "Madagaskar": "Antananarivo",
  "Malawi": "Lilongwe",
  "Malediven": "Male",
  "Mali": "Bamako",
  "Marokko": "Rabat",
  "Marschallinseln": "Majuro",
  "Mauretanien": "Nouakchott",
  "Mauritius": "Port Louis",
  "Mexiko": "Mexiko-Stadt",
  "Mikronesien": "Palikir",
  "Mongolei": "Ulan Bator",
  "Montenegro": "Podgorica",
  "Mosambik": "Maputo",
  "Myanmar": "Naypyidaw",
  "Namibia": "Windhoek",
  "Nauru": "Yaren",
  "Nepal": "Kathmandu",
  "Neuseeland": "Wellington",
  "Nicaragua": "Managua",
  "Niger": "Niamey",
  "Nigeria": "Abuja",
  "Nordmazedonien": "Skopje",
  "Oman": "Maskat",
  "Pakistan": "Islamabad",
  "Palästina": "Ramallah",
  "Panama": "Panama-Stadt",
  "Papua-Neuguinea": "Port Moresby",
  "Paraguay": "Asunción",
  "Peru": "Lima",
  "Philippinen": "Manila",
  "Ruanda": "Kigali",
  "St. Kitts und Nevis": "Basseterre",
  "St. Lucia": "Castries",
  "St. Vincent und die Grenadinen": "Kingstown",
  "Salomonen": "Honiara",
  "Sambia": "Lusaka",
  "Samoa": "Apia",
  "São Tomé und Príncipe": "São Tomé",
  "Saudi-Arabien": "Riad",
  "Senegal": "Dakar",
  "Seychellen": "Victoria",
  "Sierra Leone": "Freetown",
  "Simbabwe": "Harare",
  "Singapur": "Singapur",
  "Syrien": "Damaskus",
  "Somalia": "Mogadischu",
  "Südafrika": "Pretoria",
  "Süd السودان": "Juba",
  "Sri Lanka": "Sri Jayawardenepura Kotte",
  "Sudan": "Khartum",
  "Suriname": "Paramaribo",
  "Swasiland": "Mbabane",
  "Tadschikistan": "duschanbe",
  "Tansania": "Dodoma",
  "Thailand": "Bangkok",
  "Timor-Leste": "Dili",
  "Togo": "Lomé",
  "Tonga": "Nuku'alofa",
  "Trinidad und Tobago": "Port of Spain",
  "Tschad": "N'Djamena",
  "Tunesien": "Tunis",
  "Turkmenistan": "Aschgabat",
  "Tuvalu": "Funafuti",
  "Uganda": "Kampala",
  "Usbekistan": "Taschkent",
  "Vanuatu": "Port Vila",
  "Venezuela": "Caracas",
  "Vereinigte Arabische Emirate": "Abu Dhabi",
  "Vereinigte Staaten von Amerika": "Washington, D.C.",
  "Vietnam": "Hanoi",
  "Zentralafrikanische Republik": "Bangui"
}

countriesSelected = False
countries = europaen_countries



startInfo = f"""
{BOLD}
Hallo, \n\nschön, dass Du dieses Quiz spielst. Was möchtest Du testen ? \n
Europäische Länder und ihre Hauptstädte? --> drücke [1]
Alle Länder der Welt und ihre Hauptstädte? --> drücke [2]\n\n
Bitte wähle entweder 1 (für europäische Länder) oder 2 (für alle Länder der Welt).
{RESET}
"""

# clear the console first
clear_console()

print(startInfo)

while not countriesSelected:
    user_choice = input()
    
    match(user_choice):
        case '1':
            print(f"{GREEN}Okay. Prüfen wir die europäischen Länder.{RESET}")
            countries = europaen_countries
            countriesSelected = True
        case '2':
            print(f"{GREEN}Eine tolle Herausforderung. Du möchtest alle Länder der Welt prüfen.{RESET}")
            countries = all_world
            countriesSelected = True
        case _:
            # do nothing
            print(f"{RED}Ungültige Eingabe. Bitte wähle 1 oder 2.\n{RESET}")
            

print(f"{BOLD}Fangen wir an.  Viel Erfolg :-) !\n\n{RESET}")
country_names = list(countries.keys())
countriesAlreadyAsked = set()

points = 0

for i in range(5):
    while True:
        country = random.choice(country_names)
        if country not in countriesAlreadyAsked:
            countriesAlreadyAsked.add(country)
            break

    capital = countries[country]
    capital_guess = input(f"{YELLOW}Was ist die Hauptstadt von {country} ? : {RESET}")
    if(capital_guess == capital):
        print(f"{GREEN}Super. Das ist richtig :-) !{RESET}")
        points += 1
    else:
        print(f"{RED}Das ist leider falsch. Die Hauptstadt von {country} ist {capital}.{RESET}")
    
    print("\n---------------\n")

print(f"{BLUE}Du hast {points} von 5 Fragen richtig beantwortet.\n\n{RESET}")