from stats.Statistic import Statistic

class LocationDistrib(Statistic):
    def __init__(self):
        super().__init__()
        self.set_name('Location distribution')
    
    def add_elem(self, exam):
        identifier = exam['id']
        name = f'{exam["fname"]} {exam["lname"]}'
        sport = exam['sport']
        location = exam['location']

        athlete = {
            'id': identifier,
            'name': name,
            'sport': sport
        }

        if location not in self.get_data().keys():
            self._data[location] = [athlete]
            self._stats[location] = 1
        else:
            self._data[location].append(athlete)
            self._stats[location] += 1

    def print_data(self):
        s = ''
        for location, athletes in self.get_data().items():
            s += f'<h1>{location}</h1>\n'
            s += '<ul>\n'
            for athlete in athletes:
                s += f'<li>{athlete["id"]} - {athlete["name"]} - {athlete["sport"]}</li>\n'
            s += '</ul>\n'
        
        return s
    
    def print_stats(self):
        s = '<ul>\n'
        for location, num in self.get_stats().items():
            s += f'<li>{location} -> {num}</li>\n'
        
        s += '</ul>\n'
        return s
