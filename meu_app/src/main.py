import flet as ft


def main(page: ft.Page):
    page.title = 'Minha Calculadora'
    resultado = ft.Text(value = '0')

    # operação de soma
    def somar():
        pass

    # operação de subtração
    def subtração():
        pass

    # operação de multiplicação
    def multiplicacao():
        pass

    # operação de divisão
    def divisao():
        pass

    
    page.add(
        ft.Row([resultado]),
        ft.Row([ft.Button('AC'), ft.Button('-/+'), ft.Button('%'), ft.Button('/')]),
        ft.Row([ft.Button('7'), ft.Button('8'), ft.Button('9'), ft.Button('*')]),
        ft.Row([ft.Button('4'), ft.Button('5'), ft.Button('6'), ft.Button('-')]),
        ft.Row([ft.Button('1'), ft.Button('2'), ft.Button('3'), ft.Button('+')]),
        ft.Row([ft.Button('0'), ft.Button('.'), ft.Button('=')])
    )

if __name__ == '__main__':
    ft.run(main)
