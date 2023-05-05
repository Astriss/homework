titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

a, b, c, d, e, f = store.values()
a1 = a[0]['quantity']*a[0]['price']
b1 = b[0]['quantity']*b[0]['price'] + b[1]['quantity']*b[1]['quantity']
c1 = c[0]['quantity']*c[0]['price'] + c[1]['quantity']*c[1]['quantity']
d1 = d[0]['quantity']*d[0]['price'] + d[1]['quantity']*d[1]['quantity']
e1 = e[0]['quantity']*e[0]['price'] + e[1]['quantity']*e[1]['quantity'] + e[2]['quantity']*e[2]['quantity']
f1 = f[0]['quantity']*f[0]['price']

a2, b2, c2, d2, e2, f2 = titles.keys()

print(f'{a2} total price - {a1} rub')
print(f'{b2} total price - {b1} rub')
print(f'{c2} total price - {c1} rub')
print(f'{d2} total price - {d1} rub')
print(f'{e2} total price - {e1} rub')
print(f'{f2} total price - {f1} rub')


