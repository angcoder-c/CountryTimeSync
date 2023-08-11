# Country TIme Sync Endpoints

## Country

Is an endpoint prefixed with '/country/' in which the full name of a country can be queried, as well as its alpha2 and alpha3 acronyms. Returns an object with some useful data about the country and its time zones.

### Example

> `localhost:8000/country/spain`

```
{
  "country": "spain",
  "datetimes": [
    {
      "timezone": "UTC",
      "datetime": "2023-08-11T03:11:58.963766+00:00",
      "summary": {
        "date": "08/11/2023",
        "time": "03:11:58"
      }
    },
    {
      "timezone": "UTC+01:00",
      "datetime": "2023-08-11T04:11:58.963766+01:00",
      "summary": {
        "date": "08/11/2023",
        "time": "04:11:58"
      }
    }
  ],
  "flag": "🇪🇸"
}
```

Put the country name as `ES` or `ESP` (case insensitive) and you will get the same result.

You can also set the `emoji` filter which accepts any integer greater than zero as `True` and zero as `Flash`. Default is set to true

## Subregions

It is an endpoint prefixed with '/subregions/' where you can query for the name of one of the five continents ('americas', 'asia', 'africa', 'europe', 'oceania') and will return an object with the countries of that continent divided by their respective subregion.

You can also set the `emoji` filter to show the flags of the countries.

### Example

> `localhost:8000/subregions/africa/`

```
{
  "region": "africa",
  "subregions names": [
    "Eastern Africa",
    "Western Africa",
    "Northern Africa",
    "Middle Africa",
    "Southern Africa"
  ],
  "subregions": [
    {
      "Eastern Africa": [
        {
          "country": "seychelles",
          "datetimes": [
            {
              "timezone": "UTC+04:00",
              "datetime": "2023-08-11T07:32:57.728972+04:00",
              "summary": {
                "date": "08/11/2023",
                "time": "07:32:57"
              }
            }
          ],
          "flag": "🇸🇨"
        },
        {
          "country": "madagascar",
          "datetimes": [
            {
              "timezone": "UTC+03:00",
              "datetime": "2023-08-11T06:32:57.729102+03:00",
              "summary": {
                "date": "08/11/2023",
                "time": "06:32:57"
              }
            }
          ],
          "flag": "🇲🇬"
        },
        ...
      ]
    }
  ]
}
```

## Regions

It is an endpoint prefixed with '/region/' where you can query for the name of one of the five continents ('americas', 'asia', 'africa', 'europe', 'oceania') and will return an object with the countries in that region.

You can also set the `emoji` filter to display country flags.

### Example

> `localhost:8000/region/europe/`

```
[
  {
    "country": "cyprus",
    "datetimes": [
      {
        "timezone": "UTC+02:00",
        "datetime": "2023-08-11T05:38:58.863146+02:00",
        "summary": {
          "date": "08/11/2023",
          "time": "05:38:58"
        }
      }
    ],
    "flag": "🇨🇾"
  },
  {
    "country": "albania",
    "datetimes": [
      {
        "timezone": "UTC+01:00",
        "datetime": "2023-08-11T04:38:58.897658+01:00",
        "summary": {
          "date": "08/11/2023",
          "time": "04:38:58"
        }
      }
    ],
    "flag": "🇦🇱"
  },
  {
    "country": "slovenia",
    "datetimes": [
      {
        "timezone": "UTC+01:00",
        "datetime": "2023-08-11T04:38:58.935598+01:00",
        "summary": {
          "date": "08/11/2023",
          "time": "04:38:58"
        }
      }
    ],
    "flag": "🇸🇮"
  },
  {
    "country": "ireland",
    "datetimes": [
      {
        "timezone": "UTC",
        "datetime": "2023-08-11T03:38:58.972018+00:00",
        "summary": {
          "date": "08/11/2023",
          "time": "03:38:58"
        }
      }
    ],
    "flag": "🇮🇪"
  },
  ...
]
```