import re

# re模块官方文档：https://docs.python.org/zh-cn...
# re模块库源码：https://github.com/python/cpy...


def reg_i():
    """
    语法： re.IGNORECASE 或简写为 re.I
    作用： 进行忽略大小写匹配。
    :return:
    """
    text = '今天天气真好A'
    pattern = r'今天天气真好a'
    print('默认模式：', re.findall(pattern, text))
    print('忽略大小写模式：', re.findall(pattern, text, re.I))


def reg_A():
    """
    语法： re.ASCII 或简写为 re.A
    作用： 顾名思义，ASCII表示ASCII码的意思，让 \w, \W, \b, \B, \d, \D, \s 和 \S 只匹配ASCII，而不是Unicode。
    :return:
    """
    text = '今天天气真好A'
    pattern = r'\w+'
    print('Unicode：', re.findall(pattern, text))
    print('ASCII：', re.findall(pattern, text, re.A))


def reg_S():
    """
    语法： re.DOTALL 或简写为 re.S
    作用： DOT表示.，ALL表示所有，连起来就是.匹配所有，包括换行符\n。默认模式下.是不能匹配行符\n的。
    :return:
    """
    text = '今天天气真好\nA'
    pattern = r'.*'
    print('默认模式：', re.findall(pattern, text))
    print('.匹配所有模式：', re.findall(pattern, text, re.S))


def reg_M():
    """
    语法： re.MULTILINE 或简写为 re.M
    作用： 多行模式，当某字符串中有换行符\n，默认模式下是不支持换行符特性的，比如：行开头 和 行结尾，而多行模式下是支持匹配行开头的。
    :return:
    """
    text = '今天天气真好\nA'
    pattern = r'^A'  # 正则表达式中^表示匹配行的开头
    print('默认模式：', re.findall(pattern, text))   # 默认模式下它只能匹配字符串的开头
    print('多行模式：', re.findall(pattern, text, re.M))  # 多行模式下，它还可以匹配 换行符\n后面的字符


def reg_X():
    """
    语法： re.VERBOSE 或简写为 re.X
    作用： 详细模式，可以在正则表达式中加注解！
    :return:
    """
    text = '今天天气真好A'
    pattern = r"""^今天   # 时间
                   天气   # 其他
               """
    print('默认模式：', re.findall(pattern, text))
    print('.匹配所有模式：', re.findall(pattern, text, re.X))


def reg_DEBUG():
    """
    语法： re.DEBUG
    作用： 显示编译时的debug信息。
    :return:
    """
    text = '今天天气真好A'
    pattern = r'天气'
    print('默认模式：', re.findall(pattern, text))
    print('.匹配所有模式：', re.findall(pattern, text, re.DEBUG))
