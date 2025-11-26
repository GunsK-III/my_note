"""使用PySimpleGUI模块做一个简单加法计算器"""
import PySimpleGUI as sg


def fun1(a, b):
    return int(a) + int(b)


layout = [
    [sg.Text('输入a值:'), sg.InputText(key='-IN-A-')],
    [sg.Text('输入b值:'), sg.InputText(key='-IN-B-')],
    [sg.Button('计算'), sg.Push(), sg.Button('退出')],
    [sg.Text('结果:'), sg.Text('', key='-RESULT-')]
]

window = sg.Window('简单计算器', layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '退出':
        break
    if event == '计算':
        a = values['-IN-A-']
        b = values['-IN-B-']
        try:
            result = fun1(a, b)
            window['-RESULT-'].update(result)
        except ValueError:
            window['-RESULT-'].update('请输入有效的数字')

window.close()

# import PySimpleGUI as sg
#
# def create_window_1():
#     layout = [
#         [sg.Text('1')],
#         [sg.Button('退出')]
#     ]
#     window = sg.Window('窗口 1', layout)
#     while True:
#         event, values = window.read()
#         if event == '退出' or event == sg.WIN_CLOSED:
#             break
#     window.close()
#
# def create_window_2():
#     layout = [
#         [sg.Text('2')],
#         [sg.Button('退出')]
#     ]
#     window = sg.Window('窗口 2', layout)
#     while True:
#         event, values = window.read()
#         if event == '退出' or event == sg.WIN_CLOSED:
#             break
#     window.close()
#
# layout = [
#     [sg.Button('1'), sg.Button('2'), sg.Button('退出')]
# ]
#
# window = sg.Window('主窗口', layout)
#
# while True:
#     event, values = window.read()
#     if event == '1':
#         create_window_1()
#     elif event == '2':
#         create_window_2()
#     elif event == '退出' or event == sg.WIN_CLOSED:
#         break
#
# window.close()
