from countryinfo import CountryInfo
from fastapi import FastAPI, Request, HTTPException
from ip2geotools.databases.noncommercial import DbIpCity
from utils.formattools import FormatCountryTools
from routers import countries, regions, subregions
import uvicorn

app = FastAPI()
app.include_router(countries.router)
app.include_router(regions.router)
app.include_router(subregions.router)

@app.get('/')
async def root (request : Request):
    ip_client = request.client.host
    ip_info = DbIpCity.get(ip_client, api_key='free')

    if ip_info.country == 'ZZ':
        raise HTTPException(status_code=400, detail='the client ip is a private ip or localhost')
    
    tools = FormatCountryTools(CountryInfo(ip_info.country))
    return tools.country_fromat()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)