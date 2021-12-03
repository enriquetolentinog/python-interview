from datetime import date, datetime

Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('Winter', (date(Y,  1,  1),  date(Y,  3, 18))),
           ('Spring', (date(Y,  3, 19),  date(Y,  6, 19))),
           ('Summer', (date(Y,  6, 20),  date(Y,  9, 21))),
           ('Fall', (date(Y,  9, 22),  date(Y, 12, 19))),
           ('Winter', (date(Y, 12, 20),  date(Y, 12, 31)))]

def get_status_order(orders):
    '''Return the "global" status in customer order if considerate all the items in the order'''
    if(not orders['status'][orders['status'].isin(['PENDING'])].empty):
        return 'PENDING'
    elif(orders['status'].size == orders['status'][orders['status'].isin(['CANCELLED'])].size):
        return 'CANCELLED'
    else:
        return 'SHIPPED'

def get_season(order_date):
    if isinstance(order_date, datetime):
        order_date = order_date.date()
    order_date = order_date.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= order_date <= end)

def detect_changes(weather):
    weather_changes_detected = []
    for index, elem in enumerate(weather):
        if (index < len(weather) and index - 1 >= 0):
            prev_el = weather[index-1]
            curr_el = elem
            if(not prev_el['was_rainy'] and curr_el['was_rainy']):
                weather_changes_detected.append(curr_el)
                
    return weather_changes_detected