import flet as ft
from .components.card_informacoes import CartaoInformacoes

def main_page(page: ft.Page):
    page.title = "Main Page"
    page.views.clear()  # Limpa as telas anteriores
    page.views.append(
        ft.View(
            "/",
            [
                #TOP TITLE
                ft.Row(
                controls=[
                    ft.Text("Viagens", 
                                style= "headlineMedium",
                                weight= ft.FontWeight.BOLD),
                ],
                alignment= ft.MainAxisAlignment.CENTER),

                ft.Divider(),

                #TEXTFIELD
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.TextField(
                            label="Pesquisar", 
                            width=350),
                        ]
                ),
                
                CartaoInformacoes(
                    comprador= "comprador", 
                    data= "awdasd",
                    destino= "asdawd",
                    num_animais= "asdawd",
                    origem= "awdasd",
                    valor="1200"
                    ),


                ft.BottomAppBar(
                    bgcolor=ft.colors.GREY_800,
                    content=ft.Row(
                        alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.CALCULATE, 
                                icon_color=ft.colors.WHITE,
                                on_click= lambda _: page.go("/financias")
                            ),
                            ft.IconButton(
                                icon=ft.icons.ADD, 
                                icon_color=ft.colors.WHITE,
                                on_click= lambda _: page.go("/addpage")
                            ),
                        ]
                    ),
                )
            ],
        )
    )
    page.update()
    
