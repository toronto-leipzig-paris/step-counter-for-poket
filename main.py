def on_button_pressed_a():
    basic.show_number(counter)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

AC = 0
counter = 0
counter = 0

def on_forever():
    global AC, counter
    AC = input.acceleration(Dimension.STRENGTH)
    if AC > 1419:
        counter += 1
        basic.pause(515)
basic.forever(on_forever)
