import http.client
import json
import urllib
from http import HTTPStatus

def get_stock_close_price(code, date):
    try:
        conn = http.client.HTTPConnection("q.stock.sohu.com")
        params = urllib.parse.urlencode({
            "code": "cn_" + code,
            "start": date,
            "end": date,
            "order": "D",
            "period": "d"
        })
        url = "/hisHq?" + params
        conn.request("GET", url)
        response = conn.getresponse()
        if HTTPStatus.OK != response.status:
            raise Exception("Unexpected status: {}".format(response.status))
        body = response.read()
        body = json.loads(body)
        return float(body[0]["hq"][0][2])
    finally:
        if conn:
            conn.close()

def get_fund_unit_net(code, date):
    try:
        conn = http.client.HTTPConnection("stock.finance.sina.com.cn")
        params = urllib.parse.urlencode({
            "symbol": code,
            # TODO: convert format
            "datefrom": date,
            "dateto": date
        })
        url = "/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?" + params
        conn.request("GET", url)
        response = conn.getresponse()
        if HTTPStatus.OK != response.status:
            raise Exception("Unexpected status: {}".format(response.status))
        body = response.read()
        body = json.loads(body)
        return float(body["result"]["data"]["data"][0]["jjjz"])
    finally:
        if conn:
            conn.close()

def get_price(type, code, date):
    if "STOCK" == type:
        return get_stock_close_price(code, date)
    elif "FUND" == type:
        return get_fund_unit_net(code, date)
    else:
        raise Exception("Invalid code: {}".format(code))
