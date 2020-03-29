import unittest

from lib.command import existPath, getDemandas


class CommandTest(unittest.TestCase):
    def test_get_demanda(self):
        #path = 'C:\\TFS\\Energisa\\Sistemas\\TECCOM\\APICOMERCIAL'
        path = 'C:/TFS/Energisa/Sistemas/TECCOM/APICOMERCIAL/WebServices'
        branch = 'Branches'
        result = getDemandas(path, branch)
        self.assertIsNotNone(result)

    def test_exist_path(self):
        exist_file = 'C:/TFS/Energisa/Sistemas/TECCOM/APICOMERCIAL/MicroServicos/Branches/D462371/MSPAG'
        result = existPath(exist_file)
        self.assertTrue(result)

    def test_not_exist_path(self):
        not_exist_file = 'C:/TFS/Energisa/Sistemas/TECCOM/APICOMERCIAL/WebServices/MSPAG'
        result = existPath(not_exist_file)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
