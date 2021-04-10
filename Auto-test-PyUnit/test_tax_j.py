import unittest
import tax_final as tax_f

class TestTax(unittest.TestCase):

    ### test progressive tax (no tax) ###
    def test_tax_j1(self):
        result = tax_f.Caltax(income_H = 156000, income_W = 120000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 7800)
        self.assertEqual(result.MPF_W, 6000)
        self.assertEqual(result.MPF, 13800)
        self.assertEqual(result.tax_H, 324)
        self.assertEqual(result.tax_W, 0)
        self.assertEqual(result.s_tax, 324)
        self.assertEqual(result.tax, 0)

    ### test join tax, separate tax better ###
    def test_tax_j2(self):
        result = tax_f.Caltax(income_H = 600000, income_W = 400000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 18000)
        self.assertEqual(result.MPF_W, 18000)
        self.assertEqual(result.MPF, 36000)
        self.assertEqual(result.tax_H, 58500)
        self.assertEqual(result.tax_W, 24500)
        self.assertEqual(result.s_tax, 83000)
        self.assertEqual(result.tax, 101000)

    ### test join tax, join tax better ###
    def test_tax_j3(self):
        result = tax_f.Caltax(income_H = 600000, income_W = 120000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 18000)
        self.assertEqual(result.MPF_W, 6000)
        self.assertEqual(result.MPF, 24000)
        self.assertEqual(result.tax_H, 58500)
        self.assertEqual(result.tax_W, 0)
        self.assertEqual(result.s_tax, 58500) 
        self.assertEqual(result.tax, 55440)   

    ### test join tax, separate tax better, Husband pay stand tax ###
    def test_tax_j4(self):
        result = tax_f.Caltax(income_H = 2200000, income_W = 1200000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 18000)
        self.assertEqual(result.MPF_W, 18000)
        self.assertEqual(result.MPF, 36000)
        self.assertEqual(result.stand_tax_H, 327300)
        self.assertEqual(result.tax_W, 160500)
        self.assertEqual(result.s_tax, 487800)
        self.assertEqual(result.stand_tax, 504600)

    ### test join tax, separate tax better, Wife pay stand tax ###
    def test_tax_j5(self):
        result = tax_f.Caltax(income_H = 1500000, income_W = 3000000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 18000)
        self.assertEqual(result.MPF_W, 18000)
        self.assertEqual(result.MPF, 36000)
        self.assertEqual(result.tax_H, 211500)
        self.assertEqual(result.stand_tax_W, 447300)
        self.assertEqual(result.s_tax, 658800)
        self.assertEqual(result.stand_tax, 669600)     

    ### test join tax = separate tax, Husband and Wife pay stand tax ###
    def test_tax_j6(self):
        result = tax_f.Caltax(income_H = 900000000, income_W = 250000000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 18000)
        self.assertEqual(result.MPF_W, 18000)
        self.assertEqual(result.MPF, 36000)
        self.assertEqual(result.stand_tax_H, 134997300)
        self.assertEqual(result.stand_tax_W, 37497300)
        self.assertEqual(result.s_tax, 172494600)
        self.assertEqual(result.stand_tax, 172494600)  

    def test_tax_j7(self):
        result = tax_f.Caltax(income_H = 2040000, income_W = 2040000)
        result.tax_j()
        self.assertEqual(result.MPF_H, 18000)
        self.assertEqual(result.MPF_W, 18000)
        self.assertEqual(result.MPF, 36000)
        self.assertEqual(result.tax_H, 303300)
        self.assertEqual(result.tax_W, 303300)
        self.assertEqual(result.s_tax, 606600)
        self.assertEqual(result.stand_tax, 606600)                                       

if __name__ == '__main__':
    unittest.main()