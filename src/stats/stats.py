from csv_parser.parser import parse_emd
from stats.ResultByYear import ResultByYear
from stats.GenderByYear import GenderByYear
from stats.LocationDistrib import LocationDistrib
from stats.FederatedByYear import FederatedByYear
from stats.AgeGenderDistrib import AgeGenderDistrib
from stats.SportByYear import SportByYear

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

statistics = {
    'age_gender_distrib': AgeGenderDistrib(),
    'federated_by_year': FederatedByYear(),
    'sport_by_year': SportByYear(),
    'location_distrib': LocationDistrib(),
    'gender_by_year': GenderByYear(),
    'result_by_year': ResultByYear()
}


def get_stats(path: str):
    exams = parse_emd(path)

    # Temporary code to check if the parsing works
    # for exam in exams:
    # print(f'{exam["fname"]} {exam["lname"]}: {exam["email"]}')

    print('Data loaded!')

    # (a)

    # (b)

    for exam in exams:
        statistics['age_gender_distrib'].add_elem(exam)
        statistics['federated_by_year'].add_elem(exam)
        statistics['sport_by_year'].add_elem(exam)
        statistics['location_distrib'].add_elem(exam)
        statistics['gender_by_year'].add_elem(exam)
        statistics['result_by_year'].add_elem(exam)