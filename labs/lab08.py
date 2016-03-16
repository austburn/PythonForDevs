with open('/home/austin/learning/PythonForDevs/LabsData/tmpprecip2012.dat') as precip_data:
    total_precip = 0
    precip_days = 0
    for l in precip_data:
        precip = l[8:13]

        try:
            fprecip = float(precip)
        except ValueError:
            print 'I found bad data: {}'.format(precip)
            continue

        if fprecip > 0:
            precip_days +=1
            total_precip += fprecip

    print 'Days of Precipitation: {}; Total Precipitation: {}'.format(precip_days, total_precip)

