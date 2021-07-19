# fed_tax_calculator.py

from dataclasses import dataclass, field


tax_rates = [.10, .12, .22, .24, .32, .37]
tax_brackets = [9700, 39475, 84200, 160725, 204100, 510300]


@dataclass
class FedTaxCalc:
	'''
	Federal Tax Information
	'''
	rates: list		# Tax rates for each tax bracket.
	brackets: list	# Dollar value thresholds for each tax bracket.

	def federal_tax_calculator(self, income):
		tax = 0 								# Running total for final tax liability.
		income_decrement = income 				# Incremental portion of income remaining to apply to current tax bracket being calculated for next loop.
		tax_bracket_portion = 0 				# Amount of tax calculated for current bracket calculation on each loop.
		running_income_portion_calculated = 0	# Running total of income for which tax has already been calculated.
		income_after_tax = 0					# Final income remaining after all federal taxes have been calculated.
		for num in range(len(self.brackets)):
			# Make sure there is income remaining to be taxed.
			if income_decrement > 0:
				# print(f'calculated income portion: {tax_bracket_portion}')
				# Determines if income remaining or tax bracket portion should be used for current loop.
				tax_bracket_portion = min((self.brackets[num] - running_income_portion_calculated), income_decrement)
				# Keep track of total amount of income that taxes have already been calculated for.
				running_income_portion_calculated += tax_bracket_portion
				# print(f'current income portion calculating: {tax_bracket_portion}')
				# Determine taxes on current tax bracket portion.
				portion = tax_bracket_portion * self.rates[num]
				# print(f"this portion's income tax: {portion}")
				# Keep track of taxes calculated thus far.
				tax += portion
				# Calculate remaining income to calculate taxes on.
				income_decrement -= tax_bracket_portion
				# print(f'remaining income to be taxed {income_decremented}')
				# print('\n')
			# If there is no more income remaining to calculate taxes on.	
			else:
				# Determine final income after all bracket tax values have been calculated. 
				income_after_tax = income - tax
				break
		return f'Base Income: ${income:,.2f}, Tax: {tax:,.2f}, Income After Tax: {income_after_tax:,.2f}, Monthly Income: ${income_after_tax/12:,.2f}'

		
#results=FedTaxCalc(tax_rates, tax_brackets)
#print(results.federal_tax_calculator(100000))

