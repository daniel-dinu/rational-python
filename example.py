from rational.rational import Rational


__author__ = 'Daniel Dinu'


r = Rational(1, 2)
print('Object:      {}'.format(repr(r)))
print('Numerator:   {}'.format(r.numerator))
print('Denominator: {}'.format(r.denominator))
print('Value:       {}'.format(r.value))
print('Quotient:    {}'.format(r.quotient))
print('Remainder:   {}'.format(r.remainder))

print()


a = Rational(1, 2)
b = Rational(a)
c = 0

print('Initial: a = {}; b = {}'.format(a, b))
a += 1
b = 2 - b
print('Final:   a = {}; b = {}'.format(a, b))

print()

print('Initial: a = {}; b = {}'.format(a, b))
a = r / b
b = a * r
print('Final:   a = {}; b = {}'.format(a, b))

print()

print('Initial: a = {}; c = {}'.format(a, c))
a **= 2
c = 2 ** b
print('Final:   a = {}; c = {}'.format(a, c))

print()

d = Rational(a - b)
print('Initial:                {}'.format(d))
print('Absolute value:         {}'.format(abs(d)))
print('Additive inverse:       {}'.format(-d))
print('Multiplicative inverse: {}'.format(~d))

print()

s = 0
for i in range(1, 10):
    s += Rational(1, i)
print('s = {} = {}'.format(s, s.value))

p = 1
for i in range(1, 10):
    p *= Rational(1, i)
print('p = {} = {}'.format(p, p.value))

print()

print('{} <  {} : {}'.format(s, p, s < p))
print('{} <= {} : {}'.format(s, p, s <= p))
print('{} == {} : {}'.format(s, p, s == p))
print('{} != {} : {}'.format(s, p, s != p))
print('{} >= {} : {}'.format(s, p, s >= p))
print('{} >  {} : {}'.format(s, p, s > p))




import numbers
numbers.Rational