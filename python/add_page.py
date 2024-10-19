import flet as ft
import uuid

comprador = ft.TextField(label="Digite aqui", width=350)
data = ft.TextField(label="Digite aqui", width=350)
origem = ft.TextField(label="Digite aqui", width=350)
destino = ft.TextField(label="Digite aqui", width=350)
valor = ft.TextField(label="Digite aqui", width=350)
num_animais = ft.TextField(label="Digite aqui", width=350)

def add_page(page: ft.Page):

    def nome(e):
          list = []
          list.append({
               "Comprador": comprador.value, 
               "Data": data.value,
               "Origem": origem.value,
               "Destino": destino.value,
               "Valor": valor.value,
               "NumeroDeAnimais": num_animais.value,
               "Id": uuid.uuid4(),
               })
          print(list)


    page.title = "Tela 2"
    page.views.clear()
    page.views.append(

        ft.View(
            "/addpage",
            [
                #TOP TITLE
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
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
                        comprador
                    ]
                ),

                # TEXTFIELD DATA
                ft.Text(value= "Data"),
                ft.Row(
                    controls=[
                        data
                    ]
                ),

                # TEXTFIELD ORIGEM
                ft.Text(value= "Origem"),
                ft.Row(
                controls=[
                    origem
                    ]
                ),

                # TEXTFIELD DESTINO
                ft.Text(value= "Destino"),
                ft.Row(
                controls=[
                    destino
                    ]
                ),

                # TEXTFIELD VALOR
                ft.Text(value= "Valor"),
                ft.Row(
                controls=[
                    valor
                    ]
                ),

                # TEXTFIELD QUANTIDADE DE ANIMAIS   
                ft.Text(value= "Número de animais"),
                ft.Row(
                controls=[
                    num_animais
                    ]
                ),
                
                # BOTAO ADICIONAR
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls= [
                        ft.FilledButton(
                            icon= "save", 
                            text= "Salvar", 
                            on_click=
                                 nome,
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