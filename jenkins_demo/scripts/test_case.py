import pytest
import allure


@allure.feature('Test_all01')
class Test_all01():
    @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
    def test_setup(self):
        print("我就是打酱油的setup")

    @allure.step(title="run就是一个正常的方法.")
    def test_run(self):
        allure.attach("自定义描述1", "描述内容，自定义")
        print("我要运行")
        assert 1

    def test_skip(self):
        print("我要跳过")

    @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
    @allure.testcase("http://www.baidu.com/", "测试用例的地址")
    @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
    def test_error(self):
        allure.attach("自定义描述1", "我需要让他进行错误")
        print("我错误了")
        assert 1

    @allure.severity("critical")
    # @allure.epic("项目名称: 会所资源管理系统")
    # @allure.feature("资源管理模块")
    @allure.story("用例的标题: 对会所资源进行增、删、改、查")
    @allure.issue("http://149.335.82.12:8080/zentao/bug-view-1.html")  # 禅道bug地址
    @allure.testcase("http://149.335.82.12:8080/zentao/testcase-view-5-1.html")  # 禅道用例连接地址
    def test_next(self):
        allure.attach.file(r"C:\Users\eng-maxlong\Desktop\qq.png", name="这是图片", attachment_type=allure.attachment_type.PNG)
        assert 1


@allure.feature('Test_all02')
class Test_all02():
    @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
    def test_setup(self):
        print("我就是打酱油的setup")

    @allure.step(title="run就是一个正常的方法.")
    def test_run(self):
        allure.attach("自定义描述1", "描述内容，自定义")
        print("我要运行")
        assert 1

    def test_skip(self):
        print("我要跳过")

    @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
    @allure.testcase("http://www.baidu.com/", "测试用例的地址")
    @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
    def test_error(self):
        allure.attach("自定义描述1", "我需要让他进行错误")
        print("我错误了")
        assert 1

    @allure.severity("critical")
    # @allure.epic("项目名称: 会所资源管理系统")
    # @allure.feature("资源管理模块")
    @allure.story("用例的标题: 对会所资源进行增、删、改、查")
    @allure.issue("http://149.335.82.12:8080/zentao/bug-view-1.html")  # 禅道bug地址
    @allure.testcase("http://149.335.82.12:8080/zentao/testcase-view-5-1.html")  # 禅道用例连接地址
    def test_next(self):
        allure.attach.file(r"C:\Users\eng-maxlong\Desktop\qq.png", name="这是图片", attachment_type=allure.attachment_type.PNG)
        assert 1