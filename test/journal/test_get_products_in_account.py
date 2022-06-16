from test import common
from assertpy import assert_that
from finclerk import journal

class TestJournalGetProductsInAccount:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_ordinary(self):
        products_1 = journal.get_products_in_account(1)
        assert_that(len(products_1)).is_equal_to(2)
        products_2 = journal.get_products_in_account(2)
        assert_that(len(products_2)).is_equal_to(1)
