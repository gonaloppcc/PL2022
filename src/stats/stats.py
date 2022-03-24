from csv_parser.parser import parse_emd

'''
1. Página principal: de nome "index.html", contendo os seguintes indicadores estatísticos:
(a) Datas extermas dos registos no dataset;
(b) Distribuição por género em cada ano e no total;
(c) Distribuição por modalidade em cada ano e no total;
(d) Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35);
(e) Distribuição por morada;
(f) Distribuição por estatuto de federado em cada ano;
(g) Percentagem de aptos e não aptos por ano
'''

'''
# Defined variables from the dataset:
# exams -> List with all exams (a exam is a dictionary)
# exams[1] -> Index 1 exam
# exams[1][attribute] -> Gets the attribute from the index 1 exam

# Attributes:
# id
# index
# date
# fname (first name)
# lname (lastname)
# age
# gender
# location
# sport
# club
# email
# federated
# result

'''

age_gender_distrib = {
    'name': 'Gender Distribution by age',
    'distrib': {
        '< 35': {
            'M': [],
            'F': []
        },
        '>= 35': {
            'M': [],
            'F': []
        }
    }
}

location_distrib = {
    'name': 'Location distribution',
    'distrib': {}
}

gender_distrib_year = {
    'name': 'Gender distribution by year',
    'distrib': {}
} # Ano -> genero -> [M, F]

sport_distrib_year = {
    'name': 'Sport distribution by year and total',
    'distrib': {}
}

federated_by_year = {
    'name': 'Federated by year',
    'distrib': {}
}


# Adds an exam to age_gender_distrib
def add_age_gender_distrib(exam):
    identifier = exam['id']
    name = f'{exam["fname"]} {exam["lname"]}'
    sport = exam['sport']

    if exam['age'] < 35:
        if exam['gender'] == 'M':
            age_gender_distrib['distrib']["< 35"]['M'].append((identifier, name, sport))
        else:
            age_gender_distrib['distrib']["< 35"]['F'].append((identifier, name, sport))
    else:
        if exam['gender'] == 'M':
            age_gender_distrib['distrib'][">= 35"]['M'].append((identifier, name, sport))
        else:
            age_gender_distrib['distrib'][">= 35"]['F'].append((identifier, name, sport))


# Adds an exam to location_distrib
def add_location_distrib(exam):
    identifier = exam['id']
    name = f'{exam["fname"]} {exam["lname"]}'
    sport = exam['sport']
    location = exam['location']

    if location not in location_distrib.keys():
        location_distrib['distrib'][location] = [(identifier, name, sport)]
    else:
        location_distrib['distrib'][location].append((identifier, name, sport))


def add_gender_per_year(exam):
    identifier = exam['id']
    name = f'{exam["fname"]} {exam["lname"]}'
    sport = exam['sport']
    gender = exam['gender']
    year = exam['date'].year

    if year not in gender_distrib_year['distrib'].keys():
        gender_distrib_year['distrib'][year] = {
            'M': [],
            'F': []
        }

    if gender == 'M':
        gender_distrib_year['distrib'][year]['M'].append((identifier, name, sport))
    else:
        gender_distrib_year['distrib'][year]['F'].append((identifier, name, sport))


def add_sport_distrib_year(exam):
    year = exam['date'].year
    identifier = exam['id']
    name = f'{exam["fname"]} {exam["lname"]}'
    sport = exam['sport']

    if year not in sport_distrib_year['distrib'].keys():
        sport_distrib_year['distrib'][year] = {
            sport: [(identifier, name, sport)]
        }
    else:
        if sport not in sport_distrib_year['distrib'][year].keys():
            sport_distrib_year['distrib'][year][sport] = [(identifier, name, sport)]
        else:
            sport_distrib_year['distrib'][year][sport].append((identifier, name, sport))


def add_federated_by_year(exam):
    identifier = exam['id']
    name = f'{exam["fname"]} {exam["lname"]}'
    sport = exam['sport']
    year = exam['date'].year
    federated = exam['federated']

    if year not in federated_by_year['distrib'].keys():
        federated_by_year['distrib'][year] = {
            True: [],
            False: []
        }

    federated_by_year['distrib'][year][federated].append((identifier, name, sport))


def get_stats(path: str):
    exams = parse_emd(path)

    # Temporary code to check if the parsing works
    # for exam in exams:
    # print(f'{exam["fname"]} {exam["lname"]}: {exam["email"]}')

    print('Data loaded!')

    # (a)

    # (b)

    for exam in exams:
        add_age_gender_distrib(exam)
        add_location_distrib(exam)
        add_gender_per_year(exam)
        add_sport_distrib_year(exam)
        add_federated_by_year(exam)
