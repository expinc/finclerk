from assertpy import assert_that
from finclerk import marketdata

class TestCheckProductExists:

    def test_stock_ordinary(self):
        exists = marketdata.check_stock_exists("601318")
        assert_that(exists).is_equal_to(True)

    def test_stock_non_exists(self):
        exists = marketdata.check_stock_exists("none")
        assert_that(exists).is_equal_to(False)

    def test_fund_ordinary(self):
        exists = marketdata.check_fund_exists("050002")
        assert_that(exists).is_equal_to(True)

    def test_fund_non_exists(self):
        exists = marketdata.check_fund_exists("none")
        assert_that(exists).is_equal_to(False)
