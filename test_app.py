import unittest
from main import server


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = server.test_client()
        self.app.testing = True

    def test_server(self):
        response = self.app.post('/', data={"question": "who are you？"})
        print("data:\n{}\n".format(response.data))


if __name__ == '__main__':
    unittest.main()