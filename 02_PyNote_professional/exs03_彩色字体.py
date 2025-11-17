""" 已封装
    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │ANSI 转义序列（ANSI Escape Sequences）是一种在终端中控制文本格式、颜色和光标位置的标准方式。
    │通过在输出的字符串中嵌入特定的转义代码，可以让终端显示不同颜色的文字、背景色、加粗、下划线等效果。
    │一般格式为： \033[<参数1;参数2;参数3>m<colorful text>\033[0m
    │    \033 是 ESC 字符的八进制表示（也可以写作 \x1b 或 \e，取决于语言支持）。
    │    [ 表示控制序列开始。
    │    <参数1;参数2;参数3> 是一个或多个用分号 ; 分隔的数字，用于指定样式、前景色、背景色等。
    │        参数1：字体格式
    │            0重置、1加粗、3斜体、4下划线、5闪烁、7反色
    │        参数2：字体颜色
    │            基础8色：30黑色、31红色、32绿色、33黄色、34蓝色、35品红、36青色、37白色
    │            高亮8色：90灰色、91亮红、92亮绿、93亮黄、94亮蓝、95洋红、96亮青、97亮白
    │        参数3：背景色，与字体颜色规则一致，基础色是4开头，高亮色是10开头
    │    m 表示这是一个“SGR”（Select Graphic Rendition）命令。
    │    <colorful text> 是显示文本
    │    \033[0m 恢复默认样式
    └──────────────────────────────────────────────────────────────────────────────────┘"""

def print_color():
    print("\033[31m这是红色文字\033[0m")
    print("\033[1;32m这是加粗绿色文字\033[0m")
    print("\033[4;33;44m下划线黄字蓝底\033[0m")
    print("\033[97;41m亮白字红底\033[0m")

# 上面的方式电单独调用比较麻烦，建议对方法进行封装
# ——————————————————————————————————————————————————————————————————————————————————————————————————
class Colorize:
    """
    用于生成带颜色和样式格式的ANSI转义序列文本的工具类
    标签：
        color(text, color='', background='', style='')
    支持的颜色（color）:
        0: black, 1: red, 2: green, 3: yellow, 4: blue, 5: magenta, 6: cyan, 7: white
    支持的样式（style）:
        bold(粗体), underline(下划线), blink(闪烁), reverse(反显), italics(斜体)
    """
    @staticmethod
    def color(text, color='', background='', style=''):
        start_code, end_code = '\033[', '\033[0m'
        colors = {'': '', 'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
                  'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37,
                  '0': 30, '1': 31, '2': 32, '3': 33, '4': 34, '5': 35, '6': 36, '7': 37}
        backgrounds = {'': '', 'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
                       'blue': 44, 'magenta': 45, 'cyan': 46, 'white': 47,
                       '0': 40, '1': 41, '2': 42, '3': 43, '4': 44, '5': 45, '6': 46, '7': 47}
        styles = {'': '', 'bold': 1, 'underline': 4, 'blink': 5, 'reverse': 7,
                  '0': 0, '1': 1, '3': 3, '4': 4, '5': 5, '7': 7}

        codes = [str(styles[style]), str(colors[color] if color in colors else ''),
                 str(backgrounds[background] if background in backgrounds else '')]
        codes = ';'.join([code for code in codes if code])  # 排除空字符串

        return f"{start_code}{codes}m{text}{end_code}"

# ——————————————————————————————————————————————————————————————————————————————————————————————————


if __name__ == '__main__':
    col = Colorize()
    print(col.color('Hello, World!', style='1', color='4', background='2'), "这是正常的字体。")
