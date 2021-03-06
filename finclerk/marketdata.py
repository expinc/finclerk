import http.client
import json
import urllib
from . import common
from http import HTTPStatus

def check_stock_exists(code):
    try:
        conn = http.client.HTTPSConnection("q.stock.sohu.com")
        params = urllib.parse.urlencode({
            "code": "cn_" + code
        })
        url = "/hisHq?" + params
        conn.request("GET", url)
        response = conn.getresponse()
        if HTTPStatus.OK != response.status:
            raise Exception("Unexpected status: {}".format(response.status))
        body = response.read()
        body = json.loads(body)
        return isinstance(body, list) and 0 == body[0]["status"]
    finally:
        if conn:
            conn.close()

def check_fund_exists(code):
    try:
        conn = http.client.HTTPSConnection("stock.finance.sina.com.cn")
        params = urllib.parse.urlencode({
            "symbol": code
        })
        url = "/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?" + params
        conn.request("GET", url)
        response = conn.getresponse()
        if HTTPStatus.OK != response.status:
            raise Exception("Unexpected status: {}".format(response.status))
        body = response.read()
        body = json.loads(body)
        return "0" != body["result"]["data"]["total_num"]
    finally:
        if conn:
            conn.close()

def _get_stock_close_price(code, date):
    try:
        conn = http.client.HTTPSConnection("q.stock.sohu.com")
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

def _get_fund_unit_net(code, date):
    try:
        conn = http.client.HTTPSConnection("stock.finance.sina.com.cn")
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
    # FIXME: handle close date price
    common.check_date_format(date)
    # YYYY-MM-DD -> YYYYMMDD
    date = date.replace("-", "")
    if "STOCK" == type:
        return _get_stock_close_price(code, date)
    elif "FUND" == type:
        return _get_fund_unit_net(code, date)
    else:
        raise Exception("Invalid code: {}".format(code))
