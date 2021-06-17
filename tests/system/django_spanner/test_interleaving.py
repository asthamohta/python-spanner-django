from .models import Author, Person
from django.test import TransactionTestCase
from django.db import connection
from decimal import Decimal
import pdb
from .utils import (
    setup_instance,
    teardown_instance,
    setup_database,
    teardown_database,
)


class TestQueries(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        setup_instance()
        setup_database()
        with connection.schema_editor() as editor:
            # Create the tables
            editor.create_model(Person)
            editor.create_model(Author)
        pdb.set_trace()

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as editor:
            # delete the table
            editor.delete_model(Person)
            editor.delete_model(Author)
        teardown_database()
        teardown_instance()

    def test_insert_and_fetch_value(self):
        """
        Tests model object creation with Author model.
        Inserting data into the model and retrieving it.
        """
        person= Person(name="Astha",user_id=36)
        author_kent = Author(
            first_name="Arthur", last_name="Kent", rating=Decimal("4.1"),
        )
        #author_kent.save()
        # qs1 = Author.objects.all().values("first_name", "last_name")
        # self.assertEqual(qs1[0]["first_name"], "Arthur")
        # self.assertEqual(qs1[0]["last_name"], "Kent")
        # Delete data from Author table.
        Author.objects.all().delete()
