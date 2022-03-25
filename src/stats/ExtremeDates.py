from stats.Statistic import Statistic

class ExtremeDates(Statistic):
    def __init__(self):
        super().__init__()
        self.set_data('Extreme dates')
        data = {
            'oldest': {},
            'newest': {}
        }
        self.set_data(data)


    def add_elem(self, elem):
        if 