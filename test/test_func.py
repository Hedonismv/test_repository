import unittest
import requests


class TestCheckFunctions(unittest.TestCase):
    def setUp(self):
        self.url = 'https://cdn.pixabay.com/photo/2021/02/15/21/47/robin-6019247_960_720.jpg'
        self.req = requests.get(self.url)

    def tearDown(self) -> None:
        pass

    def test_check_image(self):
        result = self.req.headers['content-type']
        self.assertEqual(result[0:5], 'image')

    def test_check_status_code(self):
        result = self.req.status_code
        self.assertFalse(result == 404)
        print(result)


if __name__ == '__main__':
    unittest.main()
