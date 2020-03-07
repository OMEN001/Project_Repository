#_*_conding:utf-8_*_
#@Time    :2020/3/215:36
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

"""
selenium是什么？ selenium是一款基web网页的UI自动化测试框架
    （1）ide录制工具  -- 代码录制工具，
    （2）selenium webdriver  --访问网页、可以在网页中进行输入、点击等操作
    （3）grid(分布式)    --支持多浏览器的操作（IE、Chrome、Firefox）
    （4）跨平台操作   --windows、Linux、Mac
    （5）支持多语言  -- Python、Java


元素定位？
    （1）绝对定位： 以 / 开头
    （2）相对路径： 以 // 开头
        标签名[@属性名称=值]
        逻辑运算：and or    //标签名[@属性名称=值 and @属性名称=值]
        文本定位：//标签名[text()=文本值]
        包含定位：//标签名[contains(@属性,值)]   //标签名[contains(text(),值)]
        层级定位：//div[@id="u1"]//a[@name="tj_login"]

selenium webdriver的工作原理？
    （1）客户端脚本（java、python、ruby）不能直接与浏览器进行通信，webdriver(chrome、IE、FireFox)浏览器驱动程序将客户端的
        脚本解析成浏览器可以识别的代码，然后发送http请求到浏览器，浏览器根据收到的请求做相应的操作并且返回结果。

元素在页面的3中状态
    （1）存在  --能够找到
    （2）可用  --呈现在浏览器的页面当中，可以看的见
    （3）可见  --如输入框和按钮的操作

为什么要等待？ 要操作的元素尚未加载出来
    （1）后台数据请求
    （2）网络速度很慢
    （3）页面渲染需要时间

等待的三种方式？
    （1）强制等待  --time.sleep(5)   强制等待设置的等待时间，无论什么情况都会在等待时间外执行后续的代码
    （2）隐性等待  --implicitly_wait(5)
        (a) 一个driver会话只设置一次，全局都可以用
        (b)设置最长等待时间，在这个时间点内只要加载完成，则执行下一步代码。
    （3）显性等待 -- WebDriverWait(driver,等待时长，轮循周期).util/unitl_not(判断条件)
        (a) 设置了最大的等待时间，程序每隔一个轮循周期去看一眼，如条件成立，则执行下一步，否则继续等待。
            直到超过最大等待时间，然后抛出异常
        (b) WebDriverWait --显性等待类   expected_conditions --提供了一系列期望发生的条件
        (c) expected_conditions 的部分条件类
            (A) visibility_of_element_locted  判断某个元素是否可见，可见代表元素非隐藏
            (B) presence_of_element_locted   判断某个元素是否被加载到DOM树里面，并不代表该元素一定可见
            (C) title_is 判断当前页面的title是否精确等于预期

什么时候要等待？
    （1）元素操作之前都请等一等
    （2）页面跳转应该等一等


PO模式    --pageobjct-页面对象
    （1）页面对象和测试用例的彻底分离

有点
    （1）页面当中元素定位与元素操作与测试用例无关
    （2）页面当中调用顺序发生了变化与测试对象无关










"""
