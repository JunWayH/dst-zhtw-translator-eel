from trans_func import pofile_trans
from tkinter import Tk
from tkinter import filedialog
import eel


@eel.expose
def trans_from_py(fpath):
    obj = pofile_trans()
    obj.run(fpath)
    eel.sleep(0.5)
    eel.changeBtn()

@eel.expose
def choose_path():
    fp = filedialog.askopenfilename()
    return fp


root = Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
eel.init('web')
eel.start("view.html", size=(350,230), mode='chrome')    

