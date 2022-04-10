from . import journal
from . import marketdata

def get_buy_total(product_id, start_date, end_date):
    where_clause = (journal.Trade.product.id == product_id) & (journal.Trade.side == "BUY") & (journal.Trade.datetime <= end_date)
    if start_date:
        where_clause = where_clause & (journal.Trade.datetime >= start_date)
    all_trades = (journal.Trade.select().where(where_clause))
    return sum([trade.quantity*trade.price for trade in all_trades])

def get_sell_total(product_id, start_date, end_date):
    where_clause = (journal.Trade.product.id == product_id) & (journal.Trade.side == "SELL") & (journal.Trade.datetime <= end_date)
    if start_date:
        where_clause = where_clause & (journal.Trade.datetime >= start_date)
    all_trades = (journal.Trade.select().where(where_clause))
    return sum([trade.quantity*trade.price for trade in all_trades])

def get_value(product_id, date):
    product = journal.Product.select().where(journal.Product.id == product_id).get()
    current_price = marketdata.get_price(product.type, product.code, date)
    all_buy = (journal.Trade.select()
        .where((journal.Trade.product.id == product_id) & (journal.Trade.side == "BUY") & (journal.Trade.datetime <= date))
        .order_by(journal.Trade.datetime))
    all_sell = (journal.Trade.select()
        .where((journal.Trade.product.id == product_id) & (journal.Trade.side == "SELL") & (journal.Trade.datetime <= date))
        .order_by(journal.Trade.datetime))
    buy_quantity = sum([buy.quantity for buy in all_buy])
    sell_quantity = sum([sell.quantity for sell in all_sell])
    return current_price * (buy_quantity - sell_quantity) + get_sell_total(product_id, None, date)

def calculate_earning(product_ids, start_date, end_date):
    # FIXME: DB concurrency control
    total_earn = 0
    for product_id in product_ids:
        start_value = get_value(product_id, start_date)
        end_value = get_value(product_id, end_date)
        total_earn += end_value - start_value - get_buy_total(product_id, start_date, end_date)
    return total_earn
