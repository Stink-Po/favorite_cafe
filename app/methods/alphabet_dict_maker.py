import string
from app.methods.database_methods import DataBaseInfo


class AlphabetDictMaker:
    """This Class make Alphabetical dict from given a table in a database"""

    def __init__(self):
        self.upper_alphabet = string.ascii_uppercase
        self.lower_alphabet = string.ascii_lowercase
        self.start_letter = None
        self.db_info = DataBaseInfo()
        self.alphabet_dict = {}
        self.empty_alphabet_dict_maker()

    def empty_alphabet_dict_maker(self):
        """

        :return: an Empty Dict with uppercase alphabet as Keys
        """
        self.alphabet_dict = {letter: [] for letter in self.upper_alphabet}
        return self.alphabet_dict

    def ret_alphabetical_country(self):
        """

        :return: a Dict With all alphabets as a key and every value
        is a list that's contain all country that their name start with this key
        """

        for country in self.db_info.all_country:
            self.start_letter = country.country_name[0].upper()
            for (key, value) in self.alphabet_dict.items():
                if key == self.start_letter:
                    local_dict = {
                        "country": country.country_name,
                        "country_id": country.id
                    }
                    self.alphabet_dict[key].append(local_dict)

        return self.alphabet_dict

    def ret_item_by_index(self, index):
        """
        used in to paginate for the Country view
        :param index: given index of a list
        :type index: int
        :return: value of the given index
        """
        return self.alphabet_dict[self.upper_alphabet[index - 1]]


