input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(counter)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.clearScreen()
})
let AC = 0
let counter = 0
counter = 0
basic.forever(function on_forever() {
    
    AC = input.acceleration(Dimension.Strength)
    if (AC > 1419) {
        counter += 1
        basic.pause(515)
    }
    
})
