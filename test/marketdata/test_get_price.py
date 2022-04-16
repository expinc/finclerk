from assertpy import assert_that
from finclerk import marketdata

class TestGetPrice:

    def test_stock(self):
        price = marketdata.get_price("STOCK", "601318", "2022-03-01")
        assert_that(price).is_equal_to(51.39)

    def test_fund(self):
        price = marketdata.get_price("FUND", "050002", "2022-03-01")
        assert_that(price).is_equal_to(1.7652)

    def test_invalid_type(self):
        assert_that(marketdata.get_price).raises(Exception).when_called_with("INVALID", "601318", "2022-03-01")

    def test_invalid_stock_code(self):
        assert_that(marketdata.get_price).raises(Exception).when_called_with("STOCK", "invalid", "2022-03-01")

    def test_invalid_stock_date(self):
        assert_that(marketdata.get_price).raises(Exception).when_called_with("STOCK", "601318", "invalid")

    def test_invalid_fund_code(self):
        assert_that(marketdata.get_price).raises(Exception).when_called_with("FUND", "invalid", "2022-03-01")

    def test_invalid_fund_date(self):
        assert_that(marketdata.get_price).raises(Exception).when_called_with("FUND", "050002", "invalid")
