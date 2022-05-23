import peewee
from test import common
from assertpy import assert_that
from finclerk import journal

class TestJournalAddProduct:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_stock_ordinary(self):
        product = journal.add_product(1, "600519", "贵州茅台", "STOCK")
        assert_that(product).is_not_none()

    def test_fund_ordinary(self):
        product = journal.add_product(1, "000311", "景顺长城沪深300指数增强A", "FUND")
        assert_that(product).is_not_none()

    def test_stock_non_exists(self):
        assert_that(journal.add_product).raises(Exception).when_called_with(1, "none", "none", "STOCK")

    def test_fund_non_exists(self):
        assert_that(journal.add_product).raises(Exception).when_called_with(1, "none", "none", "FUND")

    def test_no_account(self):
        assert_that(journal.add_product).raises(peewee.DoesNotExist).when_called_with(-1, "600276", "恒瑞医药", "STOCK")

    def test_duplicate_code(self):
        product = journal.add_product(1, "000858", "五粮液", "STOCK")
        assert_that(product).is_not_none()
        assert_that(journal.add_product).raises(Exception).when_called_with(1, "000858", "五粮液", "STOCK")

    def test_invalid_type(self):
        assert_that(journal.add_product).raises(Exception).when_called_with(1, "300059", "东方财富", "NONE")
