
import portfolio as p
import security as sy
import stock as st
import trade as t


########################## STOCK TEST - WORKS ##################################
symb = 'aapl'
name = 'Apple'
pps = 0
ns = 0
tv = 0
pp = 0
dpla = 0
dplp = 0
date = '4/1/23'
tpla = 0
tplp = 0
pe = 0
eps = 0
de = 0
sector = 'large cap tech'
industry = 'industrial'
style = 'idk'

test_stock = st.Stock(symb,name,date,pps,ns,tv,pp,dpla,dplp,tpla,tplp,pe,eps,de,sector,industry,style)

print(test_stock.to_csv_row())

print()

print(test_stock.to_string())
#################################### WORKS ####################################

########################## PORTFOLIO TEST - WORKS ##################################
t_list = list()
t_list.append(test_stock)
t_list.append(test_stock)

stocks = p.Portfolio(t_list)

print(stocks.to_string())

print()

print(stocks.to_excel('csvtest.csv'))


####################################  ####################################