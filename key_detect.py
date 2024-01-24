from pynput.keyboard import Key, Listener

positions = {'1': 'sup',  # сап
             '2': 'adc',  # адк
             '3': 'jungle',  # лес
             '4': 'mid',  # мид
             '5': 'top'
             }  # топ

combs = []


def on_press(key):
    if len(combs) == 0:
        print('{0} pressed'.format(
            key))
        combs.append(key)
    elif len(combs) == 1:
        print('{0} pressed'.format(
            key))
        combs.append(key)
        return False


def on_release(key):
    if key == Key.esc:
        combs.clear()
        return False


def need_combination() -> list[str]:
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    return [positions[str(combs[0]).replace("'", "")], combs[1]]

