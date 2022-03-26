from stats.Statistic import Statistic


class AgeGenderDistrib(Statistic):

    def __init__(self):
        super().__init__()
        self.set_name('Gender distribution by age')
        data = {
            '< 35': {
                'M': [],
                'F': []
            },
            '>= 35': {
                'M': [],
                'F': []
            }
        }
        stats = {
            '< 35': (0, (0, 0)),
            '>= 35': (0, (0, 0))
        }
        self.set_data(data)
        self.set_stats(stats)

    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        age = exam['age']
        gender = exam['gender']

        athlete = {
            'id': identifier,
            'name': name,
            'age': age
        }

        if age < 35:
            self._data['< 35'][gender].append(athlete)
            age = self._stats['< 35'][0]
            m = self._stats['< 35'][1][0]
            f = self._stats['< 35'][1][1]
            if gender == 'M':
                self._stats['< 35'] = (age + 1, (m + 1, f))
            else:
                self._stats['< 35'] = (age + 1, (m, f + 1))
        else:
            self._data['>= 35'][gender].append(athlete)
            age = self._stats['>= 35'][0]
            m = self._stats['>= 35'][1][0]
            f = self._stats['>= 35'][1][1]
            if gender == 'M':
                self._stats['>= 35'] = (age + 1, (m + 1, f))
            else:
                self._stats['>= 35'] = (age + 1, (m, f + 1))

    def print_data(self):
        s = ''
        for age, distrib in self.get_data().items():
            s += '<h1>' + age + '</h1>\n'
            for gender, athletes in distrib.items():
                s += '<h2>' + gender + '</h2>\n'
                s += '<ul>\n'
                for athlete in athletes:
                    s += f'<li>{athlete["id"]} - {athlete["name"]} - {athlete["age"]}</li>\n'
                s += '</ul>'
        return s

    def print_stats(self):
        s = ''
        for age, val in self.get_stats().items():
            s += f'<h3>{age} -> {val[0]}</h3>\n'
            s += '<ul>\n'
            s += f'<li>M -> {val[1][0]}</li>\n'
            s += f'<li>F -> {val[1][1]}</li>\n'
            s += '</ul>\n'
        return s
