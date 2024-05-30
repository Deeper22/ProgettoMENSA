import unittest
from main import Utente, Admin, Menu


class TestUtente(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Sto eseguendo il setup principale')

    @classmethod
    def tearDownClass(cls):
        print('Sto eseguendo il teardown principale')

    def setUp(self):
        self.utente1 = Utente('Valerio', 'Clementi', 1234567)
        print('Sto eseguendo il setup')

    def tearDown(self):
        print('Sto eseguendo il teardown')


if __name__ == '__main__':
    unittest.main()
