import flet as ft

def add_page(page: ft.Page):
    page.title = "Tela 2"
    page.views.clear()
    page.views.append(

        ft.View(
            "/addpage",
            [
                #TOP TITLE
                ft.Row(
                    controls=[
                        ft.Text(
                            value= "Adicionar Viagem", style= "headlineMedium",
                            weight= ft.FontWeight.BOLD,
                        ),
                    ]
                ),

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
                            icon= "save", 
                            text= "Salvar", 
                            on_click= {},
                        ),
                    ]
                ),

                ft.BottomAppBar(
                    
                    bgcolor=ft.colors.GREY_800,
                    content=ft.Row(
                        alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.HOME, 
                                icon_color=ft.colors.WHITE,
                                on_click= lambda _: page.go("/")
                            ),
                            ft.IconButton(
                                icon=ft.icons.CALCULATE, 
                                icon_color=ft.colors.WHITE,
                                on_click= lambda _: page.go("/financias")
                            ),
                        ]
                    ),
                )
            ],
        ),
    ),
    page.update()
