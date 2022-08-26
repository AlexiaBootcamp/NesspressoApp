from unicodedata import name
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

from application import app, d
class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            LIVESERVER_PORT=self.TEST_PORT,            
            DEBUG=True,
            TESTING=True
        )
        return app

    def setUp(self):
        from application import NessCapsules
        d.create_all() # create schema before we try to get the page

    def tearDown(self):
        d.session.remove()
        d.drop_all()

class TestRoute(TestBase):
   
    def test_index_route(self):
        response = app.test_client().get('/')

        assert response.status_code == 200