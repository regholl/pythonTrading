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
	def __init__(self, name, symbol, pps, ns, tv, pp, dpla, dplp, tpla, tplp, pe, eps, de, sector, industry, style): # use a DS with keys for the parameter data
		# This is included in the old program
		self.symbol = symbol # Ticker Symbol
		self.pps = pps # Price Per Share
		self.ns = ns # Number of Shares
		self.tv = tv # Total Value of Shares
		self.pp = pp # Purchase Price of the Shares
		self.dpla = dpla # P/L Amount for the Day
		self.dplp = dplp # P/L Percentage for the Day

		# This is not covered in the old program, find dict keys! TODO
		self.name = name # Name of the Stock
		self.tpla = tpla # TotaL P/L Amount for the Day
		self.tplp = tplp # Total P/L Percentage
		self.pe = pe # PE Ratio
		self.eps = eps # Earnings per Share
		self.de = de # Dividends Earned
		self.sector = sector
		self.industry = industry
		self.style = style

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

	# TODO: either create a table for the position in Excel or update the data
	def to_sql(self):
		pass
		
# OUT OF CLASS

# Flow:
# API->json->object->CSV/SQL

def json_to_obj(): pass
