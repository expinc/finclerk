import peewee
from test import common
from assertpy import assert_that
from finclerk import analysis

class TestCalcEarn:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        result = analysis.calculate_earning([4], "2022-03-08", "2022-03-14")
        assert_that(result).is_equal_to(-355)

    def test_all_time(self):
        result = analysis.calculate_earning([4], "2022-02-28", "2022-03-14")
        assert_that(result).is_equal_to(-1430)

    def test_same_day(self):
        assert_that(analysis.calculate_earning).raises(Exception).when_called_with([4], "2022-03-01", "2022-03-01")

    def test_no_trade(self):
        result = analysis.calculate_earning([4], "2022-01-04", "2022-01-28")
        assert_that(result).is_equal_to(0)

    def test_future_value(self):
        assert_that(analysis.calculate_earning).raises(KeyError).when_called_with([4], "2099-01-01", "2099-12-31")

    def test_no_product(self):
        assert_that(analysis.calculate_earning).raises(peewee.DoesNotExist).when_called_with([-1], "2022-03-08", "2022-03-14")

    def test_empty_product(self):
        result = analysis.calculate_earning([], "2022-03-08", "2022-03-14")
        assert_that(result).is_equal_to(0)

    def test_multi_products(self):
        result = analysis.calculate_earning([4, 5], "2022-03-08", "2022-03-14")
        assert_that(result).is_equal_to(-588)

    def test_invalid_date(self):
        assert_that(analysis.calculate_earning).raises(Exception).when_called_with([4], None, "invalid")

    def test_reverse_date(self):
        assert_that(analysis.calculate_earning).raises(Exception).when_called_with([4], "2022-03-14", "2022-03-08")
