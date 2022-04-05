# Market Data APIs

- [Stock](#stock)
- [Fund](#fund)

## Stock

Method: ```GET https://q.stock.sohu.com/hisHq```

Parameters:

- code: Product code starts with "cn_". Suffix will be ignored, e.g., "cn_1234567" will be regarded as "cn_12345" if there is a product code "12345".
- start: Start date with format "YYYYMMDD"
- end: End date with format "YYYYMMDD"
- order: Record order by date. "A" for ascending. "D" for descending.
- period: Record period. "d" for day. "w" for week. "m" for month.

Response:

```json
[
    {
        "status": 0,    // 0 if no error
        "hq": [
            [
                "Date with format YYYY-MM-DD",
                "Open price",
                "Close Price",
                "Fluctuation",
                "Fluctuation percentage",
                "Lowest price",
                "Highest price",
                "Traded quantity (board lot)",
                "Traded amount (ten thousand)",
                "Turnover rate"
            ]
        ],
        "code": "Product code starts with cn_"
    }
]
```

Example:

```
curl --location --request GET 'https://q.stock.sohu.com/hisHq?code=cn_601318&start=20220301&order=D&period=d&end=20220301'
[
    {
        "status": 0,
        "hq": [
            [
                "2022-03-01",
                "51.01",
                "51.39",
                "0.63",
                "1.24%",
                "50.57",
                "51.40",
                "568036",
                "289518.09",
                "0.52%"
            ]
        ],
        "code": "cn_601318"
    }
]
```

## Fund

Method: ```GET https://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav```

Parameters:

- symbol: Product code
- datefrom: Start date with format "YYYYMMDD"
- dateto: End date with format "YYYYMMDD"

Response:

```json
{
    "result": {
        "status": {
            "code": 0
        },
        "data": {
            "data": [
                {
                    "fbrq": "Date time with format YYYY-MM-DD hh:mm:ss",
                    "jjjz": "Unit net value",
                    "ljjz": "Accumulative net value"
                }
            ],
            "total_num": "number of elements in array \"data\"" // none-zero if no error
        }
    }
}
```

Example:

```
curl --location --request GET 'https://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=050002&datefrom=20220301&dateto=20220301'
{
    "result": {
        "status": {
            "code": 0
        },
        "data": {
            "data": [
                {
                    "fbrq": "2022-03-01 00:00:00",
                    "jjjz": "1.7652",
                    "ljjz": "3.7991"
                }
            ],
            "total_num": "1"
        }
    }
}
```
