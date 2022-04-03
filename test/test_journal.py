import common
from assertpy import assert_that
from finclerk import journal

from finclerk import db

class TestJournal:

    @classmethod
    def setup_class(cls):
        common.init_app()

    @classmethod
    def teardown_class(cls):
        pass

    def test_add_product_ordinary(self):
        product = journal.add_product(1, "code4", "name4", "OPTION")
        assert_that(product).is_not_none()
