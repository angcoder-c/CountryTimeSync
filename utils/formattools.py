from countryinfo import CountryInfo
from .regions import Region
from .subregions import Subregion
from flag import flag
import datetime


class FormatCountryTools:
    def __init__(self, country : CountryInfo):
        self.country = country

        timezones = country.timezones() 
        self.tzs = [] if not timezones else timezones
        
        self.utc = datetime.datetime.now(tz=datetime.timezone.utc)
        self.tzs_convert = list(map( 
            lambda tz :{
                'timezone' : tz,
                'datetime' : FormatCountryTools.set_timezone(tz=tz, time=self.utc)
            }, self.tzs
        ))
    
    @classmethod
    # Limpiador de datos UTC
    # UTC±HH:MM
    def format_timezone(self, tz : str, ):
        difference = tz[3::]
        if difference == '' or None:
            return (0, 0)

        sign_dif, hours, minutes = difference[0].replace('−', '-'), difference[1:3], difference[4::]
        sign_dif = int(f'{sign_dif}1')
        hours = int(hours if hours else 0) * sign_dif
        minutes = int(minutes if minutes else 0) * sign_dif

        return (hours, minutes)
    
    @classmethod
    # timezone transfer
    def set_timezone (self, tz, time : datetime.datetime):
        hour, min = FormatCountryTools.format_timezone(tz)
        tz = datetime.timezone(datetime.timedelta(hours=hour, minutes=min))
        return time.astimezone(tz=tz)

    def datetime_fromat(self):
        response = list(map( 
            lambda tzi: {
                'timezone' : tzi['timezone'],
                'datetime' : tzi['datetime'],
                'summary' : {
                    'date' : tzi['datetime'].strftime('%m/%d/%Y'),
                    'time' : tzi['datetime'].strftime('%H:%M:%S')
                }
            }, self.tzs_convert     
        ))
        return response
    
    def country_fromat(self, emoji : bool = True):
        response = {
            'country' : self.country.name(),
	        'datetimes' : self.datetime_fromat()
        }

        if emoji:
            response.update({'flag' : flag(self.country.iso()['alpha2'])})

        return response


class FormatRegionTools:
    def __init__(self, region : str):
        self.region = Region(name=region)
        self.name = self.region.get_region_name()
        self.countries = self.region.get_countires()
        
    def region_format(self, emoji : bool = True):
        return list(map(
            lambda country: 
                FormatCountryTools(country=country).country_fromat(emoji=emoji), 
            self.countries
        ))
    
class FormatSubregionTools:
    def __init__(self, region : str):
        self.region_name = region
        self.region = Subregion(name=region)
        self.subregions_names = self.region.get_subregions_names()
        self.subregions = self.region.get_subregions()
        
    def subregion_format(self, emoji : bool = True):
        subregions = list(map(
            lambda subregion: 
                { 
                    subregion : list(map(
                        lambda country : FormatCountryTools(country=country).country_fromat(emoji=emoji),
                        self.subregions[subregion]
                    ))
                }, 
            self.subregions_names
        ))

        return {
            'region' : self.region_name,
            'subregions names' : self.subregions_names,
            'subregions':subregions
        }