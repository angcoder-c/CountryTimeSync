from fastapi import APIRouter, Query, HTTPException
from countryinfo import CountryInfo
from utils.formattools import FormatSubregionTools

router = APIRouter(
    prefix='/subregions',
    tags=['subregions'],
    responses={404 : {'msg' : 'not found'}}
)

@router.get('/americas')
async def get_americas_countries(emoji : int | None = Query(default=1)):
    return FormatSubregionTools('americas').subregion_format(emoji=bool(emoji))

@router.get('/europe')
async def get_europe_countries(emoji : int | None = Query(default=1)):
    return FormatSubregionTools('europe').subregion_format(emoji=bool(emoji))

@router.get('/asia')
async def get_asia_countries(emoji : int | None = Query(default=1)):
    return FormatSubregionTools('africa').subregion_format(emoji=bool(emoji))

@router.get('/africa')
async def get_africa_countries(emoji : int | None = Query(default=1)):
    return FormatSubregionTools('asia').subregion_format(emoji=bool(emoji))

@router.get('/oceania')
async def get_oceania_countries(emoji : int | None = Query(default=1)):
    return FormatSubregionTools('oceania').subregion_format(emoji=bool(emoji))