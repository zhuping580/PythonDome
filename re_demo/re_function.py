import re


def re_findone():
    """
    查找一个匹配项
    search： 查找任意位置的匹配项
    match： 必须从字符串开头匹配
    fullmatch： 整个字符串与正则完全匹配
    :return:
    """
    text = 'a今天天气真好c!今天天气真好c'
    pattern = r'今天天气真好c'
    pattern2 = r'a今天天气真好c'
    pattern3 = r'a今天天气真好c!今天天气真好c'
    print('search:', re.search(pattern, text).group())
    print('match:', re.match(pattern2, text).group())
    print('fullmatch:', re.fullmatch(pattern3, text).group())


def re_findall():
    """
    findall： 从字符串任意位置查找，返回一个列表
    finditer：从字符串任意位置查找，返回一个迭代器
    :return:
    """
    text = 'a今天天气真好c!今天天气真好c'
    pattern = r'今天天气真好c'
    print('findall:', re.findall(pattern, text))
    print('finditer:', list(re.finditer(pattern, text)))


def re_split():
    """
    re.split(pattern, string, maxsplit=0, flags=0)
    函数：用 pattern 分开 string ，
    maxsplit表示最多进行分割次数，
    flags表示模式，就是上面我们讲解的常量！
    :return:
    """
    text = 'a今天天气真好c!今天天气真好c!今天天气真好c'
    pattern = r'!'
    print('split:', re.split(pattern, text, maxsplit=1, flags=re.I))


def re_sub():
    """
    re.sub(pattern, repl, string, count=0, flags=0)
    函数参数讲解：repl替换掉string中被pattern匹配的字符，
    count表示最大替换次数，
    flags表示正则表达式的常量。
    re.subn(pattern, repl, string, count=0, flags=0) 函数与 re.sub函数 功能一致，只不过返回一个元组 (字符串, 替换次数)
    :return:
    """
    text = 'a今天天气真好c!今天天气真好c!今天天气真好c'
    pattern = r'!'
    repl = '?'
    print('sub:', re.sub(pattern, repl, text, count=1, flags=re.I))
    print('subn:', re.subn(pattern, repl, text, count=0, flags=re.I))


def test_compile():
    """
    compile函数将正则表达式的样式编译为一个 正则表达式对象
    这个对象与re模块有同样的正则函数
    :return:
    """
    text = 'a今天天气真好c!今天天气真好c!今天天气真好c'
    pattern = r'今天天气真好c'
    print('compile:', re.compile(pattern).search(text).group())
