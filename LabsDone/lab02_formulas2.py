
"""
Calculate the profit from the sale of stock and calculate the
new price of a product going on sale.  The results are formatted
 with and without thousands separators.
"""

shares = 125
purch_price = 25.32
sale_price = 48.97
profit1 = shares * (sale_price - purch_price)
print 'Profit is ${:.2f}'.format(profit1)  
print 'Profit is ${:,.2f}'.format(profit1)  # with thousands separator.

price = 127.99
discount = 0.16  # or 16%
sale_price = price - price * discount
print 'With a {:.0%} reduction, the sale price is ${:.2f}'.format(
    discount, sale_price)  
