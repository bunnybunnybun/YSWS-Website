import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk

css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.ExampleWeatherApp")
        GLib.set_application_name('ExampleApp')
    
    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="My First App")
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.button = Gtk.Button(label="Put whatever you want it to say!")
        self.label = Gtk.Label(label="Put whatever text you want here")
        self.main_box.append(self.label)
        self.main_box.append(self.button)
        window.set_child(self.main_box)
        window.present()

app = MyApplication()
app.run()