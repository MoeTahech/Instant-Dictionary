import justpy as jp

class About:
    path  = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        div = jp.Div(a=div,text="This is about page!",  classes="text-4xl m-2")
        return wp
