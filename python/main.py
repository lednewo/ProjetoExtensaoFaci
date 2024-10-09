import flet as ft
from add_page import add_page  # Importa add_page
from main_page import main_page  # Importa main_page
from Financias_page import financias  # Importa finanicas

def main(page: ft.Page):
    # Definindo o título da página
    page.title = "Flet"
    page.window_width = 430
    page.window_height = 932
    page.update()

    # Função para gerenciar as mudanças de rota
    def route_change(route):
        if page.route == "/":
            main_page(page)
        elif page.route == "/addpage":
            add_page(page)
        elif page.route == "/financias":
            financias(page)

    page.on_route_change = route_change
    page.go(page.route)

# Inicializando o app
ft.app(target=main)
