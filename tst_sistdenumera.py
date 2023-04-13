import unittest

from sistemadenumera import binario2decimal, decimal2binario

class TestSistemaDeNumeracion(unittest.TestCase):

    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('1101'), 13)
        self.assertEqual(binario2decimal('1010'), 10)
        self.assertEqual(binario2decimal('11111111'), 255)
        self.assertEqual(binario2decimal('0'), 0)
    
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(13), '00001101')
        self.assertEqual(decimal2binario(10), '00001010')
        self.assertEqual(decimal2binario(255), '11111111')
        self.assertEqual(decimal2binario(0), '00000000')
        
if __name__ == '__main__':
    unittest.main()
