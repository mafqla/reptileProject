# Beautiful Soup 解析库的练习
import re

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>品优购商城-综合网购首选-正品低价、品质保障、配送及时、轻松购物！
    </title>
</head>
<body>
<p class="title" name="test"><b>正品保障,提供发票</b></p>
    <section class="shortcut">
        <div class="w">
            <div class="fl">
                <ul>
                    <li>品优购欢迎您！&nbsp;</li>
                    <li>
                        <a href="#">请登录</a> &nbsp; <a href="#" class="style_red">免费注册</a>
                    </li>
                </ul>
            </div>
            <div class="fr">
                <ul>
                    <li>我的订单</li>
                    <li></li>
                    <li class="arrow-icon">我的品优购</li>
                    <li></li>
                    <li>品优购会员</li>
                    <li></li>
                    <li>企业采购</li>
                    <li></li>
                    <li class="arrow-icon">关注品优购</li>
                    <li></li>
                    <li class="arrow-icon">客户服务</li>
                    <li></li>
                    <li class="arrow-icon">网站导航</li>
                </ul>
            </div>
        </div>
    </section>
    <!-- 快捷导航模块 end -->
    <!-- header头部模块制作 start -->
    <header class="header w">
        <!-- logo模块 -->
        <div class="logo">
            <h1>
                <a href="index.html" title="品优购商城">品优购商城</a>
            </h1>
        </div>
        <!-- search搜索模块 -->
        <div class="search">
            <input type="search" name="" id="" placeholder="语言开发">
            <button>搜索</button>
        </div>
        <!-- hotwords模块制作 -->
        <div class="hotwords">
            <a href="#" class="style_red">优惠购首发</a>
            <a href="#">亿元优惠</a>
            <a href="#">9.9元团购</a>
            <a href="#">美满99减30</a>
            <a href="#">办公用品</a>
            <a href="#">电脑</a>
            <a href="#">通信</a>
        </div>
        <!-- 购物车模块 -->
        <div class="shopcar">
            我的购物车
            <i class="count">8</i>
        </div>
    </header>
    <!-- header头部模块制作 end -->
    <!-- nav模块制作 start -->
    <nav class="nav">
        <div class="w">
            <div class="dropdown">
                <div class="dt">全部商品分类</div>
                <div class="dd">
                    <ul>
                        <li><a href="#">家用电器</a> </li>
                        <li><a href="#">手机</a>、 <a href="#">数码</a>、<a href="#">通信</a> </li>
                        <li><a href="#">电脑、办公</a> </li>
                        <li><a href="#">家居、家具、家装、厨具</a> </li>
                        <li><a href="#">男装、女装、童装、内衣</a> </li>
                        <li><a href="#">个户化妆、清洁用品、宠物</a> </li>
                        <li><a href="#">鞋靴、箱包、珠宝、奢侈品</a> </li>
                        <li><a href="#">运动户外、钟表</a> </li>
                        <li><a href="#">汽车、汽车用品</a> </li>
                        <li><a href="#">母婴、玩具乐器</a> </li>
                        <li><a href="#">食品、酒类、生鲜、特产</a> </li>
                        <li><a href="#">医药保健</a> </li>
                        <li><a href="#">图书、音像、电子书</a> </li>
                        <li><a href="#">彩票、旅行、充值、票务</a> </li>
                        <li><a href="#">理财、众筹、白条、保险</a> </li>

                    </ul>
                </div>
            </div>
             <ul class="1" id="sss">
                    <li>服装城</li>
                </ul>
        </div>
    </nav>
    <!-- nav模块制作 end -->

    <!-- 底部模块的制作 start -->
    <footer class="footer">
        <div class="w">
            <div class="mod_service">
                <ul>
                    <li>
                        <h5></h5>
                        <div class="service_txt">
                            <h4>正品保障</h4>
                            <p>正品保障,提供发票</p>
                        </div>
                    </li>
                    <li>
                        <h5></h5>
                        <div class="service_txt">
                            <h4>正品保障</h4>
                            <p>正品保障,提供发票</p>
                        </div>
                    </li>
                    <li>
                        <h5></h5>
                        <div class="service_txt">
                            <h4>正品保障</h4>
                            <p class="title" name="test">正品保障,提供发票</p>
                        </div>
                    </li>
                    <li>
                        <h5></h5>
                        <div class="service_txt">
                            <h4>正品保障</h4>
                            <p>正品保障,提供发票</p>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="mod_help">
                <dl>
                    <dt>帮助中心</dt>
                    <dd>
                        <img src="images/wx_cz.jpg" alt="">
                        品优购客户端
                    </dd>
                </dl>
            </div>
            <div class="mod_copyright">
                    <div class="links">
                            <a href="#">关于我们</a>  |  <a href="#">联系我们</a>  |  联系客服  |  商家入驻  |  营销中心  |  手机品优购  |  友情链接  |  销售联盟  |  品优购社区  |  品优购公益  |  English Site  |  Contact U
                    </div>
                    <div class="copyright">
                            地址：北京市昌平区建材城西路金燕龙办公楼一层 邮编：100096 电话：400-618-4000 传真：010-82935100 邮箱: zhanghj+itcast.cn <br>
                            京ICP备08001421号京公网安备110108007702
                    </div>
            </div>
        </div>
    </footer>
    <!-- 底部模块的制作 end -->
</body>

</html>
"""
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
print(soup.title.string)
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)
# 获取节点名称
print(soup.title.name)

# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])

# 获取文本内容
print('\t\n\v')
print(soup.p.string)
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 获取子节点和子孙节点

print(soup.p.contents)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 得到所有子孙节点
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print("descendants:", i, child)

# 获取父节点
print(soup.a.parent)

# 获取所有祖先节点
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 获取兄弟节点
print("Next Sibling", soup.a.next_sibling)
print("Prev", soup.a.previous_sibling)

# 方法选择器
# find_all()
print(soup.find_all(name='dt'))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))

print(soup.find_all(text=re.compile('ICP')))


# css选择器

# print(soup.select('ul li'))
for ul in soup.select('ul'):
    print(ul['id'])
    print(type(ul.attrs['id']))