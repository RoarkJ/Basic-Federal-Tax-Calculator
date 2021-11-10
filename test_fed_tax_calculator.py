# test_fed_tax_calculator.py

from unittest import TestCase
from fed_tax_calculator_dataclasses import FedTaxCalc

tax_rates = [.10, .12, .22, .24, .32, .37]
tax_brackets = [9700, 39475, 84200, 160725, 204100, 510300]

class TestFedTaxCalc(TestCase):
	def test_fed_tax_calc(self):
		tax = FedTaxCalc(tax_rates, tax_brackets)
		self.assertEqual('Base Income: $100,000.00, Tax: 18,174.50, Income After Tax: 81,825.50, Monthly Income: $6,818.79', tax.federal_tax_calculator(100000))
		
