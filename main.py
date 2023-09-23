import csv, time
time.sleep(1.5)
a = '\033[4m🌟SHOP $$ TRACKER🌟\033[0m'
print(f'\033[1;33m{a:^50}\033[0m')
print()
time.sleep(1.5)
total = 0
with open('Day54Totals.csv') as a:
  b = csv.DictReader(a)
  for i in b:
    c = int(i['Quantity'])
    e = float(i['Cost'])
    d = e * c
    #print(f'{c} | {e:^6} | {d:^6}')
    total += d
print(f'Your shop made a total profit of ${round(total,2)} today.')