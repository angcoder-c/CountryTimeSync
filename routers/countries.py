from fastapi import APIRouter, Query, HTTPException
from utils.formattools import FormatCountryTools
from countryinfo import CountryInfo

router = APIRouter(
    prefix='/country',
    tags=['countries'],
    responses={404 : {'msg' : 'not found'}}
)

@router.get('/{country}')
async def get_country_time(country : str = None, emoji : int | None = Query(default=1)):
    try:
        country_info = CountryInfo(country)
        country_info.info()
    except KeyError:
        raise HTTPException(status_code=400, detail='name of country not found')

    tools = FormatCountryTools(country_info)    
    return tools.country_fromat(emoji=bool(emoji))