buy_price = 25.32
sell_price = 48.97
num_shares = 125

profit = (sell_price - buy_price) * 125

print 'You made ${} on {} shares'.format(profit, num_shares)


product_price = 127.99
sale_reduction = 0.16
sale_price = product_price * (1 - sale_reduction)

print 'The product you are interested is on sale for ${:.2f}'.format(sale_price)
