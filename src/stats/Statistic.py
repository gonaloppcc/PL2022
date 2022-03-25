from abc import abstractmethod


class Statistic:
    def __init__(self):
        self._name = 'Stat'
        self._stats = {}
        self._data = {}

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

    @abstractmethod
    def add_elem(self, elem):
        pass

    @abstractmethod
    def print_data(self):
        pass

    @abstractmethod
    def print_stats(self):
        pass
