while True:
    user_input = raw_input('Temperature in Farenheit: ')
    if isinstance(user_input, str) and user_input.lower() == 'q':
        exit()

    try:
        farenheit = float(user_input)
    except ValueError:
        print 'Must enter a number or `q` to quit!'
        continue


    centigrade = (5.0/9.0)*(farenheit - 32)

    print '{:.1f} degrees Farenheit is equivalent to {:.1f} degrees Centigrade'.format(farenheit, centigrade)
