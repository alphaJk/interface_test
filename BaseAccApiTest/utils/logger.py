import logging
import sys

from colorama import Back, Fore, Style, init
from colorlog import ColoredFormatter

init(autoreset=True)

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


def setup_logger(log_level, log_file=None):
    """
    setup root logger with ColoredFormatter.
    使用ColoredFormatter设置根日志记录器。

    """

    # 获取对象object的属性,获取logging对象的'log_level'属性值，不存在是返回None
    # getattr() 函数用于返回一个对象属性值，如果没有返回默认值。upper() 方法将字符串中的小写字母转为大写字母
    level = getattr(logging, log_level.upper(), None)
    # 如果level不存在
    if not level:
        color_print("Invalid log level: %s" % log_level, "RED")
        # 程序退出
        sys.exit(1)

    # hide traceback when log level is INFO/WARNING/ERROR/CRITICAL
    if level >= logging.INFO:
        sys.tracebacklimit = 0

    # 指定输出个格式
    formatter = ColoredFormatter(
        u"%(log_color)s%(bg_white)s%(levelname)-8s%(reset)s %(message)s",
        datefmt=None,
        reset=True,
        log_colors=log_colors_config
    )
    # 文件日志存储名称
    if log_file:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler()

    # 通过setFormatter指定输出格式
    handler.setFormatter(formatter)
    # 为logger添加的日志处理器
    logging.root.addHandler(handler)
    # 指定日志的最低输出级别，默认为WARN级别
    logging.root.setLevel(level)


def coloring(text, color="WHITE"):
    fore_color = getattr(Fore, color.upper())
    return fore_color + text


# 颜色打印
def color_print(msg, color="WHITE"):
    # 获取对象的颜色属性
    fore_color = getattr(Fore, color.upper())
    print(fore_color + msg)


def log_with_color(level):
    """ log with color by different level
    """

    def wrapper(text):
        color = log_colors_config[level.upper()]
        getattr(logging, level.lower())(coloring(text, color))

    return wrapper


log_debug = log_with_color("debug")
log_info = log_with_color("info")
log_warning = log_with_color("warning")
log_error = log_with_color("error")
log_critical = log_with_color("critical")
