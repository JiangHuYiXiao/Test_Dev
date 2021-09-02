# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/6 9:21
# @Software       : Python-Selenium
# @Python_verison : 3.7
'''
要解释remote的作用并不容易，不过我们可以通过分析selenium中的代码的方式来理解他的作用。
我们知道webdriver支持多浏览器下的执行，这是因为webdriver针对每一个浏览器都重写了webdriver方法，所以在脚本运行时需要确定是哪个浏览器驱动，
'''
# 具体如下：
from selenium import webdriver
driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Ie()

# 下面就对这些驱动进行简单分析
# 在Python中的Lib目录下第三方包site_packages的selenium下的webdriver下
# C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver
# 查看其中任何一个驱动的目录发现都有一个webdriver.py文件，除了我们熟悉的firefox，ie，chrome外，其中还包括非常重要的remote。
# 从这个角度来看也可以把remote看做是一个驱动类型，而这个驱动比较特别，他不是支持某一个特定的浏览器或者平台而是一种配置模式，
# 我们在这种模式下指定任意的浏览器或者平台，这种模式的执行都需要selenium server的支持

# firefox
# 1、打开selenium包下的firefox，
# 路径为：C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox
# 先看firefox中的webdriver.py文件
'''
...
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from .extension_connection import ExtensionConnection
from .firefox_binary import FirefoxBinary
from .firefox_profile import FirefoxProfile
...
class WebDriver(RemoteWebDriver):

    # There is no native event support on Mac
    NATIVE_EVENTS_ALLOWED = sys.platform != "darwin"

    CONTEXT_CHROME = "chrome"
    CONTEXT_CONTENT = "content"

    _web_element_cls = FirefoxWebElement

    def __init__(self, firefox_profile=None, firefox_binary=None,
                 timeout=30, capabilities=None, proxy=None,
                 executable_path="geckodriver", options=None,
                 service_log_path="geckodriver.log", firefox_options=None,
                 service_args=None, desired_capabilities=None, log_path=None,
                 keep_alive=True):
                         if log_path:
            warnings.warn('use service_log_path instead of log_path',
                          DeprecationWarning, stacklevel=2)
            service_log_path = log_path
        if firefox_options:
            warnings.warn('use options instead of firefox_options',
                          DeprecationWarning, stacklevel=2)
            options = firefox_options
        self.binary = None
        self.profile = None
        self.service = None
'''
# 2、
# 查看__init__()初始化方法，因为selenium自带firefox驱动，这个驱动的重要配置在于firefox_profile和firefox_binary两个参数，
# 而这两个参数分别调用当前目录下的firefox_profile.py和firefox_binary.py文件

# 3、
# 我们在脚本中调用firefox驱动的脚本为selenium.webdriver.Firefox(),那么他是如何指向：
# C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site - packages\selenium\webdriver\firefox\webdriver.py文件中的Webdriver类呢？
# 关键是在于 C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver中的__init__.py文件
'''
from .firefox.webdriver import WebDriver as Firefox  # noqa
from .firefox.firefox_profile import FirefoxProfile  # noqa
from .firefox.options import Options as FirefoxOptions  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .chrome.options import Options as ChromeOptions  # noqa
from .ie.webdriver import WebDriver as Ie  # noqa
from .ie.options import Options as IeOptions  # noqa
from .edge.webdriver import WebDriver as Edge  # noqa
from .opera.webdriver import WebDriver as Opera  # noqa
from .safari.webdriver import WebDriver as Safari  # noqa
from .blackberry.webdriver import WebDriver as BlackBerry  # noqa
from .phantomjs.webdriver import WebDriver as PhantomJS  # noqa
from .android.webdriver import WebDriver as Android  # noqa
from .webkitgtk.webdriver import WebDriver as WebKitGTK # noqa
from .webkitgtk.options import Options as WebKitGTKOptions # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.action_chains import ActionChains  # noqa
from .common.touch_actions import TouchActions  # noqa
from .common.proxy import Proxy  # noqa

__version__ = '3.14.1'
'''
# 4、
# 从上可以看出，在webdriver中的__init__()对每一个浏览器都用了别名，别名为对应浏览器的名字，所以在调用不同浏览器时就简化了层级。

# chrome

# 1、查看C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\chrome下的webdriver.py文件
# WebDriver类
'''
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

class WebDriver(RemoteWebDriver):
    """
    Controls the ChromeDriver and allows you to drive the browser.

    You will need to download the ChromeDriver executable from
    http://chromedriver.storage.googleapis.com/index.html
    """

    def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
'''
# 2、查看C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver的__init__文件
'''
from .firefox.webdriver import WebDriver as Firefox  # noqa
from .firefox.firefox_profile import FirefoxProfile  # noqa
from .firefox.options import Options as FirefoxOptions  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .chrome.options import Options as ChromeOptions  # noqa
from .ie.webdriver import WebDriver as Ie  # noqa
from .ie.options import Options as IeOptions  # noqa
from .edge.webdriver import WebDriver as Edge  # noqa
from .opera.webdriver import WebDriver as Opera  # noqa
from .safari.webdriver import WebDriver as Safari  # noqa
from .blackberry.webdriver import WebDriver as BlackBerry  # noqa
from .phantomjs.webdriver import WebDriver as PhantomJS  # noqa
from .android.webdriver import WebDriver as Android  # noqa
from .webkitgtk.webdriver import WebDriver as WebKitGTK # noqa
from .webkitgtk.options import Options as WebKitGTKOptions # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.action_chains import ActionChains  # noqa
from .common.touch_actions import TouchActions  # noqa
from .common.proxy import Proxy  # noqa
'''
# 3、
# 由于selenium不自带chrome的驱动，所以需要通过executable_path="chromedriver"指定chromedriver驱动

# 通过上面我们很容易发现不管是firefox下的WebDriver还是chrome下的WebDrivre都继承了RemoteWebDriver类，
# 打开C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\remote\webdriver.py
'''
class WebDriver(object):
    """
    Controls a browser by sending commands to a remote server.
    This server is expected to be running the WebDriver wire protocol
    as defined at
    https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol

    :Attributes:
     - session_id - String ID of the browser session started and controlled by this WebDriver.
     - capabilities - Dictionaty of effective capabilities of this browser session as returned
         by the remote server. See https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
     - command_executor - remote_connection.RemoteConnection object used to execute commands.
     - error_handler - errorhandler.ErrorHandler object used to handle errors.
    """

    _web_element_cls = WebElement

    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None,
                 keep_alive=False, file_detector=None, options=None):
        """
        Create a new driver that will issue commands using the wire protocol.

        :Args:
         - command_executor - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.
         - desired_capabilities - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
         - browser_profile - A selenium.webdriver.firefox.firefox_profile.FirefoxProfile object.
             Only used if Firefox is requested. Optional.
         - proxy - A selenium.webdriver.common.proxy.Proxy object. The browser session will
             be started with given proxy settings, if possible. Optional.
         - keep_alive - Whether to configure remote_connection.RemoteConnection to use
             HTTP keep-alive. Defaults to False.
         - file_detector - Pass custom file detector object during instantiation. If None,
             then default LocalFileDetector() will be used.
         - options - instance of a driver options.Options class
        """
'''
# 通过查看remote下的WebDriver类我们发现在__init__()初始化方法中ommand_executor='http://127.0.0.1:4444/wd/hub'指定了
# hub主节点的ip，通过这个参数我们可以修改为任意机子的ip。
# 除了对机子的配置，我们还需要对浏览器进行配置
# 配置的文件是commmon下的desired_capabilities.p文件
# C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\common\desired_capabilities.py文件

'''
class DesiredCapabilities(object):
    """
    Set of default supported desired capabilities.

    Use this as a starting point for creating a desired capabilities object for
    requesting remote webdrivers for connecting to selenium server or selenium grid.

    Usage Example::

        from selenium import webdriver

        selenium_grid_url = "http://198.0.0.1:4444/wd/hub"

        # Create a desired capabilities object as a starting point.
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['platform'] = "WINDOWS"
        capabilities['version'] = "10"

        # Instantiate an instance of Remote WebDriver with the desired capabilities.
        driver = webdriver.Remote(desired_capabilities=capabilities,
                                  command_executor=selenium_grid_url)

    Note: Always use '.copy()' on the DesiredCapabilities object to avoid the side
    effects of altering the Global class instance.

    """

    FIREFOX = {
        "browserName": "firefox",
        "marionette": True,
        "acceptInsecureCerts": True,
    }

    INTERNETEXPLORER = {
        "browserName": "internet explorer",
        "version": "",
        "platform": "WINDOWS",
    }

    EDGE = {
        "browserName": "MicrosoftEdge",
        "version": "",
        "platform": "WINDOWS"
    }

    CHROME = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
    }

    OPERA = {
        "browserName": "opera",
        "version": "",
        "platform": "ANY",
    }

    SAFARI = {
        "browserName": "safari",
        "version": "",
        "platform": "MAC",
    }

    HTMLUNIT = {
        "browserName": "htmlunit",
        "version": "",
        "platform": "ANY",
    }

    HTMLUNITWITHJS = {
        "browserName": "htmlunit",
        "version": "firefox",
        "platform": "ANY",
        "javascriptEnabled": True,
    }

    IPHONE = {
        "browserName": "iPhone",
        "version": "",
        "platform": "MAC",
    }

    IPAD = {
        "browserName": "iPad",
        "version": "",
        "platform": "MAC",
    }

    ANDROID = {
        "browserName": "android",
        "version": "",
        "platform": "ANDROID",
    }

    PHANTOMJS = {
        "browserName": "phantomjs",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
    }

    WEBKITGTK = {
        "browserName": "MiniBrowser",
        "version": "",
        "platform": "ANY",
    }
'''
CHROME = {
    "browserName": "chrome",            # 浏览器名称
    "version": "",                      # 浏览器版本
    "platform": "ANY",                  # 测试平台，ANY表示默认平台
}
