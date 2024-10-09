import flet as ft

class CartaoInformacoes(ft.UserControl):
    def __init__(self, comprador, origem, destino, data, num_animais, valor):
        super().__init__()
        self.comprador = comprador
        self.origem = origem
        self.destino = destino
        self.data = data
        self.num_animais = num_animais
        self.valor = valor

# widget personalizado
def build(self):
        return ft.Row(
            controls=[
                ft.Card(
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
                                                "{self.comprador}",
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
                                                "{self.origem}",
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
                                                "{self.valor}",
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
                                                "{self.data}",
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
                                                "{self.destino}",
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
                                                "{self.num_animais}",
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
            ]
        ),