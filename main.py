import pyautogui
import pytesseract
import keyboard as K
import pynput.keyboard as keyboard
import pynput.mouse as mouse
import json
import time

pytesseract.pytesseract.tesseract_cmd = r'YOUR_PATH\tesseract.exe'

langs = ['afr', 'amh', 'ara', 'asm', 'aze', 'aze_cyrl', 'bel', 'ben', 'bod', 'bos', 'bre', 'bul', 'cat', 'ceb', 'ces', 'chi_sim', 'chi_tra', 'chr', 'cos', 'cym', 'dan', 'deu', 'dzo', 'ell', 'eng', 'enm', 'epo', 'equ', 'est', 'eus', 'fao', 'fas', 'fil', 'fin', 'fra', 'frk', 'frm', 'fry', 'gla', 'gle', 'glg', 'grc', 'guj', 'hat', 'heb', 'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl', 'ita', 'ita_old', 'jav', 'jpn', 'kan', 'kat', 'kat_old', 'kaz', 'khm', 'kir', 'kmr', 'kor', 'kor_vert', 'lao', 'lat', 'lav', 'lit', 'ltz', 'mal', 'mar', 'mkd', 'mlt', 'mon', 'mri', 'msa', 'mya', 'nep', 'nld', 'nor', 'oci', 'ori', 'osd', 'pan', 'pol', 'por', 'pus', 'que', 'ron', 'rus', 'san', 'sin', 'slk', 'slv', 'snd', 'spa', 'spa_old', 'sqi', 'srp', 'srp_latn', 'sun', 'swa', 'swe', 'syr', 'tam', 'tat', 'tel', 'tgk', 'tha', 'tir', 'ton', 'tur', 'uig', 'ukr', 'urd', 'uzb', 'uzb_cyrl', 'vie', 'yid', 'yor']

def get_mouse_position():
    def on_click(x, y, button, pressed):
        if pressed and button == mouse.Button.left and keyboard.Key.ctrl_l in current_keys:
            nonlocal X, Y
            X, Y = x, y
            listener.stop()
            k_listener.stop()

    def on_press(key):
        if key == keyboard.Key.ctrl_l:
            current_keys.add(key)

    def on_release(key):
        try:
            current_keys.remove(key)
        except KeyError:
            pass

    current_keys = set()
    X, Y = None, None

    with mouse.Listener(on_click=on_click) as listener, keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener:
        listener.join()
        k_listener.join()

    return X, Y

ask = None

with open('config.json', 'r') as f:
    fdict = json.load(f)

if fdict["settings"] == "False":
    ask = True
elif fdict["settings"] == "True":
    useconfig = input(f"I found a saved configuration.\nLanguage: {fdict['lang']}\nMilliseconds: {fdict['ms']}\nDo you want to load it? (y/n/del): ")
    if useconfig.lower() == "y":
        lang = fdict['lang']
        ms = int(fdict['ms'])
        print("Configuration loaded successfully.\n")
        ask = False
    elif useconfig.lower() == "n":
        ask = True
    elif useconfig.lower() == "del":
        fdict['settings'] = "False"
        fdict['lang'] = ""
        fdict['ms'] = ""
        with open("config.json", "w") as f:
            json.dump(fdict, f)
        print("Configuration deleted.")
        ask = True

if ask:
    recolang = False
    okms = False

    while not recolang:
        lang = input("Select the language of the game: ").lower()
        if lang in langs:
            recolang = True
        else:
            print("Error: unrecognized language.\n")

    while not okms:
        ms = input("Enter the delay between each character (in milliseconds): ")
        if ms.isdigit():
            okms = True
        else:
            print("Error: invalid value entered.\n")

    if input("Do you want to save the configuration? (y/n): ").lower() == 'y':
        fdict['settings'] = "True"
        fdict['lang'] = lang
        fdict['ms'] = ms
        with open("config.json", "w") as f:
            json.dump(fdict, f)
    else:
        pass

ms = int(ms) / 1000

print("Now go to the first point, press 'Ctrl + click' to select the first corner")
x1, y1 = get_mouse_position()
print(f"Corner 1:\n  x: {x1}\n  y: {y1}")

print("Now go to the second point, press 'Ctrl + click' to select the second corner")
x2, y2 = get_mouse_position()
print(f"Corner 2:\n  x: {x2}\n  y: {y2}")

screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

text = str(pytesseract.image_to_string(screenshot, lang=lang)).replace("|", "I")
text = " ".join(text.splitlines())

print("Position the cursor, then press 'Enter' to start the bot")
K.wait('enter')

for char in text:
    pyautogui.write(char)
    time.sleep(ms)