# tmail-auto-buy
天猫抢购秒杀，出于帮忙的缘故，只对抢口罩做了优化

如果有兴趣可以帮我补充

    使用说明：
    1. 我同时尝试了Edge和Chrome，发现只有Chrome可以用selenium发送表头。如果没有表头会被天猫拦截，所以只能用Chrome
    2. 测试时我把不同版本的文件放在了一起，最后我所使用的是 auto_buy_fm2.py ， 操作比较简单，应该都能看懂
    3. 原作者 https://github.com/thelastleft-back/taobao-tianmao-auto-buy 我是在他的基础上做了补充
    4. 只优化了抢口罩，其它的管不管用我不知道

    提示：
    1. pip install selenium
    2. 下载对应版本的 ChromeDriver http://npm.taobao.org/mirrors/chromedriver/, 查看版本号：navigator.appVersion
    
    使用步奏：
    1. 选择商城并输入开售时间
    2. 程序自动打开chrome浏览器访问链接，跳至登陆页面，请选择扫码登陆（密码登录会被拦截）
    3. 开售后自动下单，在淘宝规定时间内完成支付