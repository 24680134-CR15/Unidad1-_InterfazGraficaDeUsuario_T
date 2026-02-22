import flet as ft
import re

def main(page: ft.Page):

    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Color principal definido en tu código original
    COLOR_BASE = "#4D2A32"

    # ---------- FUNCIONES VALIDACIÓN EN TIEMPO REAL (SIN CAMBIOS) ----------

    def validar_nombre(e):
        valor = txt_nombre.value
        if not valor:
            txt_nombre.error_text = None
        elif not valor.replace(" ", "").isalpha():
            txt_nombre.error_text = "Solo se permiten letras"
        else:
            txt_nombre.error_text = None
        txt_nombre.update()

    def validar_control(e):
        valor = txt_control.value
        if not valor:
            txt_control.error_text = None
        elif not valor.isdigit():
            txt_control.error_text = "Solo se permiten números"
        else:
            txt_control.error_text = None
        txt_control.update()

    def validar_email(e):
        valor = txt_email.value
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not valor:
            txt_email.error_text = None
        elif not re.match(patron, valor):
            txt_email.error_text = "Email no válido"
        else:
            txt_email.error_text = None
        txt_email.update()

    # ---------- CAMPOS (SOLO CAMBIO DE APARIENCIA) ----------

    txt_nombre = ft.TextField(
        label="Nombre",
        border_color=COLOR_BASE,
        focused_border_color=COLOR_BASE,
        border_radius=10,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        expand=True,
        on_change=validar_nombre
    )

    txt_control = ft.TextField(
        label="Numero de control",
        border_color=COLOR_BASE,
        focused_border_color=COLOR_BASE,
        border_radius=10,
        prefix_icon=ft.Icons.CO_PRESENT,
        expand=True,
        on_change=validar_control
    )

    txt_email = ft.TextField(
        label="Email",
        border_color=COLOR_BASE,
        focused_border_color=COLOR_BASE,
        border_radius=10,
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        on_change=validar_email
    )

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color=COLOR_BASE,
        border_radius=10,
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color=COLOR_BASE,
        border_radius=10,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    radio_genero = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Macho", label="Macho", fill_color=COLOR_BASE),
                ft.Radio(value="Hembra", label="Hembra", fill_color=COLOR_BASE),
                ft.Radio(value="Otro", label="Otro", fill_color=COLOR_BASE),
            ],
            spacing=20
        )
    )

    row_genero = ft.Column([
        ft.Text("Género:", weight=ft.FontWeight.BOLD, color=COLOR_BASE),
        radio_genero
    ])

    # ---------- VALIDACIÓN GENERAL (SIN CAMBIOS) ----------

    def validar_general():
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return (
            txt_nombre.value
            and txt_nombre.value.replace(" ", "").isalpha()
            and txt_control.value
            and txt_control.value.isdigit()
            and txt_email.value
            and re.match(patron, txt_email.value)
            and dd_carrera.value
            and dd_semestre.value
            and radio_genero.value
        )

    def cerrar_dialogo(dialogo):
        dialogo.open = False
        page.update()

    def enviar(e):
        if not validar_general():
            return

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Información Registrada", weight="bold"),
            content=ft.Column(
                [
                    ft.Text(f"Nombre: {txt_nombre.value}"),
                    ft.Text(f"No. Control: {txt_control.value}"),
                    ft.Text(f"Email: {txt_email.value}"),
                    ft.Text(f"Carrera: {dd_carrera.value}"),
                    ft.Text(f"Semestre: {dd_semestre.value}"),
                    ft.Text(f"Género: {radio_genero.value}")
                ],
                tight=True,
            ),
            actions=[
                ft.TextButton(
                    "Cerrar",
                    on_click=lambda e: cerrar_dialogo(dialogo)
                )
            ],
        )

        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()

    # Botón con estilo mejorado
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", size=16, weight="bold"),
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=COLOR_BASE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click=enviar,
        width=page.width
    )

    page.add(
        ft.Column(
            [
                ft.Text("Registro de Estudiante", size=24, weight="bold", color=COLOR_BASE),
                txt_nombre,
                txt_control,
                txt_email,
                ft.Row([dd_carrera, dd_semestre], spacing=10),
                ft.Container(content=row_genero, padding=ft.padding.only(top=10, bottom=10)),
                btn_enviar
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.run(main)