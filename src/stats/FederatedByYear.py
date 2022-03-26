from stats.Statistic import Statistic


class FederatedByYear(Statistic):
    def __init__(self):
        Statistic.__init__(self)
        self.set_name('Federated by year')

    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        federated = exam['federated']
        year = exam['date'].year

        athlete = {
            'id': identifier,
            'name': name
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

        self._data[year][federated].append(athlete)
        self._stats[year][federated] += 1

    def print_data(self):
        s = ''

        for year, results in self.get_data().items():
            s += f'<h2>{year}</h2>\n'

            s += '<h3>True</h3>\n'
            s += '<ul>\n'
            for athlete in results[True]:
                s += f'<li>{athlete["id"]} - {athlete["name"]}</li>\n'
            s += '</ul>\n'

            s += '<h3>False</h3>\n'
            s += '<ul>\n'
            for athlete in results[False]:
                s += f'<li>{athlete["id"]} - {athlete["name"]}</li>\n'
            s += '</ul>\n'

        return s

    def print_stats(self):
        s = ''
        for year, results in self.get_stats().items():
            s += f'<h2>{year}</h2>\n'
            s += '<ul>\n'
            s += f'<li>True -> {results[True]}</li>\n'
            s += f'<li>False -> {results[False]}</li>\n'
            s += '</ul>\n'
        return s
