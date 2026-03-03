import flet as ft
def main(page: ft.Page):
    page.title = "Formulario de Registro de Eventos"
    txt_nombre = ft.TextField(
        label="Nombre del evento",
        width=400
    )
    dropdown_tipo = ft.Dropdown(
        label="Tipo de evento",
        width=300,
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ]
    )
    radio_modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ])
    )
    check_inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?"
    )
    slider_duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )
    txt_resumen = ft.Text(
        value="Resumen",
        size=16
    )
    def mostrar_resumen(e):
        nombre = txt_nombre.value
        tipo = dropdown_tipo.value
        modalidad = radio_modalidad.value
        inscripcion = "Sí" if check_inscripcion.value else "No"
        duracion = slider_duracion.value
        resumen = f"""
        Nombre: {nombre}
        Tipo: {tipo}
        Modalidad: {modalidad}
        Requiere inscripción previa: {inscripcion}
        Duración estimada: {duracion} horas
        """
        txt_resumen.value = resumen
        page.update()
    btn_resumen = ft.ElevatedButton(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen
)
    page.add(
        ft.Text("Registro de Evento", size=24, weight="bold"),
        txt_nombre,
        dropdown_tipo,
        ft.Text("Modalidad:"),
        radio_modalidad,
        check_inscripcion,
        ft.Text("Duración estimada (horas):"),
        slider_duracion,
        btn_resumen,
        ft.Divider(),
        txt_resumen
    )
    

    page.add(ft.Text(
        value="Hola mundo",
        size=24,
        color=ft.Colors.PINK,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    ))

    page.add(ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        border_radius=ft.BorderRadius.all(10),
        repeat=ft.ImageRepeat.NO_REPEAT
    ))  
    page.add(ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400))
    page.add(ft.Row([
        ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400)
    ]))
    

ft.app(target=main)