from countryinfo import CountryInfo
from contextlib import suppress

class Region:
    def __init__(self, name : str):
        self._region = name.lower().capitalize()
        self._all_countries = CountryInfo().all()

        def filter_region(country : str):
            with suppress(KeyError): 
                return self._all_countries[country]['region'] == self._region

        self._region_countires = map(CountryInfo,filter(filter_region, self._all_countries))
    
    def get_region_name(self):
        name = self._region
        return name

    def get_countires(self):
        countires = self._region_countires
        return countires


