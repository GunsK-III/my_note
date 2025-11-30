import PySimpleGUI as sg

# 设置主题
sg.theme('DarkGrey5')

# 计算器历史记录
calculation_history = []


def format_number(num):
    """格式化数字显示，处理整数和浮点数"""
    if isinstance(num, float):
        # 处理浮点数精度问题，保留2位小数
        if num.is_integer():
            return str(int(num))
        else:
            # 四舍五入到2位小数，避免浮点数精度问题
            formatted = f"{round(num, 2):.2f}".rstrip('0').rstrip('.')
            # 如果进行了小数截断，记录提示信息
            original_str = f"{num:.10f}".rstrip('0').rstrip('.')
            formatted_str = formatted
            if '.' in original_str and '.' in formatted_str:
                original_decimals = len(original_str.split('.')[1])
                formatted_decimals = len(formatted_str.split('.')[1])
                if original_decimals > formatted_decimals:
                    return formatted, "保留2位小数"
            return formatted, None
    return str(num), None


def calculate(expression):
    """计算表达式结果"""
    try:
        # 简单的表达式计算（只支持整数和基础运算）
        if '+' in expression:
            parts = expression.split('+')
            if len(parts) == 2:
                return int(parts[0]) + int(parts[1]), None
        elif '-' in expression:
            parts = expression.split('-')
            if len(parts) == 2:
                return int(parts[0]) - int(parts[1]), None
        elif '×' in expression:
            parts = expression.split('×')
            if len(parts) == 2:
                return int(parts[0]) * int(parts[1]), None
        elif '÷' in expression:
            parts = expression.split('÷')
            if len(parts) == 2:
                dividend, divisor = int(parts[0]), int(parts[1])
                if divisor == 0:
                    return "错误：除零", None
                result = dividend / divisor
                formatted_result, decimal_note = format_number(result)
                return formatted_result, decimal_note
        return "错误", None
    except (ValueError, IndexError):
        return "错误", None


# 计算器按钮布局
button_layout = [
    # 第一行：显示区域和历史按钮
    [
        sg.Text('历史:', size=(6, 1)),
        sg.Button('查看历史', key='-HISTORY-', size=(8, 1)),
        sg.Button('清空历史', key='-CLEAR_HISTORY-', size=(8, 1)),
        sg.Button('MC', key='-MEM_CLEAR-', size=(4, 1)),
        sg.Button('MR', key='-MEM_RECALL-', size=(4, 1))
    ],
    # 第二行：显示区域
    [
        sg.Text('当前:', size=(6, 1)),
        sg.InputText('0', size=(20, 1), key='-DISPLAY-',
                     justification='right', font=('Arial', 14),
                     readonly=True, background_color='white', text_color='black')
    ],
    # 第三行：功能按钮
    [
        sg.Button('C', size=(5, 2), key='-CLEAR-', button_color=('white', 'red')),
        sg.Button('CE', size=(5, 2), key='-CLEAR_ENTRY-', button_color=('white', 'orange')),
        sg.Button('⌫', size=(5, 2), key='-BACKSPACE-'),
        sg.Button('÷', size=(5, 2), key='-DIVIDE-')
    ],
    # 第四行：数字和操作符
    [
        sg.Button('7', size=(5, 2), key='-7-'),
        sg.Button('8', size=(5, 2), key='-8-'),
        sg.Button('9', size=(5, 2), key='-9-'),
        sg.Button('×', size=(5, 2), key='-MULTIPLY-')
    ],
    # 第五行：数字和操作符
    [
        sg.Button('4', size=(5, 2), key='-4-'),
        sg.Button('5', size=(5, 2), key='-5-'),
        sg.Button('6', size=(5, 2), key='-6-'),
        sg.Button('-', size=(5, 2), key='-SUBTRACT-')
    ],
    # 第六行：数字和操作符
    [
        sg.Button('1', size=(5, 2), key='-1-'),
        sg.Button('2', size=(5, 2), key='-2-'),
        sg.Button('3', size=(5, 2), key='-3-'),
        sg.Button('+', size=(5, 2), key='-ADD-')
    ],
    # 第七行：底部按钮
    [
        sg.Button('0', size=(11, 2), key='-0-'),
        sg.Button('退出', size=(5, 2), key='-EXIT-', button_color=('white', 'darkred')),
        sg.Button('=', size=(5, 2), key='-EQUALS-', button_color=('white', 'blue'))
    ]
]

# 内存存储
memory_value = 0
current_input = "0"
current_operator = None
previous_value = None

# 创建窗口
layout = [
    [sg.Column(button_layout, element_justification='center')],
    [sg.StatusBar('就绪', key='-STATUS-', size=(50, 1))]
]

window = sg.Window('科学计算器', layout, finalize=True)

# 事件循环
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break

    display = window['-DISPLAY-']
    status = window['-STATUS-']

    # 数字按钮处理
    if event in ['-0-', '-1-', '-2-', '-3-', '-4-', '-5-', '-6-', '-7-', '-8-', '-9-']:
        digit = event.strip('-')
        if current_input == "0" or current_input == "错误":
            current_input = digit
        else:
            current_input += digit
        display.update(current_input)
        status.update('输入数字')

    # 操作符按钮处理
    elif event in ['-ADD-', '-SUBTRACT-', '-MULTIPLY-', '-DIVIDE-']:
        if current_input != "错误":
            previous_value = current_input
            current_input = "0"
            current_operator = {
                '-ADD-': '+',
                '-SUBTRACT-': '-',
                '-MULTIPLY-': '×',
                '-DIVIDE-': '÷'
            }[event]
            status.update(f'选择操作符: {current_operator}')

    # 等号按钮 - 执行计算
    elif event == '-EQUALS-':
        if previous_value is not None and current_operator is not None:
            expression = f"{previous_value}{current_operator}{current_input}"
            result, decimal_note = calculate(expression)

            # 记录计算历史
            history_entry = f"{expression} = {result}"
            if decimal_note:
                history_entry += f" ({decimal_note})"
            calculation_history.append(history_entry)

            current_input = str(result)
            display.update(current_input)
            previous_value = None
            current_operator = None

            # 更新状态信息
            if decimal_note:
                status.update(f'计算完成 - {decimal_note}')
            else:
                status.update('计算完成')

    # 清除按钮
    elif event == '-CLEAR-':
        current_input = "0"
        previous_value = None
        current_operator = None
        display.update(current_input)
        status.update('已清除')

    # 清除当前输入
    elif event == '-CLEAR_ENTRY-':
        current_input = "0"
        display.update(current_input)
        status.update('清除当前输入')

    # 退格按钮
    elif event == '-BACKSPACE-':
        if current_input != "0" and current_input != "错误":
            if len(current_input) > 1:
                current_input = current_input[:-1]
            else:
                current_input = "0"
            display.update(current_input)
            status.update('退格')

    # 查看历史记录
    elif event == '-HISTORY-':
        if calculation_history:
            history_text = "\n".join(calculation_history[-10:])  # 显示最近10条
            sg.popup_scrolled('计算历史:', history_text, size=(40, 15), title='历史记录')
        else:
            sg.popup('历史记录为空', title='历史记录')

    # 清空历史记录
    elif event == '-CLEAR_HISTORY-':
        calculation_history.clear()
        status.update('历史记录已清空')

    # 内存清除
    elif event == '-MEM_CLEAR-':
        memory_value = 0
        status.update('内存已清除')

    # 内存读取
    elif event == '-MEM_RECALL-':
        if memory_value != 0:
            current_input = str(memory_value)
            display.update(current_input)
            status.update('读取内存值')

window.close()
