from fastapi import APIRouter, Query, HTTPException
from countryinfo import CountryInfo
from utils.formattools import FormatRegionTools

router = APIRouter(
    prefix='/region',
    tags=['regions'],
    responses={404 : {'msg' : 'not found'}}
)

@router.get('/americas')
async def get_americas_countries(emoji : int | None = Query(default=1)):
    return FormatRegionTools('americas').region_format(emoji=bool(emoji))

@router.get('/europe')
async def get_europe_countries(emoji : int | None = Query(default=1)):
    return FormatRegionTools('europe').region_format(emoji=bool(emoji))

@router.get('/asia')
async def get_asia_countries(emoji : int | None = Query(default=1)):
    return FormatRegionTools('africa').region_format(emoji=bool(emoji))

@router.get('/africa')
async def get_africa_countries(emoji : int | None = Query(default=1)):
    return FormatRegionTools('asia').region_format(emoji=bool(emoji))

@router.get('/oceania')
async def get_oceania_countries(emoji : int | None = Query(default=1)):
    return FormatRegionTools('oceania').region_format(emoji=bool(emoji))