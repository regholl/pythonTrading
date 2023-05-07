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
import csv

class Position():

	def __init__(self, name, symbol, date, pps, ns, tv, pp, dpla, dplp, tpla, tplp, pe, eps, de, sector, industry, style): # use a DS with keys for the parameter data
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
		self.date = date # date the API was accessed
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
		ret += 'NAME: ' + str(self.name) + ' | ' + str(self.symbol) + '; ' + str(self.tplp) + ', $' + str(self.tpla) + '\n'

		ret += 'PRICE: $' + str(self.pps) + ' | '
		# add an up or down depending on day performance
		if self.dpla<0:
			ret += '(⬇) '
		elif self.dpla==0:
			ret += '(-) '
		else:
			ret += '(⬆) '
		ret += str(self.dplp) + ', $' + str(self.dpla) + '\n'

		ret += 'INIT: $' + str(self.pp) + ' | '
		if self.tpla<0:
			ret += '(⬇) '
		elif self.tpla==0:
			ret += '(-) '
		else:
			ret += '(⬆)'

		ret += str(self.dplp) + ', $' + str(self.dpla) + '\n'
		ret += 'NUM_SHARES: ' + str(self.ns) + '\n'
		ret += 'PE RATIO: ' + str(self.pe) + ' | EPS: ' + str(self.eps) + '\n'
		ret += 'DIVIDENDS EARNED: ' + str(self.de)

		return ret
	
	# TODO: put the stock in excel-friendly format
	def to_csv_row(self): 
		to_return = dict()

		# TABLE FORMAT
		'''
		- Symbol
		- name
		- pps
		- ns
		- tv
		- pp
		- dpla
		- dplp
		- tpla
		- tplp
		- pe
		- eps
		- de
		- sector
		- industry
		- style
		'''
		to_return['Date'] = self.date
		to_return['Symbol'] = self.symbol
		to_return['Name'] = self.name
		to_return['Price Per Share'] = self.pps
		to_return['Number of Shares'] = self.ns
		to_return['Total Value'] = self.tv
		to_return['Purchase Price'] = self.pp
		to_return['Daily Profit/Loss Amount'] = self.dpla
		to_return['Daily Profit/Loss Percentage'] = self.dplp
		to_return['Total Profit/Loss Amount'] = self.tpla
		to_return['Total Profit/Loss Percentage'] = self.tplp
		to_return['PE Ratio'] = self.pe
		to_return['Earnings Per Share'] = self.eps
		to_return['Dividends Earned'] = self.de
		to_return['Sector'] = self.sector
		to_return['Industry'] = self.industry
		to_return['Style'] = self.style
		
		
		return to_return
	
	# Update SQL with the most recent API call
	def update_sql(self):
		pass
	
# OUT OF CLASS

# Flow:
# API->json->object->CSV/SQL

def json_to_obj(): pass
