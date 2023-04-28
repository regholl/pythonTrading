# Author: Trevor Rowland
#
# A Class to serve as a Collection of Stocks

import csv

class Portfolio:
    def __init__(self, stocks): #input is a Disctionary of Stock Objects from the tda-api JSON
        self.stocks = stocks

    # TODO: toString and toExcel Methods
    def to_string(self):
        ret = ''

        for s in self.stocks:
            ret += s.to_string() + '\n\n'
        
        return ret

    def to_excel(self, csv_file):
        
        file = open(csv_file, 'w', newline = '')

        with file:
            header = ['Date', 'Symbol', 'Name', 'Price Per Share', 'Number of Shares', 'Total Value', 'Purchase Price', 'Daily Profit/Loss Amount', 'Daily Profit/Loss Percentage', 'Total Profit/Loss Amount', 'Total Profit/Loss Percentage', 'PE Ratio', 'Earnings Per Share', 'Dividends Earned', 'Sector', 'Industry', 'Style']
            writer = csv.DictWriter(file, fieldnames = header)

            for s in self.stocks:
                writer.writerow(s.to_csv_row())

        file.close()

        return 0 # idk what to return here TODO

        

    # Access Companies by the ROI, + winners and losers list
    def get_winners(self): # return all stocks with >50% return
        sorted = list()

        for s in self.stocks:
            if s.tot_chg_pct > .5:
                sorted.__add__(s)
            else:
                pass

        return sorted
    
    def get_losers(self): # return all stocks with > -50% return
        sorted = list()

        for s in self.stocks:
            if s.tot_chg_pct > (0-.5):
                sorted.__add__(s)
            else:
                pass

        return sorted
    
    def get_by_pct(self, pct): # return all stocks with a given percent return
        sorted = list()

        for s in self.stocks:
            if s.tot_chg_pct > pct:
                sorted.__add__(s)
            else:
                pass

        return sorted
    
    def get_by_dollars(self, usd): # return all stocks with a given dollar amount return
        sorted = list()

        for s in self.stocks:
            if s.tot_chg_pct > .5:
                sorted.__add__(s)
            else:
                pass

        return sorted
    
    # Access Companies by Type(Sector, Industry, Style)
    def get_by_sector(self, sector):
        sorted = list()

        for s in self.stocks:
            if s.sector == sector:
                sorted.__add__(s)
            else:
                pass
        
        return sorted
    
    def get_by_industry(self, industry):
        sorted = list()

        for s in self.stocks:
            if s.industry == industry:
                sorted.__add__(s)
            else:
                pass
        
        return sorted
    
    def get_by_style(self, style):
        sorted = list()

        for s in self.style:
            if s.sector == style:
                sorted.__add__(s)
            else:
                pass
        
        return sorted