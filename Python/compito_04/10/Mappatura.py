from pynput import keyboard

def on_press(key):   #funzione che si attiva quando si preme un qualsiasi tasto della tastiera
    try:
        # Verifica se il tasto premuto è una lettera
        if key.char.isalpha():
            print(f'Tasto premuto: {key.char}')
    except AttributeError:
        # ingoro caratteri speciali come shit ctrl...
        pass

def start_listening(): 
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    print("Premi una lettera sulla tastiera")
    start_listening()