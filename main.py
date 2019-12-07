import yaml
from benedict.dicts import benedict as bdict
import gi; gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


with open(r'/run/media/robert/Data/Projects/Python/Dictionary/data.yml') as file:
    words = bdict(yaml.load(file, Loader=yaml.FullLoader))


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Translator")
        self.set_size_request(400, 60)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        hbox = Gtk.Box(spacing=6)
        hbox.set_homogeneous(False)

        label = Gtk.Label("")
        hbox.pack_start(label, True, True, 0)

        global entry
        entry = Gtk.Entry()
        hbox.pack_start(entry, True, True, 0)

        vbox.pack_start(hbox, True, True, 0)
        hbox1 = Gtk.Box(spacing=6)
        vbox.pack_start(hbox1, True, True, 0)

        button = Gtk.Button.new_with_label("Translate")
        button.connect("clicked", self.on_translate_clicked)
        hbox1.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Type")
        button.connect("clicked", self.on_type_clicked)
        hbox1.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Gender")
        button.connect('clicked', self.on_gender_clicked)
        hbox1.pack_start(button, True, True, 0)

        self.result = Gtk.Label()
        vbox.pack_start(self.result, True, True, 0,)

    def on_translate_clicked(self, button):
        key = entry.get_text().lower()
        temp = words.get([[key], 'translation'])
        self.result.set_text(temp)

    def on_type_clicked(self, button):
        key = entry.get_text().lower()
        temp = words.get([[key], 'type'])
        self.result.set_text(temp)

    def on_gender_clicked(self, button):
        key = entry.get_text().lower()
        temp = words.get([[key], 'gender'])
        self.result.set_text(temp)

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()