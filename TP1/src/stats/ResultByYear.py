from stats.Statistic import Statistic


class ResultByYear(Statistic):
    def __init__(self):
        super().__init__()
        self.set_name('Result distribution by year')

    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        sport = exam['sport']
        result = exam['result']
        year = exam['date'].year

        athlete = {
            'id': identifier,
            'name': name,
            'sport': sport
        }

        if year not in self.get_data().keys():
            self._data[year] = {
                True: [],
                False: []
            }
            self._stats[year] = {
                True: 0,
                False: 0
            }

        self._data[year][result].append(athlete)
        self._stats[year][result] += 1

    def print_data(self):
        s = ''
        for year, results in self.get_data().items():
            s += f'<h1>{year}</h1>\n'

            s += '<h2>True</h2>\n'
            s += '<ul>\n'
            for athlete in results[True]:
                s += f'<li>{athlete["id"]} - {athlete["name"]} -- {athlete["sport"]}</li>\n'
            s += '</ul>\n'

            s += '<h2>False</h2>\n'
            s += '<ul>\n'
            for athlete in results[False]:
                s += f'<li>{athlete["id"]} - {athlete["name"]} -- {athlete["sport"]}</li>\n'
            s += '</ul>\n'

        return s

    def print_stats(self):
        s = ''
        for year, results in self.get_stats().items():
            s += f'<h3>{year}</h3>\n'
            s += '<ul>\n'
            s += f'<li>Positive -> {results[True]}</li>\n'
            s += f'<li>Negative -> {results[False]}</li>\n'
            s += '</ul>\n'

        return s

    def sort(self):
        data = self.get_data()
        for year in data.keys():
            data[year][True] = sorted(data[year][True], key=lambda athlete: athlete['name']) # Sort athletes in True
            data[year][False] = sorted(data[year][False], key=lambda athlete: athlete['name']) # Sort athletes in False
        data = dict(sorted(data.items())) # Sort years in data
        self.set_data(data)

        self.set_stats(dict(sorted(self.get_stats().items()))) # Sort years in stats