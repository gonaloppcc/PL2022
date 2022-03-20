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
    "< 35":{
        "M": [],
        "F": []
    },
    ">= 35": {
        "M": [],
        "F": []
    }
}

location_distrib = {}

# Adds an exam to age_gender_distrib
def add_age_gender_distrib(exam):
    if exam['age'] < 35:
        if exam['gender'] == 'M':
            age_gender_distrib["< 35"]['M'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
        else:
            age_gender_distrib["< 35"]['F'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
    else:
        if exam['gender'] == 'M':
            age_gender_distrib[">= 35"]['M'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))
        else:
            age_gender_distrib[">= 35"]['F'].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))

# Adds an exam to location_distrib
def add_location_distrib(exam):
    if exam['location'] not in location_distrib.keys():
        location_distrib[exam['location']] = [(exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport'])]
    else:
        location_distrib[exam['location']].append((exam['id'], f"{exam['fname']} {exam['lname']}", exam['sport']))


def get_stats(path: str):
    exams = parse_emd(path)

    # Temporary code to check if the parsing works
    # for exam in exams:
    # print(f'{exam["fname"]} {exam["lname"]}: {exam["email"]}')

    print('Data loaded!')

    # (a)

    # (b)
    b_stats = gender_per_year(exams)

    for exam in exams:
        add_age_gender_distrib(exam)
        add_location_distrib(exam)

    return b_stats


def gender_per_year(exams: List[dict]):
    gender_distrib_year = {}  # Ano -> genero -> [M, F]

    for exam in exams:
        year = exam['date'].year
        if year not in gender_distrib_year.keys():
            gender_distrib_year[year] = [0, 0]

        else:
            if exam['gender'] == 'M':
                gender_distrib_year[year][0] += 1
            else:
                gender_distrib_year[year][1] += 1

    for genders in gender_distrib_year.values():
        total = genders[0] + genders[1]
        genders[0] /= total
        genders[1] /= total

    return gender_distrib_year
