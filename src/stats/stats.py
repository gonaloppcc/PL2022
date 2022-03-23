import statistics

from typing import List

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
    'name': 'Gender distribuition by year',
    'distrib': {}
} # Ano -> genero -> [M, F]


# Adds an exam to age_gender_distrib
def add_age_gender_distrib(exam):
    if exam['age'] < 35:
        if exam['gender'] == 'M':
            age_gender_distrib['distrib']["< 35"]['M'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
        else:
            age_gender_distrib['distrib']["< 35"]['F'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
    else:
        if exam['gender'] == 'M':
            age_gender_distrib['distrib'][">= 35"]['M'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
        else:
            age_gender_distrib['distrib'][">= 35"]['F'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))


# Adds an exam to location_distrib
def add_location_distrib(exam):
    if exam['location'] not in location_distrib.keys():
        location_distrib['distrib'][exam['location']] = [(exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport'])]
    else:
        location_distrib['distrib'][exam['location']].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))


def add_gender_per_year(exam):
    year = exam['date'].year
    if year not in gender_distrib_year['distrib'].keys():
        gender_distrib_year['distrib'][year] = {
            'M': [],
            'F': []
        }
    if exam['gender'] is 'M':
        gender_distrib_year['distrib'][year]['M'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
    else:
        gender_distrib_year['distrib'][year]['F'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))


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
