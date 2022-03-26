from abc import abstractmethod


class Statistic:
    def __init__(self):
        self._name = 'Stat' # Name of the statistic
        self._stats = {}    # Statistics
        self._data = {}     # Elements

    def set_name(self, name):
        self._name = name

    def set_stats(self, stats):
        self._stats = stats

    def set_data(self, data):
        self._data = data

    def get_name(self):
        return self._name

    def get_stats(self):
        return self._stats

    def get_data(self):
        return self._data

    # Adds an element to data and stats
    @abstractmethod
    def add_elem(self, elem):
        pass

    # Prints the data in html format
    @abstractmethod
    def print_data(self):
        pass

    # Prints the stats in html format
    @abstractmethod
    def print_stats(self):
        pass
