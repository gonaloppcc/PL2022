import statistics

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


def get_stats(path: str):
    athletes = parse_emd(path)

    # Temporary code to check if the parsing works
    # for athlete in athletes:
    # print(f'{athlete["fname"]} {athlete["lname"]}: {athlete["email"]}')

    print('Data loaded!')

    # (a)

    # (b)
    gender_distrib_year = {}  # Ano -> genero -> [M, F]
    for athlete in athletes:
        year = athlete['date'].year
        if year not in gender_distrib_year.keys():
            gender_distrib_year[year] = [0, 0]

        else:
            if athlete['gender'] == 'M':
                gender_distrib_year[year][0] += 1
            else:
                gender_distrib_year[year][1] += 1

    for genders in gender_distrib_year.values():
        total = genders[0] + genders[1]
        genders[0] /= total
        genders[1] /= total


    return gender_distrib_year
