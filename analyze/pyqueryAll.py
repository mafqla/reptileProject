from pyquery import PyQuery as pq
doc = pq(url='https://skyseek.top')
# print(doc('title'))
items = doc('.list')
print(items)
lis = items.find('li')
print(lis.attr('href'))
a = doc('a')
for item in a.items():
    print(item.attr('href'))

print(a.text())
# print(a.html())
a.find('icon').remove()
print(a.text())