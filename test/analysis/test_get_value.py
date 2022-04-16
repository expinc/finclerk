import peewee
from test import common
from assertpy import assert_that
from finclerk import analysis

class TestGetValue:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        result = analysis.get_cumulative_value(4, "2022-03-08")
        assert_that(result).is_equal_to(28825)

    def test_all_time(self):
        result = analysis.get_cumulative_value(4, "2022-04-01")
        assert_that(result).is_equal_to(68420)

    def test_future_value(self):
        assert_that(analysis.get_cumulative_value).raises(KeyError).when_called_with(4, "2099-12-12")

    def test_no_trade(self):
        result = analysis.get_cumulative_value(4, "2022-01-10")
        assert_that(result).is_equal_to(0)

    def test_no_list(self):
        assert_that(analysis.get_cumulative_value).raises(KeyError).when_called_with(4, "1970-01-01")

    def test_close_date(self):
        # FIXME: support close date value
        assert_that(analysis.get_cumulative_value).raises(KeyError).when_called_with(4, "2022-01-01")

    def test_invalid_date(self):
        assert_that(analysis.get_cumulative_value).raises(Exception).when_called_with(4, None)

    def test_no_product(self):
        assert_that(analysis.get_cumulative_value).raises(peewee.DoesNotExist).when_called_with(-1, "2022-03-08")
