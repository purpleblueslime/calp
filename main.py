vv = ['SA', 'SU', 'MO', 'TU', 'WE', 'TH', 'FR']

def yr(yy):
  if yy % 4 == 0: return True
  return False

def dys(yy, mm):
  if mm == 2: 
    if yy: return 29
    return 28
  if mm >= 8:
    if mm % 2 == 0: return 31
    return 30
  if mm % 2 == 0: return 30
  return 31

def dy(yy, mm, dd):
  mgic = [None, 6, 2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
  a = yy % 100
  b = round(a / 4)
  c = a + b + mgic[mm] + dd
  d = c % 7
  return vv[d]

yy = int(input('yy: '))
mm = int(input('mm: '))
ee = dys(yr(yy), mm)

fmt = 'SU    MO    TU    WE    TH    FR    SA'
print(fmt)

def ddfy(dd):
  if dd <= 9: return f'0{dd}'
  return f'{dd}'

def clrfy(_):
  for v in vv:
    _ = _.replace(v, '  ')
  return _

_ = fmt
for dd in range(1, ee+1):
  v = dy(yy, mm, dd)
  _ = _.replace(v, ddfy(dd))
  if v == 'SA':
    print(clrfy(_))
    _ = fmt

if _ != fmt: print(clrfy(_))