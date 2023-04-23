# Author: Trevor Rowland
#
# A Class to serve as a Collection of Stocks

class Portfolio:
    def __init__(self, stocks): #input is a Disctionary of Stock Objects from the tda-api JSON
        self.stocks = stocks

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
    
    def get_by_style(self):
        sorted = list()

        for s in self.style:
            if s.sector == style:
                sorted.__add__(s)
            else:
                pass
        
        return sorted