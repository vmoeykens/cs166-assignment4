"""
Shared fixtures. Note that pytest has these available fixtures: cache, capfd,
capfdbinary, caplog, capsys, capsysbinary, cov, doctest_namespace, monkeypatch,
no_cover, pytestconfig, record_property, record_testsuite_property,
record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir,
tmpdir_factory. Don't reinvent the wheel.
"""

# pylint: disable=W0611,W0621

import pytest

from bank import app as app_


@pytest.fixture
def app():
    """Yield app with its context set up and ready. """
    with app_.app_context():
        yield app_


@pytest.fixture
def client(app):
    """Get a test client for Flask app. This client is used for testing
    the app -- that is, views and whatnot. Use db_setup_client for lower
    level testing that does not involve views (i.e. headless stuff). Note that
    we disable WTF's CSRF protection so we don't get CSRF validation
    errors when creating and submitting forms in testing . """
    # print('fixture: client')
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Not using WTF at this moment...
    app.config['DEBUG'] = False  # IMPORTANT !
    return app.test_client()
