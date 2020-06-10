"""
Do a little setup!
Run this setup.py script directly whenever you want a
fresh database to play around with.

"""

import os

from db import Db

DIRS = ['instance/var/db',
        'instance/var/log',
        'instance/var/tmp',
        'instance/var/run']

if __name__ == '__main__':

    print("Creating directories...")
    for d in DIRS:
        try:
            os.makedirs(d)
        except FileExistsError:
            pass

    print("Initializing database...")
    Db.setup()

    print("Done!")
