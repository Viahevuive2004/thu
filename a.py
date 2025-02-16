# d =  {'person':2, 'cat': 4,'spider':8}
# for animal in d:
#     print('A %s has %d legs'% (animal, d[animal]))
# for legs in d.values():
#     print('%d legs'%(legs))
# for animal, legs in d.items():
#     print('A %s has %d legs'%(animal, legs))
# def sign(x):
#     if x > 0:
#         return 'positive'
#     elif x < 0:
#         return 'negative'
#     else:
#         return 'zero'
# for x in [-1,0,1]:
#     print(sign(x))\
import numpy as nghia
# a = nghia.array([1,2,3])
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
# print(a)
# b = nghia.array([[1,2,3],[4,5,6]])
# print(b.shape)
# print(b[0, 0], b[0, 1], b[1, 0])
a = nghia.zeros((2,2))
print(a)
b = nghia.ones((1,2))
print(b)
c = nghia.full((2,2), 7)
print(c)
d =nghia.eye(2)
print(d)
e = nghia.random.random((2,2))
print(e)