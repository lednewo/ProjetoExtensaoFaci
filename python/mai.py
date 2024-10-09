import flet as ft
from python.components.card_informacoes import cardinfo


def main(page: ft.Page):
    # Definindo o título da página
    page.title = "Flet"
    page.window_width = 430
    page.window_height = 932


    #clicksfunction
    def click_index(e):
        bt = e.control.selected_index
        if bt == 0:
            page.clean(),
            page.add(
                #TOP TITLE
                ft.Row(
                controls=[
                    ft.Text("Viagens", 
                            style= "headlineMedium",
                            weight= ft.FontWeight.BOLD)
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
                cardinfo,
                
            ), #adicionar conteudo
            page.update()


        # PAGINA FINANCIAS
        if bt == 1:
            page.clean()
            page.add(
                #TOP TITLE
                ft.Row(
                controls=[
                    ft.Text("Financias", 
                            style= "headlineMedium",
                            weight= ft.FontWeight.BOLD)
                ],
                alignment= ft.MainAxisAlignment.CENTER),

                ft.Divider(),
                ),
            page.update # conteúdo
        
        # PAGINA ADICIONAR
        if bt == 2:
            page.clean()
            page.add(
                #TOP TITLE
                ft.Row(
                controls=[
                    ft.Text("Adicionar", 
                            style= "headlineMedium",
                            weight= ft.FontWeight.BOLD)
                ],
                alignment= ft.MainAxisAlignment.CENTER),

                ft.Divider(),

                # TEXTFIELD COMPRADOR
                ft.Text(value= "Comprador"),
                ft.Row(
                controls=[
                    ft.TextField(
                        label="Digite aqui", 
                        width=350),
                    ]
                ),

                # TEXTFIELD DATA
                ft.Text(value= "Data"),
                ft.Row(
                controls=[
                    ft.TextField(
                        label="Digite aqui", 
                        width=350),
                    ]
                ),

                # TEXTFIELD ORIGEM
                ft.Text(value= "Origem"),
                ft.Row(
                controls=[
                    ft.TextField(
                        label="Digite aqui", 
                        width=350),
                    ]
                ),

                # TEXTFIELD DESTINO
                ft.Text(value= "Destino"),
                ft.Row(
                controls=[
                    ft.TextField(
                        label="Digite aqui", 
                        width=350),
                    ]
                ),

                # TEXTFIELD VALOR
                ft.Text(value= "Valor"),
                ft.Row(
                controls=[
                    ft.TextField(
                        label="Digite aqui", 
                        width=350,
                        ),
                    ]
                ),

                # TEXTFIELD QUANTIDADE DE ANIMAIS   
                ft.Text(value= "Número de animais"),
                ft.Row(
                controls=[
                    ft.TextField(
                        label="Digite aqui", 
                        width=350,
                        ),
                    ]
                ),
                
                # BOTAO ADICIONAR
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls= [
                        ft.FilledButton(
                            icon= "add", 
                            text= "Adicionar", 
                            on_click= {},
                        ),
                    ]
                )
            ),



    # Botton navigator
    page.navigation_bar = ft.NavigationBar(
        on_change=click_index,
        destinations=[
            #PAGE HOME
            ft.NavigationDestination(icon=ft.icons.EXPLORE,
            label="Viagens", ),

            #PAGE FINANCIAS
            ft.NavigationDestination(icon=ft.icons.CALCULATE, label="Financias"),

            #PAGE ADICIONAR
            ft.NavigationDestination(icon=ft.icons.ADD, label="Adicionar"),
        ]
    )

    # ADD IN PAGE
    page.add(
        
    ) 
    

ft.app(target=main)
