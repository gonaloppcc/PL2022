import datetime
from stats.Statistic import Statistic

class ExtremeDates(Statistic):
    def __init__(self):
        super().__init__()
        self.set_name('Extreme dates')
        data = {
            'oldest': {
                'id': 'empty',
                'name': 'empty',
                'sport': 'empty',
                'date': datetime.datetime.max
            },
            'newest': {
                'id': 'empty',
                'name': 'empty',
                'sport': 'empty',
                'date': datetime.datetime.min
            },
        }
        self.set_data(data)


    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        date = exam['date']
        sport = exam['sport']
        
        athlete = {
            'id': identifier,
            'name': name,
            'date': date,
            'sport': sport
        }
        if date < self._data['oldest']['date']:
            self._data['oldest'] = athlete
        if date > self._data['newest']['date']:
            self._data['newest'] = athlete

    def print_data(self):
        oldest = self.get_data()['oldest']
        newest = self.get_data()['newest']
        s = '<h2>Oldest</h2>\n'
        s += f'{oldest["id"]} - {oldest["name"]} -- {oldest["sport"]} -- {oldest["date"]}\n'
        s += '<h2>Newest</h2>\n'
        s += f'{newest["id"]} - {newest["name"]} -- {newest["sport"]} -- {newest["date"]}\n'

        return s

    def print_stats(self):
        oldest = self.get_data()['oldest']
        newest = self.get_data()['newest']

        s = '<ul>\n'
        s += f'<li>Oldest -> {oldest["name"]} - {oldest["date"]}</li>\n'
        s += f'<li>Newest -> {newest["name"]} - {newest["date"]}</li>\n'
        s += '</ul>\n'

        return s

