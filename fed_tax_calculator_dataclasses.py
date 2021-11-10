# fed_tax_calculator.py

from dataclasses import dataclass, field

# These are Single filing status 2019 rates and brackets.
tax_rates = [.10, .12, .22, .24, .32, .35, .37]
tax_brackets = [9700, 39475, 84200, 160725, 204100, 510300]

# dataclass is a mechanism for declaring class attributes without having to write all the extra code to delcare attributes in the constructor
# that need to be initialized when the class is instantiated.
@dataclass
class FedTaxCalc:
	'''
	Federal Tax Information
	'''
	rates: list # Tax rates for each tax bracket.
	brackets: list # Dollar value thresholds for each tax bracket.

	def federal_tax_calculator(self, income):
		tax = 0 # Running total for final tax liability.
		income_decremented = income # Incremental portion of income remaining to apply to current tax bracket being calculated for next loop.
		tax_bracket_portion = 0 # Amount of tax calculated for current bracket calculation on each loop.
		income_after_tax = 0 # Final income remaining after all federal taxes have been calculated.
		index = 0 # Keep track of current loop index.
		while income_decremented > 0:
			if index == 0:
				# Make sure there is income remaining to be taxed.
				# Determines if income remaining or tax bracket portion should be used.
				tax_bracket_portion= min(self.brackets[index], income_decremented)
				# Determine taxes on current tax bracket portion.
				portion = tax_bracket_portion * self.rates[index]
				# Keep track of taxes calculated thus far.
				tax += portion
				# Calculate remaining income to calculate taxes on.
				income_decremented -= tax_bracket_portion
				# If there is no more income remaining to calculate taxes on.
				index += 1
			elif index < 6 and index > 0:
				tax_bracket_portion= min((self.brackets[index]-self.brackets[index-1]), income_decremented)
				portion = tax_bracket_portion * self.rates[index]
				tax += portion
				income_decremented -= tax_bracket_portion
				index += 1
			else:
				tax_bracket_portion = income_decremented
				portion = tax_bracket_portion * self.rates[index]
				tax += portion
				income_decremented -= tax_bracket_portion
							
		# Determine final income after all bracket tax values have been calculated. 
		income_after_tax = income - tax
		return f'''Base Income: ${income:,.2f}, Tax: ${tax:,.2f}, Income After Tax: ${income_after_tax:,.2f}, Monthly Income After Tax: ${income_after_tax/12:,.2f}'''
		
# Uncomment the next two lines to enter an annual gross income to calculate.	
#results=FedTaxCalc(tax_rates, tax_brackets)
#print(results.federal_tax_calculator(100000))

