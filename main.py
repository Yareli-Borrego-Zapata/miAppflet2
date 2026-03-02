import flet as ft

def main(page: ft.Page):
    page.title = "formulario de registro de eventis"
    page.padding = 20
    titulo = ft.Text(
        "Registro de Eventos",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="blue"
    )