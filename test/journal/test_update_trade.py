from test import common
from assertpy import assert_that
from finclerk import journal
from finclerk import model

class TestJournalUpdateTrade:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()

        cnt_updated = journal.update_trade(trade.id, "SELL", 11.9, 200.5, "2022-01-31")
        assert_that(cnt_updated).is_equal_to(1)

        new_trade = model.Trade.select().where(model.Trade.id == trade.id).get()
        assert_that(new_trade.side).is_equal_to("SELL")
        assert_that(new_trade.price).is_equal_to(11.9)
        assert_that(new_trade.quantity).is_equal_to(200.5)
        assert_that(new_trade.datetime).is_equal_to("2022-01-31")

    def test_no_change(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()

        cnt_updated = journal.update_trade(trade.id, trade.side, trade.price, trade.quantity, trade.datetime)
        assert_that(cnt_updated).is_equal_to(1)

        new_trade = model.Trade.select().where(model.Trade.id == trade.id).get()
        assert_that(new_trade.side).is_equal_to(trade.side)
        assert_that(new_trade.price).is_equal_to(trade.price)
        assert_that(new_trade.quantity).is_equal_to(trade.quantity)
        assert_that(new_trade.datetime).is_equal_to(trade.datetime)

    def test_invalid_side(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()
        assert_that(journal.update_trade).raises(Exception).when_called_with(trade.id, "NONE", trade.price, trade.quantity, trade.datetime)

    def test_invalid_price(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()
        assert_that(journal.update_trade).raises(Exception).when_called_with(trade.id, trade.side, -10.9, trade.quantity, trade.datetime)

    def test_invalid_quantity(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()
        assert_that(journal.update_trade).raises(Exception).when_called_with(trade.id, trade.side, trade.price, 0, trade.datetime)

    def test_invalid_date(self):
        trade = journal.add_trade(1, "BUY", 10.9, 100.5, "2022-01-01")
        assert_that(trade).is_not_none()
        assert_that(journal.update_trade).raises(Exception).when_called_with(trade.id, trade.side, trade.price, trade.quantity, "INVALID")
