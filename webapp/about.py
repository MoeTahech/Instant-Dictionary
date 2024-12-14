import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gradient-to-r from-blue-100 "
                                          "to-blue-300 h-screen p-8")

        # Title with styling
        jp.Div(a=div, text="About Us", classes="text-5xl font-extrabold text-gray-800 mb-6 text-center")

        # Subtitle
        jp.Div(a=div, text=(
            "Learn more about the Instant Dictionary Web App!"
        ), classes="text-2xl italic text-gray-700 mb-6 text-center")

        # Description text
        jp.Div(a=div, text=(
            "Our Instant Dictionary App aims to provide a seamless experience for discovering word definitions, synonyms, "
            "and related information. Whether you're a student, writer, or simply curious about words, this app is here to help!"
        ), classes="text-lg text-gray-800 mb-4 leading-relaxed max-w-3xl mx-auto")

        # Additional paragraph
        jp.Div(a=div, text=(
            "We are dedicated to building a platform that's intuitive, responsive, and enjoyable to use. "
            "Thank you for choosing our app!"
        ), classes="text-lg text-gray-800 leading-relaxed max-w-3xl mx-auto")

        return wp
