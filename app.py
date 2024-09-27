# função biblioteca gáfica
import flet as ft 

# função principal
def main(page: ft.Page):
    # ação do evento on_change
    def acao(e):
        result.value = texto.value
        page.update()
    # configuração da janela
    page.title = "Meu flet App"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # declaração de variáveis
    texto = ft.TextField(label="Digite aqui o seu texto", on_change=acao)
    result = ft.Text(size=30)

    # conteúdo da janela
    page.add(
        texto,
        result
    )

    # atualização do app 
    page.update()

# executa a aplicação
ft.app(main)