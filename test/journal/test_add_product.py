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

    def test_ordinary(self):
        product = journal.add_product(1, "code4", "name4", "OPTION")
        assert_that(product).is_not_none()

    def test_no_account(self):
        assert_that(journal.add_product).raises(peewee.DoesNotExist).when_called_with(-1, "code4", "name4", "OPTION")

    def test_duplicate_code(self):
        product = journal.add_product(1, "code5", "name5", "OPTION")
        assert_that(product).is_not_none()
        assert_that(journal.add_product).raises(peewee.IntegrityError).when_called_with(1, "code5", "name6", "OPTION")

    def test_invalid_type(self):
        assert_that(journal.add_product).raises(Exception).when_called_with(1, "code6", "name6", "NONE")
