from stats.Statistic import Statistic


class GenderByYear(Statistic):
    def __init__(self):
        super().__init__()
        self.set_name('Gender distribution by year')

    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        sport = exam['sport']
        gender = exam['gender']
        year = exam['date'].year

        athlete = {
            'id': identifier,
            'name': name,
            'sport': sport
        }

        if year not in self.get_data().keys():
            self._data[year] = {
                'M': [],
                'F': []
            }
            self._stats[year] = {
                'M': 0,
                'F': 0
            }

        self._data[year][gender].append(athlete)
        self._stats[year][gender] += 1

    def print_data(self):
        s = ''
        for year, genders in self.get_data().items():
            s += f'<h1>{year}</h1>\n'

            s += '<h2>M</h2>\n'
            s += '<ul>\n'
            for athlete in genders['M']:
                s += f'<li>{athlete["id"]} - {athlete["name"]} -- {athlete["sport"]}</li>\n'
            s += '</ul>\n'

            s += '<h2>F</h2>\n'
            s += '<ul>\n'
            for athlete in genders['F']:
                s += f'<li>{athlete["id"]} - {athlete["name"]} -- {athlete["sport"]}</li>\n'
            s += '</ul>\n'

        return s

    def print_stats(self):
        s = ''
        for year, genders in self.get_stats().items():
            s += f'<h3>{year}</h3>\n'
            s += '<ul>\n'
            s += f'<li>M -> {genders["M"]}</li>\n'
            s += f'<li>F -> {genders["F"]}</li>\n'
            s += '</ul>\n'

        return s
