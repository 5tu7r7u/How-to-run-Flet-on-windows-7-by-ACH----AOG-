import flet as ft

def main(page: ft.Page):
    # إعداد الصفحة
    page.title = "مجتمع فليت مع راكوان"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"  # خلفية فاتحة جميلة

    # نص العنوان الرئيسي
    title_text = ft.Text(
        "مجتمع فليت مع راكوان",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#004aad",
        font_family="Arial",
        text_align=ft.TextAlign.CENTER,
    )

    # نص الوصف
    description_text = ft.Text(
        """
        مرحبًا بكم في مجتمع فليت مع راكوان! هنا نعمل معًا لبناء تطبيقات قوية ومتجاوبة باستخدام Python ومكتبة Flet.
        مجتمعنا يضم العديد من المطورين والمبرمجين المبدعين الذين يسعون دائمًا لمشاركة المعرفة والعمل على مشاريع مميزة.
        """,
        size=18,
        color="#333333",
        font_family="Verdana",
        text_align=ft.TextAlign.CENTER,
    )

    # إنشاء Container لتصميم النصوص بشكل أفضل
    content = ft.Container(
        content=ft.Column(
            [
                title_text,
                description_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding(20, 20, 20, 20),  # استخدام padding بقيم محددة
        #margin=ft.Margin.all(10),
        width=600,
        height=400,
        border_radius=15,
        bgcolor="#ffffff",  # لون خلفية النصوص
        #border=ft.Border.all(color="#004aad", width=2),  # إطار خارجي
        shadow=ft.BoxShadow(
            blur_radius=10, spread_radius=2, color="#cccccc", offset=ft.Offset(5, 5)
        ),  # تأثير الظل
    )

    # إضافة المحتوى إلى الصفحة
    page.add(content)

# تشغيل التطبيق
ft.app(target=main)
