"""
Test for database setup and query execution
"""

from nose.tools import assert_equal

from db import Db


def test_table_creation():
    """
    Are tables created as expected?
    """
    expected = {'account':
                    ['id', 'uname', 'pw_hash', 'created_at', 'last_login'],
                'trnsaction':
                    ['id', 'account_id', 'debit', 'credit', 'dt', 'memo']
                }

    cnx = Db.setup()
    for k, v in expected.items():
        cursor = cnx.execute('select * from {}'.format(k))
        names = list(map(lambda x: x[0], cursor.description))
        assert_equal(names, v)
