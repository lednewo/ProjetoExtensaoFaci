import flet as ft

def add_page(page: ft.Page):
    page.title = "Tela 2"

    # DICT PRA ARMAZENAR DADOS
    viagem_data = {}

    #VARIAVEIS DOS TEXTFIELDS
    comprador_field = ft.TextField(label="Digite aqui", width=350)
    data_field = ft.TextField(label="Digite aqui", width=350)
    origem_field = ft.TextField(label="Digite aqui", width=350)
    destino_field = ft.TextField(label="Digite aqui", width=350)
    valor_field = ft.TextField(label="Digite aqui", width=350)
    animais_field = ft.TextField(label="Digite aqui", width=350)

    # FUNÇAO SALVAR OS DADOS
    def save_data(e):
        # PEGAR VALOR
        viagem_data['comprador'] = comprador_field.value
        viagem_data['data'] = data_field.value
        viagem_data['origem'] = origem_field.value
        viagem_data['destino'] = destino_field.value
        viagem_data['valor'] = valor_field.value
        viagem_data['animais'] = animais_field.value

        #CHECK DADOS SALVOS
        print("Dados da viagem salvos:", viagem_data)

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
                ft.Row(controls=[comprador_field]),

                # TEXTFIELD DATA
                ft.Text(value= "Data"),
                ft.Row(controls=[data_field]),

                # TEXTFIELD ORIGEM
                ft.Text(value= "Origem"),
                ft.Row(controls=[origem_field]),

                # TEXTFIELD DESTINO
                ft.Text(value= "Destino"),
                ft.Row(controls=[destino_field]),

                # TEXTFIELD VALOR
                ft.Text(value= "Valor"),
                ft.Row(controls=[valor_field]),

                # TEXTFIELD QUANTIDADE DE ANIMAIS
                ft.Text(value= "Número de animais"),
                ft.Row(controls=[animais_field]),

                # BOTAO ADICIONAR
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.FilledButton(
                            icon="save", 
                            text="Salvar", 
                            on_click=save_data,
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
                ),
            ],
        ),
    )
    page.update()
