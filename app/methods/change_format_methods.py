class ChangeStringsFormation:
    """This class will handel change style and format like replace and..."""
    def __init__(self):
        self.output = None

    def change_population_format(self, population: float):
        """
        change Values on numbers like 14000.1 to 14,000
        :param population: its can be any float point number
        :return: a formatted number
        """
        number = int(population)
        self.output = '{:,}'.format(number)
        return self.output

