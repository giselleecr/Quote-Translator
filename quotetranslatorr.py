import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"


    quote_text = ft.Text(
        value="Get in loser, we're going shopping",
        size=30,
        color="white",
        text_align="center"
    )

    translations = {
        "English": "Get in loser, we're going shopping",
        "Spanish": "Sube, perdedor, vamos de compras",
        "Portuguese": "Entra, perdedor, vamos fazer compras"
    }

    def change_language(e):
        selected = e.control.value
        quote_text.value = translations[selected]
        page.update()

    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="English", label="English"),
            ft.Radio(value="Spanish", label="Spanish"),
            ft.Radio(value="Portuguese", label="Portuguese"),
        ]),
        value="English",
        on_change=change_language
    )

    image = ft.Image(
        src="Assets/images/meangirlsimage.jpg",
        width=250,
        height=250
    )

    page.add(
        ft.Column(
            [
                ft.Text("Quote Translator", size=30, weight="bold"),
                image,
                quote_text,
                ft.Text("Choose a language:", size=17),
                radio_group,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=25
        )
    )

ft.run(main=main, assets_dir="assets")