import justpy as jp
from webapp import layout
from webapp import page

class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gradient-to-b from-blue-100 to-blue-300 h-screen p-8")

        # Welcome title
        jp.Div(a=div, text="Welcome to the Instant Dictionary App!",
               classes="text-5xl font-extrabold text-gray-800 mb-6 text-center")

        # Subtitle
        jp.Div(a=div, text=(
            "Discover word definitions, synonyms, and more with ease."
        ), classes="text-2xl italic text-gray-700 mb-6 text-center")

        # Description paragraph
        jp.Div(a=div, text=(
            "Our dictionary app is designed for speed and simplicity, offering you an intuitive way to look up words "
            "from any device. Whether you're on your phone, tablet, or desktop, we're here to make learning effortless!"
        ), classes="text-lg text-gray-800 mb-4 leading-relaxed max-w-3xl mx-auto")

        # Navigation prompt
        jp.Div(a=div, text=(
            "Use the navigation menu above to start exploring the dictionary or to learn more about the app."
        ), classes="text-lg text-gray-800 leading-relaxed max-w-3xl mx-auto")
        return wp

