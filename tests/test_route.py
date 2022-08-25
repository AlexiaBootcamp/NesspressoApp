from unicodedata import name
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

from app import application, db
class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):
        application.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            LIVESERVER_PORT=self.TEST_PORT,            
            DEBUG=True,
            TESTING=True
        )
        return application

    def setUp(self):
        from app import NessCapsules
        db.create_all() # create schema before we try to get the page

        test_nessapp = NessCapsules(capsule_name = "Test")
        db.session.add(test_nessapp)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestAdd(TestBase):
   
    def test_index_route(self):
        response = application.test_client().get('/')

        assert response.status_code == 200