from flet import *
def main(note:Page):
    note.window.width=250
    note.window.height=490
    t=Text("simple")
    note.add(t)

    
    note.update()
app(main)
