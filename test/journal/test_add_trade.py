import peewee
from test import common
from assertpy import assert_that
from finclerk import journal

class TestJournalAddTrade:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()

    def test_no_product(self):
        assert_that(journal.add_trade).raises(peewee.DoesNotExist).when_called_with(-1, "BUY", 10.9, 100.5, "2022-01-01")

    def test_invalid_side(self):
        assert_that(journal.add_trade).raises(Exception).when_called_with(1, "NONE", 10.9, 100.5, "2022-01-01")

    def test_invalid_price(self):
        assert_that(journal.add_trade).raises(Exception).when_called_with(1, "BUY", -10.9, 100.5, "2022-01-01")

    def test_invalid_quantity(self):
        assert_that(journal.add_trade).raises(Exception).when_called_with(1, "BUY", 10.9, 0, "2022-01-01")

    def test_invalid_date(self):
        assert_that(journal.add_trade).raises(Exception).when_called_with(1, "BUY", 10.9, 100.5, "INVALID")
