import flet as ft

PRODUCTOS = [
    {
        "nombre": "Laptop Pro X1",
        "precio": 18999.00,
        "stock": 12,
        "categoria": "Electrónica",
        "descripcion": 'Laptop de alto rendimiento con procesador Intel i9, 32GB RAM, SSD 1TB y pantalla 4K de 15.6". Ideal para profesionales y creadores de contenido.',
        "imagen": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&h=250&fit=crop",
    },
    {
        "nombre": "Auriculares SoundMax",
        "precio": 2499.00,
        "stock": 35,
        "categoria": "Audio",
        "descripcion": "Auriculares inalámbricos con cancelación activa de ruido, batería de 40 horas y sonido envolvente Hi-Fi. Conectividad Bluetooth 5.3.",
        "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=250&fit=crop",
    },
    {
        "nombre": "Smartwatch Series 7",
        "precio": 4599.00,
        "stock": 20,
        "categoria": "Wearables",
        "descripcion": 'Reloj inteligente con monitor de salud 24/7, GPS integrado, resistencia al agua 50m y pantalla AMOLED de 1.9". Compatible con iOS y Android.',
        "imagen": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400&h=250&fit=crop",
    },
    {
        "nombre": "Cámara Mirrorless Z50",
        "precio": 22500.00,
        "stock": 8,
        "categoria": "Fotografía",
        "descripcion": "Cámara sin espejo de 24.5MP con video 4K 60fps, estabilización de imagen en 5 ejes, pantalla táctil abatible y dual SD.",
        "imagen": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400&h=250&fit=crop",
    },
    {
        "nombre": "Teclado Mecánico RGB",
        "precio": 1899.00,
        "stock": 50,
        "categoria": "Periféricos",
        "descripcion": "Teclado mecánico compacto 75% con switches Cherry MX Red, iluminación RGB por tecla, marco de aluminio y cable USB-C desmontable.",
        "imagen": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=400&h=250&fit=crop",
    },
]

COLORES = {
    "fondo": "#0F0F14",
    "tarjeta": "#1A1A24",
    "acento": "#6C63FF",
    "acento2": "#FF6584",
    "texto_principal": "#F0F0F5",
    "texto_secundario": "#9090A8",
    "precio": "#A78BFA",
    "stock_ok": "#34D399",
    "stock_bajo": "#F59E0B",
    "borde": "#2A2A3C",
    "panel": "#13131C",
}


def crear_badge(texto, color_fondo="#252535", color_texto="#9090A8"):
    return ft.Container(
        content=ft.Text(texto, size=11, weight=ft.FontWeight.W_600, color=color_texto),
        bgcolor=color_fondo,
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=10, vertical=4),
    )


def main(page: ft.Page):
    page.title = "TechStore — Ventas"
    page.bgcolor = COLORES["fondo"]
    page.padding = 0
    page.fonts = {
        "Montserrat": "https://fonts.gstatic.com/s/montserrat/v26/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Hw5aXo.woff2",
        "Roboto": "https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Me5Q.woff2",
    }
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK

    # ── Estado del carrito ──
    carrito = {}

    # ── Estado de favoritos ──
    favoritos = set()

    # ── Badge de cantidad en header ──
    badge_cantidad = ft.Text("0", color=ft.Colors.WHITE, size=11, weight=ft.FontWeight.W_700)
    badge_container = ft.Container(
        content=badge_cantidad,
        bgcolor=COLORES["acento2"],
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=6, vertical=2),
        visible=False,
    )

    # ── Controles del panel ──
    lista_carrito = ft.Column(spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)
    total_text = ft.Text(
        "$0.00", size=20, weight=ft.FontWeight.W_800,
        color=COLORES["precio"], font_family="Montserrat"
    )

    carrito_vacio_msg = ft.Container(
        padding=ft.padding.symmetric(vertical=40),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.SHOPPING_CART_OUTLINED, color=COLORES["texto_secundario"], size=48),
                ft.Text("Tu carrito está vacío", color=COLORES["texto_secundario"],
                        size=14, font_family="Roboto"),
            ],
        ),
    )

    def calcular_total():
        return sum(item["producto"]["precio"] * item["cantidad"] for item in carrito.values())

    def actualizar_panel_carrito():
        lista_carrito.controls.clear()
        if not carrito:
            lista_carrito.controls.append(carrito_vacio_msg)
        else:
            for nombre, item in list(carrito.items()):
                prod = item["producto"]
                cantidad = item["cantidad"]

                def hacer_restar(e, n=nombre):
                    carrito[n]["cantidad"] -= 1
                    if carrito[n]["cantidad"] <= 0:
                        del carrito[n]
                    actualizar_panel_carrito()
                    actualizar_badge()
                    page.update()

                def hacer_sumar(e, n=nombre):
                    carrito[n]["cantidad"] += 1
                    actualizar_panel_carrito()
                    actualizar_badge()
                    page.update()

                fila = ft.Container(
                    bgcolor="#1E1E2C",
                    border_radius=12,
                    padding=ft.padding.all(12),
                    border=ft.border.all(1, COLORES["borde"]),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Column(
                                spacing=2,
                                expand=True,
                                controls=[
                                    ft.Text(
                                        prod["nombre"], size=13, weight=ft.FontWeight.W_700,
                                        color=COLORES["texto_principal"], font_family="Montserrat",
                                        max_lines=1, overflow=ft.TextOverflow.ELLIPSIS,
                                    ),
                                    ft.Text(
                                        f"${prod['precio']:,.2f} c/u", size=11,
                                        color=COLORES["texto_secundario"], font_family="Roboto",
                                    ),
                                    ft.Text(
                                        f"Subtotal: ${prod['precio'] * cantidad:,.2f}", size=12,
                                        color=COLORES["precio"], font_family="Montserrat",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ],
                            ),
                            ft.Row(
                                spacing=2,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                                        icon_color=COLORES["acento2"],
                                        icon_size=20,
                                        on_click=hacer_restar,
                                    ),
                                    ft.Container(
                                        width=28, height=28,
                                        bgcolor=COLORES["acento"],
                                        border_radius=8,
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Text(
                                            str(cantidad), color=ft.Colors.WHITE,
                                            size=13, weight=ft.FontWeight.W_700,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                                        icon_color=COLORES["stock_ok"],
                                        icon_size=20,
                                        on_click=hacer_sumar,
                                    ),
                                ],
                            ),
                        ],
                    ),
                )
                lista_carrito.controls.append(fila)

        total_text.value = f"${calcular_total():,.2f}"
        lista_carrito.update()
        total_text.update()

    def actualizar_badge():
        total_items = sum(item["cantidad"] for item in carrito.values())
        badge_cantidad.value = str(total_items)
        badge_container.visible = total_items > 0
        badge_cantidad.update()
        badge_container.update()

    def abrir_carrito(e=None):
        actualizar_panel_carrito()
        panel_carrito.visible = True
        panel_carrito.update()

    def cerrar_carrito(e=None):
        panel_carrito.visible = False
        panel_carrito.update()

    def agregar_al_carrito(producto):
        nombre = producto["nombre"]
        if nombre in carrito:
            carrito[nombre]["cantidad"] += 1
        else:
            carrito[nombre] = {"producto": producto, "cantidad": 1}
        actualizar_badge()
        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                f"✓  {nombre} agregado al carrito",
                color=ft.Colors.WHITE, font_family="Roboto",
            ),
            bgcolor="#2A2A3C",
            duration=1500,
        )
        page.snack_bar.open = True
        page.update()

    # ────────────────────────────────────────────────
    #  PANEL LATERAL DEL CARRITO
    # ────────────────────────────────────────────────
    panel_carrito = ft.Container(
        width=380,
        bgcolor=COLORES["panel"],
        border=ft.border.only(left=ft.BorderSide(1, COLORES["borde"])),
        visible=False,
        content=ft.Column(
            spacing=0,
            controls=[
                # Header del panel
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=20, vertical=18),
                    border=ft.border.only(bottom=ft.BorderSide(1, COLORES["borde"])),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(spacing=10, controls=[
                                ft.Icon(ft.Icons.SHOPPING_CART, color=COLORES["acento"], size=22),
                                ft.Text(
                                    "Mi Carrito", size=18, weight=ft.FontWeight.W_800,
                                    color=COLORES["texto_principal"], font_family="Montserrat",
                                ),
                            ]),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_color=COLORES["texto_secundario"],
                                icon_size=20,
                                on_click=cerrar_carrito,
                            ),
                        ],
                    ),
                ),
                # Lista
                ft.Container(
                    expand=True,
                    padding=ft.padding.all(16),
                    content=lista_carrito,
                ),
                # Footer total + pago
                ft.Container(
                    padding=ft.padding.all(20),
                    border=ft.border.only(top=ft.BorderSide(1, COLORES["borde"])),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        "Total:", size=16, color=COLORES["texto_secundario"],
                                        font_family="Montserrat", weight=ft.FontWeight.W_600,
                                    ),
                                    total_text,
                                ],
                            ),
                            ft.ElevatedButton(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=8,
                                    controls=[
                                        ft.Icon(ft.Icons.PAYMENT, color=ft.Colors.WHITE, size=18),
                                        ft.Text(
                                            "Proceder al pago", color=ft.Colors.WHITE, size=14,
                                            font_family="Montserrat", weight=ft.FontWeight.W_600,
                                        ),
                                    ],
                                ),
                                style=ft.ButtonStyle(
                                    bgcolor=COLORES["acento"],
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    padding=ft.padding.symmetric(horizontal=20, vertical=14),
                                    elevation=0,
                                ),
                                expand=True,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    # ────────────────────────────────────────────────
    #  BOTÓN FAVORITO (con estado reactivo)
    # ────────────────────────────────────────────────
    def crear_boton_favorito(producto):
        nombre = producto["nombre"]
        en_fav = nombre in favoritos

        icono = ft.Icon(
            ft.Icons.FAVORITE if en_fav else ft.Icons.FAVORITE_BORDER,
            color="#FF6584" if en_fav else COLORES["texto_secundario"],
            size=18,
        )
        etiqueta = ft.Text(
            "En favoritos" if en_fav else "Añadir a favoritos",
            color="#FF6584" if en_fav else COLORES["texto_secundario"],
            size=14, font_family="Montserrat", weight=ft.FontWeight.W_600,
        )
        boton_ref = ft.Ref()

        def toggle_favorito(e, n=nombre, icono=icono, etiqueta=etiqueta):
            if n in favoritos:
                favoritos.discard(n)
                icono.name = ft.Icons.FAVORITE_BORDER
                icono.color = COLORES["texto_secundario"]
                etiqueta.value = "Añadir a favoritos"
                etiqueta.color = COLORES["texto_secundario"]
                msg = f"♡  {n} eliminado de favoritos"
            else:
                favoritos.add(n)
                icono.name = ft.Icons.FAVORITE
                icono.color = "#FF6584"
                etiqueta.value = "En favoritos"
                etiqueta.color = "#FF6584"
                msg = f"♥  {n} añadido a favoritos"
            icono.update()
            etiqueta.update()
            page.snack_bar = ft.SnackBar(
                content=ft.Text(msg, color=ft.Colors.WHITE, font_family="Roboto"),
                bgcolor="#2A2A3C",
                duration=1500,
            )
            page.snack_bar.open = True
            page.update()

        return ft.ElevatedButton(
            ref=boton_ref,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=8,
                controls=[icono, etiqueta],
            ),
            style=ft.ButtonStyle(
                bgcolor="#FF658422" if en_fav else "#1E1E2C",
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.padding.symmetric(horizontal=20, vertical=14),
                elevation=0,
                side=ft.BorderSide(1, "#FF658466" if en_fav else COLORES["borde"]),
                overlay_color=ft.Colors.with_opacity(0.05, "#FF6584"),
            ),
            expand=True,
            on_click=toggle_favorito,
        )

    # ────────────────────────────────────────────────
    #  TARJETA DE PRODUCTO
    # ────────────────────────────────────────────────
    def crear_tarjeta_producto(producto):
        stock_color = COLORES["stock_ok"] if producto["stock"] > 15 else COLORES["stock_bajo"]
        stock_label = (
            f"✓ {producto['stock']} en stock"
            if producto["stock"] > 15
            else f"⚠ Solo {producto['stock']} restantes"
        )
        return ft.Container(
            width=340,
            bgcolor=COLORES["tarjeta"],
            border_radius=16,
            border=ft.border.all(1, COLORES["borde"]),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=200,
                        content=ft.Stack(
                            controls=[
                                ft.Image(src=producto["imagen"], width=340, height=200, fit="cover"),
                                ft.Container(
                                    width=340, height=200,
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment(0, -1),
                                        end=ft.Alignment(0, 1),
                                        colors=["transparent", "#00000088"],
                                    ),
                                ),
                                ft.Container(
                                    top=12, left=12,
                                    content=crear_badge(
                                        producto["categoria"],
                                        color_fondo="#1A1A24CC",
                                        color_texto=COLORES["acento"],
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ft.Container(
                        padding=ft.padding.all(18),
                        content=ft.Column(
                            spacing=10,
                            controls=[
                                ft.Text(
                                    producto["nombre"], size=18, weight=ft.FontWeight.W_700,
                                    color=COLORES["texto_principal"], font_family="Montserrat",
                                ),
                                ft.Text(
                                    producto["descripcion"], size=13,
                                    color=COLORES["texto_secundario"],
                                    max_lines=3, overflow=ft.TextOverflow.ELLIPSIS,
                                    font_family="Roboto",
                                ),
                                ft.Divider(height=1, color=COLORES["borde"]),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Column(spacing=2, controls=[
                                            ft.Text(
                                                "PRECIO", size=10, color=COLORES["texto_secundario"],
                                                weight=ft.FontWeight.W_600, font_family="Montserrat",
                                            ),
                                            ft.Text(
                                                f"${producto['precio']:,.2f}", size=22,
                                                weight=ft.FontWeight.W_800, color=COLORES["precio"],
                                                font_family="Montserrat",
                                            ),
                                        ]),
                                        ft.Container(
                                            content=ft.Text(
                                                stock_label, size=11, color=stock_color,
                                                weight=ft.FontWeight.W_600,
                                            ),
                                            bgcolor=f"{stock_color}22",
                                            border_radius=20,
                                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    margin=ft.margin.only(top=4),
                                    content=ft.ElevatedButton(
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=8,
                                            controls=[
                                                ft.Icon(ft.Icons.SHOPPING_CART_OUTLINED,
                                                        color=ft.Colors.WHITE, size=18),
                                                ft.Text(
                                                    "Agregar al carrito", color=ft.Colors.WHITE,
                                                    size=14, font_family="Montserrat",
                                                    weight=ft.FontWeight.W_600,
                                                ),
                                            ],
                                        ),
                                        style=ft.ButtonStyle(
                                            bgcolor=COLORES["acento"],
                                            shape=ft.RoundedRectangleBorder(radius=10),
                                            padding=ft.padding.symmetric(horizontal=20, vertical=14),
                                            elevation=0,
                                            overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                                        ),
                                        expand=True,
                                        on_click=lambda e, p=producto: agregar_al_carrito(p),
                                    ),
                                ),
                                # ── Botón Favoritos ──
                                ft.Container(
                                    margin=ft.margin.only(top=2),
                                    content=crear_boton_favorito(producto),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

    # ────────────────────────────────────────────────
    #  HEADER
    # ────────────────────────────────────────────────
    header = ft.Container(
        padding=ft.padding.symmetric(horizontal=40, vertical=24),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#1A1A2E", "#0F0F14"],
        ),
        border=ft.border.only(bottom=ft.BorderSide(1, COLORES["borde"])),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(spacing=14, controls=[
                    ft.Container(
                        width=40, height=40, bgcolor=COLORES["acento"], border_radius=10,
                        content=ft.Icon(ft.Icons.BOLT, color=ft.Colors.WHITE, size=22),
                    ),
                    ft.Column(spacing=0, controls=[
                        ft.Text(
                            "TechStore", size=22, weight=ft.FontWeight.W_800,
                            color=COLORES["texto_principal"], font_family="Montserrat",
                        ),
                        ft.Text(
                            "Tecnología de vanguardia", size=12,
                            color=COLORES["texto_secundario"], font_family="Roboto",
                        ),
                    ]),
                ]),
                ft.GestureDetector(
                    on_tap=abrir_carrito,
                    content=ft.Container(
                        content=ft.Row(
                            spacing=8,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Stack(
                                    width=26, height=26,
                                    controls=[
                                        ft.Icon(ft.Icons.SHOPPING_BAG_OUTLINED,
                                                color=ft.Colors.WHITE, size=22),
                                        ft.Container(
                                            right=-2, top=-4,
                                            content=badge_container,
                                        ),
                                    ],
                                ),
                                ft.Text("Carrito", color=ft.Colors.WHITE,
                                        size=14, font_family="Montserrat"),
                            ],
                        ),
                        bgcolor=COLORES["acento"],
                        border_radius=10,
                        padding=ft.padding.symmetric(horizontal=16, vertical=10),
                    ),
                ),
            ],
        ),
    )

    # ────────────────────────────────────────────────
    #  LAYOUT PRINCIPAL
    # ────────────────────────────────────────────────
    subtitulo = ft.Container(
        padding=ft.padding.symmetric(horizontal=40, vertical=30),
        content=ft.Column(spacing=6, controls=[
            ft.Text(
                "Catálogo de Productos", size=28, weight=ft.FontWeight.W_800,
                color=COLORES["texto_principal"], font_family="Montserrat",
            ),
            ft.Text(
                f"{len(PRODUCTOS)} productos disponibles", size=14,
                color=COLORES["texto_secundario"], font_family="Roboto",
            ),
        ]),
    )

    tarjetas = [crear_tarjeta_producto(p) for p in PRODUCTOS]
    grid = ft.Container(
        padding=ft.padding.symmetric(horizontal=40, vertical=10),
        content=ft.ResponsiveRow(
            columns=12, spacing=24, run_spacing=24,
            controls=[
                ft.Column(col={"xs": 12, "sm": 6, "md": 4, "lg": 4}, controls=[t])
                for t in tarjetas
            ],
        ),
    )

    footer = ft.Container(
        margin=ft.margin.only(top=40),
        padding=ft.padding.all(20),
        border=ft.border.only(top=ft.BorderSide(1, COLORES["borde"])),
        content=ft.Text(
            "© 2025 TechStore — Todos los derechos reservados",
            size=12, color=COLORES["texto_secundario"],
            text_align=ft.TextAlign.CENTER, font_family="Roboto",
        ),
    )

    contenido = ft.Column(spacing=0, expand=True,
                          controls=[header, subtitulo, grid, footer])

    page.add(
        ft.Row(
            spacing=0,
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(content=contenido, expand=True),
                panel_carrito,
            ],
        )
    )


ft.app(target=main)