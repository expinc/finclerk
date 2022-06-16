from test import common
from assertpy import assert_that
from finclerk import analysis

class TestGetBuyTotal:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        result = analysis.get_buy_total(1, "2022-02-28", "2022-03-08")
        assert_that(result).is_equal_to(29900)

    def test_no_start_date(self):
        result = analysis.get_buy_total(1, None, "2022-03-08")
        assert_that(result).is_equal_to(29900)

    def test_all_time(self):
        result = analysis.get_buy_total(1, None, "2099-12-12")
        assert_that(result).is_equal_to(66700)

    def test_no_trade(self):
        result = analysis.get_buy_total(1, None, "1970-01-01")
        assert_that(result).is_equal_to(0)

    def test_one_day(self):
        result = analysis.get_buy_total(1, "2022-03-01", "2022-03-01")
        assert_that(result).is_equal_to(10220)

    def test_no_product(self):
        assert_that(analysis.get_buy_total).raises(Exception).when_called_with(-1, "2022-03-01", "2022-03-01")

    def test_invalid_start_date(self):
        assert_that(analysis.get_buy_total).raises(Exception).when_called_with(1, "invalid", "2022-03-01")

    def test_invalid_end_date(self):
        assert_that(analysis.get_buy_total).raises(Exception).when_called_with(1, "2022-03-01", None)
