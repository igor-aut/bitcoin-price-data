path = '/Users/3sal/PycharmProjects/python-remembering/BTC-daily.csv'
file = open(path, 'r')
raw_data = file.read()
first_line = []
for part in raw_data.split('\n')[0].split(','):
    first_line.append(part)
raw_data = raw_data.split('\n')[1:]
price = []
for day in raw_data:
    day = day.split(',')
    day_price = int((float(day[4]) + float(day[5])) / 2)
    price.append([day[1].split(" ")[0], day_price])
price.reverse()
for item in price:
    print(item)
