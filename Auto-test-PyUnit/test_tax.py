import unittest
import tax_final as tax_f

class TestTax(unittest.TestCase):

### test progressive tax (no tax) ###
    def test_tax_s1(self):
        result = tax_f.Caltax(income = 10000)
        result.tax_s()
        self.assertEqual(result.deductions, 500)
        self.assertEqual(result.taxs, 0)

### test progressive tax (need pay tax) ###
    def test_tax_s2(self):
        result = tax_f.Caltax(income = 150000)
        result.tax_s()
        self.assertEqual(result.deductions, 7500)
        self.assertEqual(result.taxs, 210)

### test standard rate of tax ###
    def test_tax_s3(self):
        result = tax_f.Caltax(income = 2500000)
        result.tax_s()
        self.assertEqual(result.deductions, 18000)
        self.assertEqual(result.st_tax, 372300)

    def test_tax_s4(self):
        result = tax_f.Caltax(income = 50000000)
        result.tax_s()
        self.assertEqual(result.deductions, 18000)
        self.assertEqual(result.st_tax, 7497300)  

### test max boundary values tested ###
    def test_tax_s5(self):
        result = tax_f.Caltax(income = 2040000)
        result.tax_s()
        self.assertEqual(result.deductions, 18000)
        self.assertEqual(result.st_tax, 303300)                        

if __name__ == '__main__':
    unittest.main()