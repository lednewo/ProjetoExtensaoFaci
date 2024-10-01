# custom_ft.py
import flet as ft
from componets.card_informacoes import CartaoInformacoes

# Adicionando o widget personalizado ao namespace de ft
ft.CartaoInformacoes = CartaoInformacoes

# Exportando o namespace ft com o widget adicionado
__all__ = ['ft']