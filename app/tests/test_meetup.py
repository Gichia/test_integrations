import json
import unittest
from app import create_app

APP = create_app()

class TestMeetup(unittest.TestCase):

    def setUp(self):
        APP.testing = True
        self.app = APP.test_client()
        self.data = {
            "id": 1,
            "created_on": "12/12/1018",
            "location": "Nairobi",
            "topic": "Web Dev",
            "tags": ["Flask", "API"]
        }

    def test_create_meetups(self):

        response = self.app.post('/api/v1/meetup', data = json.dumps(self.data), content_type="application/json")
        result = json.loads(response.data.decode('UTF-8'))
        print(result)


if __name__ == '__main__':
    unittest.main()



