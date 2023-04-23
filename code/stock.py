# Author: Trevor Rowland
#
#	A Class and relevant Functions to define a stock object, stores name, price and other relevant info.
# data to capture:
"""
- price
- num shares
- tot val of shares
- price bought at or price basis if multiple orders
- change in dollars
- change in %
- day change in dollars
- day change in %
- how long til you can cash out 1/2 and break even
- how long til you can cash out 1/3 and break even
- how long til you can cash out 1/4 and break even
- have I lost more than 1/2 my initial investment
- have I lost more than 2/3 my initial investment
- have I lost more than 3/4 my initial investment
- how much have I earned in dividends(cash and stock represented in $$$ with %s given)
- market cap
- eps
- pe ratio
- sort stocks by:
    - sector
    - industry
    - style
"""

class Stock:
	def __init__(self, data): # use a DS with keys for the parameter data
		self.name = ''
		self.ticker = ''
		self.price = ''
		self.num_shares = ''
		self.tot_val = self.price * self.num_shares
		self.price_basis = ''
		self.tot_chg_usd = ''
		self.tot_chg_pct = ''
		self.day_chg_usd = ''
		self.day_chg_pct = ''
		self.pe_ratio = ''
		self.eps = ''
		self.divs_earned = ''

		self.sector = ''
		self.industry = ''
		self.style = ''

	def to_string(self):
		ret = ''
		ret += 'NAME: ' + str(self.name) + ' | ' + str(self.ticker) + '; ' + str(self.tot_chg_pct) + ', $' + str(self.tot_chg_usd) + '\n'

		ret += 'PRICE: $' + str(self.price) + ' | '
		# add an up or down depending on day performance
		if self.day_chg_usd<0:
			ret += '(⬇) '
		elif self.day_chg_usd==0:
			ret += '(-) '
		else:
			ret += '(⬆) '
		ret += str(self.day_chg_pct) + ', $' + str(self.day_chg_usd) + '\n'

		ret += 'INIT: $' + str(self.price_basis) + ' | '
		if self.tot_chg_usd<0:
			ret += '(⬇) '
		elif self.tot_chg_usd==0:
			ret += '(-) '
		else:
			ret += '(⬆)'

		ret += str(self.day_chg_pct) + ', $' + str(self.day_chg_usd) + '\n'
		ret += 'NUM_SHARES: ' + str(self.num_shares) + '\n'
		ret += 'PE RATIO: ' + str(self.pe_ratio) + ' | EPS' + str(self.eps) + '\n'
		ret += 'DIVIDENDS EARNED: ' + str(self.divs_earned)

		return ret
	
	# TODO: put the stock in excel-friendly format
	def to_excel(self): 
		pass
		
# OUT OF CLASS

# Flow:
# API->json->object->CSV/SQL

def json_to_obj():return
