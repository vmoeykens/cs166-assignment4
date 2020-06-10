""""
SQL Injection Example
This function is the only one you are permitted
to modify for the lab assignment.

Note: if you aren't familiar with str.format, here
is a link to the docs:
https://docs.python.org/3/library/stdtypes.html#str.format
"""


def create_search_query(account_id: int, search_term: str) -> str:
    """
    Creation of SQL query that has injection vulnerability.
    You should be able to
        1) explain why this is vulnerable,
        2) demonstrate how to exploit this vulnerability, and
        3) modify this code to prevent SQL injection attack
    :param account_id: int
    :param search_term: str
    :return: str (the query)
    """
    # Never do this in the real world...
    q = 'SELECT * FROM trnsaction ' \
        'WHERE trnsaction.account_id = {} ' \
        'AND ' \
        'trnsaction.memo LIKE "%{}%"'.format(account_id, search_term)
    return q
