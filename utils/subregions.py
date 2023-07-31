from .regions import Region
from contextlib import suppress

class Subregion:
    def __init__(self, name : str):
        self.__region_countries = Region(name=name).get_countires()
        self.subregions = {}

        for country in self.__region_countries:
            with suppress(KeyError): 
                subregion_country = country.subregion()
                if subregion_country not in self.subregions.keys():
                    self.subregions[subregion_country] = []
                else:
                    self.subregions[subregion_country].append(country)
    
    def get_subregions_names(self):
        subregions = self.subregions.keys()
        return list(subregions)

    def get_subregions(self):
        subregions = self.subregions
        return subregions