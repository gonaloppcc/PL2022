from stats.Statistic import Statistic


class SportByYear(Statistic):
    def __init__(self):
        super().__init__()
        self.set_name('Sport distribution by year')

    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        year = exam['date'].year
        sport = exam['sport']

        athlete = {
            'id': identifier,
            'name': name
        }

        if year not in self.get_data().keys():
            self._data[year] = {
                sport: [athlete]
            }
            self._stats[year] = {
                sport: 1
            }
        else:
            if sport not in self._data[year]:
                self._data[year][sport] = [athlete]
                self._stats[year][sport] = 1
            else:
                self._data[year][sport].append(athlete)
                self._stats[year][sport] += 1

    def print_data(self):
        s = ''
        for year, sport_dict in self.get_data().items():
            s += f'<h1>{year}</h1>\n'
            for sport, athletes in sport_dict.items():
                s += f'<h3>{sport}</h3>\n'
                s += '<ul>\n'
                for athlete in athletes:
                    s += f'<li>{athlete["id"]} - {athlete["name"]}</li>\n'
                s += '</ul>\n'

        return s

    def print_stats(self):
        s = ''
        for year, sports in self.get_stats().items():
            s += f'<h3>{year}</h3>\n'
            s += '<ul>\n'
            for sport, num in sports.items():
                s += f'<li>{sport} -> {num}</li>\n'
            s += '</ul>'

        return s
