import flet as ft

# Criando o widget personalizado
class CartaoInformacoes(ft.UserControl):
    def __init__(self, comprador, origem, destino, data, num_animais):
        super().__init__()
        self.comprador = comprador
        self.origem = origem
        self.destino = destino
        self.data = data
        self.num_animais = num_animais

    def build(self):
        return ft.Card(
            width= 350,
            content=ft.Container(
                padding=ft.padding.all(15),
                content=ft.Row(
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        # COLUMN ESQUERDA
                        ft.Column(
                        controls=[
                            # COMPRADOR
                            ft.Text("Comprador:\n", size= 10, 
                                    spans=[
                                        ft.TextSpan(
                                        "Wendel",
                                        ft.TextStyle(
                                            weight= ft.FontWeight.BOLD, 
                                            size=14,
                                            color= ft.colors.AMBER_800
                                        ),
                                    ),  
                                ]
                            ),

                            # ORIGEM
                            ft.Text("Origem:\n", size= 10, 
                                    spans=[
                                        ft.TextSpan(
                                        "Fazenda",
                                        ft.TextStyle(
                                            weight= ft.FontWeight.BOLD, 
                                            size=14,
                                            color= ft.colors.AMBER_800
                                        ),
                                    ),  
                                ]
                            ),

                            # ORIGEM
                            ft.Text("Valor:\n", size= 10, 
                                    spans=[
                                        ft.TextSpan(
                                        "R$ 1400",
                                        ft.TextStyle(
                                            weight= ft.FontWeight.BOLD, 
                                            size=14,
                                            color= ft.colors.AMBER_800
                                        ),
                                    ),  
                                ]
                            ),
                        ]
                    ),
                    # COLUMN DIREITA
                    ft.Column(
                        controls=[
                            # COMPRADOR
                            ft.Text("Data:\n", size= 10, 
                                    spans=[
                                        ft.TextSpan(
                                        "20/05/2024",
                                        ft.TextStyle(
                                            weight= ft.FontWeight.BOLD, 
                                            size=14,
                                            color= ft.colors.AMBER_800
                                        ),
                                    ),  
                                ]
                            ),

                            # ORIGEM
                            ft.Text("Destino:\n", size= 10, 
                                    spans=[
                                        ft.TextSpan(
                                        "Fazenda",
                                        ft.TextStyle(
                                            weight= ft.FontWeight.BOLD, 
                                            size=14,
                                            color= ft.colors.AMBER_800
                                        ),
                                    ),  
                                ]
                            ),

                            # ORIGEM
                            ft.Text("N0 de animais:\n", size= 10, 
                                    spans=[
                                        ft.TextSpan(
                                        "24",
                                        ft.TextStyle(
                                            weight= ft.FontWeight.BOLD, 
                                            size=14,
                                            color= ft.colors.AMBER_800
                                        ),
                                    ),  
                                ]
                            ),
                        ]
                    ),
                ],), # FINAL ROW
            ),
            elevation=4,
        ),