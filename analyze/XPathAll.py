# XPth 练习
"""
/ 从当前节点选取直接子节点
// 从当前节点选取子孙节点
. 选取当前节点
.. 选取当前节点的父节点
@ 选取属性
"""

from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)
html2 = etree.parse('test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
result2 = html2.xpath('//li[@class="item-0"]/a/text()')
print('result2: ', result2)
grid = html.xpath('//li')
print(grid)