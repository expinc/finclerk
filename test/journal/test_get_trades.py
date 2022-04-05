import peewee
from test import common
from assertpy import assert_that
from finclerk import journal

class TestJournalGetTrades:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        trades = journal.get_trades_of_product(1)
        assert_that(len(trades)).is_equal_to(2)

    def test_no_trade(self):
        trades = journal.get_trades_of_product(3)
        assert_that(len(trades)).is_equal_to(0)

    def test_invalid_product(self):
        trades = journal.get_trades_of_product(-1)
        assert_that(len(trades)).is_equal_to(0)
