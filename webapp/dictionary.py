import justpy as jp
import definition
from webapp import layout
from webapp import page

class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        # Main container
        div = jp.Div(a=container, classes="bg-gradient-to-b from-blue-100 to-blue-300 h-screen p-8")

        # Page title
        jp.Div(a=div, text="Instant English Dictionary",
               classes="text-5xl font-extrabold text-gray-800 mb-6 text-center")

        # Subtitle
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.",
               classes="text-2xl italic text-gray-700 mb-6 text-center")

        # Input and output containers
        input_div = jp.Div(a=div, classes="grid grid-cols-2 gap-4 max-w-3xl mx-auto")

        # Input box
        input_box = jp.Input(
            a=input_div,
            placeholder="Type in a word here...",
            classes=(
                "m-2 bg-gray-100 border-2 border-gray-200 rounded w-full "
                "focus:bg-white focus:outline-none focus:border-blue-500 py-2 px-4"
            ),
        )

        # Scrollable output box
        output_div = jp.Div(
            a=div,
            text="Your definition will appear here...",
            classes=(
                "m-2 p-4 text-lg border-2 border-blue-400 bg-white rounded overflow-y-auto "
                "transition-all duration-300"
            ),
            style="height: 12rem; max-height: 50vh;"  # Fixed height with a maximum of 50% viewport height
        )

        # Assign event handler
        input_box.output = output_div
        input_box.on("input", cls.get_definition)

        return wp

    # Event handler
    @staticmethod
    def get_definition(widget, msg):
        # Get the definition of the word
        defined = definition.Definition(widget.value).get()
        widget.output.text = " ".join(defined) if defined else "No definition found."
