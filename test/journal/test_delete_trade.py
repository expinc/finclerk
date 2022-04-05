import peewee
from test import common
from assertpy import assert_that
from finclerk import journal
from finclerk import model

class TestJournalDeleteTrade:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()

        cnt_deleted = journal.delete_trade(trade.id)
        assert_that(cnt_deleted).is_equal_to(1)

    def test_noexist(self):
        assert_that(journal.delete_trade).raises(peewee.DoesNotExist).when_called_with(-1)
