from slimua.gui import Gtk
from pprint import pprint

class MailboxTreeView:
    def __init__(self, master, treestore):
        self.master = master
        self.treestore = treestore

        self.tree_view = Gtk.TreeView(self.treestore.get_store())
        for i, column_title in enumerate(["mailbox"]):
            self.tree_view.append_column(Gtk.TreeViewColumn(column_title, Gtk.CellRendererText(), text=i))

        self.tree_view.connect("row-activated", self.on_activated)
        self.tree_view.connect("row-collapsed", self.on_row_collapsed)
        self.tree_view.connect("row-expanded",  self.on_row_expanded)
        self.tree_view.set_rules_hint(True)

        self.selection = self.tree_view.get_selection()
        self.selection.connect('changed', self.on_selection_changed)
#        self.selection.set_mode(Gtk.SELECTION_SINGLE)

    def on_selection_changed(self, selection):
        print "on_selection_changed"
        tree_model, tree_iter = selection.get_selected()
        pprint(tree_model)
        pprint(tree_iter)
        print(tree_model.get_value(tree_iter, 0))
        (model, pathlist) = tree_selection.get_selected_rows()
        pprint(pathlist)

    def on_activated(self, widget, row, col):
        print("on_activated")
        model = widget.get_model()
        text = model[row][0]
        pprint(model)

    def on_row_collapsed(self, widget, row, col):
        print("on_row_collapsed")
        model = widget.get_model()
        text = model[row][0]
        pprint(model)

    def on_row_expanded(self, widget, row, col):
        print("on_row_expanded")
        model = widget.get_model()
        text = model[row][0]
        pprint(model)

    def get_widget(self):
        return self.tree_view
