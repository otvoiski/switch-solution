import unittest

from constante import Constante


class ConfigTest(unittest.TestCase):
    def testa_se_config_is_not_none(self):
        config = Constante().getConfig()
        result = config['others']['ms']
        self.assertTrue(result == 'MicroServicos')


if __name__ == '__main__':
    unittest.main()
