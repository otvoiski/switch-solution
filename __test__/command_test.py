import unittest

from lib.command import getDemandas


class CommandTest(unittest.TestCase):
    def test_get_demanda(self):
        #path = 'C:\\TFS\\Energisa\\Sistemas\\TECCOM\\APICOMERCIAL'
        path = 'C:/TFS/Energisa/Sistemas/TECCOM/APICOMERCIAL/WebServices'
        branch = 'Branches'
        result = getDemandas(path, branch)
        self.assertIsNotNone(result)

    def existPath(self):
        exist_file = None
        self.assertTrue(exist_file)


if __name__ == '__main__':
    unittest.main()
