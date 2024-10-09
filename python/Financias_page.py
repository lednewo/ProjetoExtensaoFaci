import flet as ft

def financias(page: ft.Page):
    page.title = "Tela 2"
    page.views.clear()
    page.views.append(
        ft.View(
            "/financias",
            [
                #TOP TITLE
                ft.Row(
                controls=[
                    ft.Text("Financias", 
                            style= "headlineMedium",
                            weight= ft.FontWeight.BOLD)
                ],
                alignment= ft.MainAxisAlignment.CENTER),

                #DIVIDER
                ft.Divider(),

                #BUTTOMBAR
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
