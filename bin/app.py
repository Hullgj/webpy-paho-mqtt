import web
from web import form
import mqtt_comm
import json

resp = "Nothing yet"

web.config.debug = True

urls = (
    '/', 'Index',
    '/hello', 'Hello',
    '/welcome', 'Comms'
)

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('templates/', base="layout", globals={'urls': urls})

class Index(object):
    def GET(self):
        return render.index()

class Hello(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.hello(greeting = greeting)

class Comms(object):
    def GET(self):
        return render.welcome(mbed_data=resp)

    def POST(self):
        # client = mqtt_comm.get_data()
        form = web.input(mbed_data = "Click start to recieve data")
        mbed_data = json.loads(form.mbed_data)
        global resp
        resp = mbed_data['d']
        return render.welcome(mbed_data=resp)


if __name__ == "__main__":
    app.run()