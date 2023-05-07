import db
class Security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    symbol = db.Column(db.String(5))
    security_type = db.Column(db.String(100))
    currency = db.Column(db.String(20))
    # add sector, style, industry later
    


    def __init__(self, name, symbol, type, currency, sector, style, industry):
        self.name = name
        self.symbol = symbol
        self.type = type
        self.currency = currency
        self.sector = sector
        self.style = style
        self.industry = industry