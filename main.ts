input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    if (Money > 0) {
        Food += 1
        Money += -1
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    control.reset()
})
input.onGesture(Gesture.ScreenDown, function on_gesture_screen_down() {
    
    health = 0
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    if (health < 10 && health > 0) {
        music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        health += 1
        Food += -1
        basic.showIcon(IconNames.Silly)
        basic.pause(1000)
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    health += -2
})
let Money = 0
let health = 0
health = 10
let Food = 5
Money = 8
basic.forever(function on_forever() {
    
    if (health > 6) {
        Money += 1
        basic.pause(10000)
    }
    
})
basic.forever(function on_forever2() {
    
    if (health <= 10 && health > 6) {
        health += -1
        basic.pause(10000)
    }
    
    if (health <= 6 && health > 3) {
        health += -1
        basic.pause(5000)
    }
    
    if (health <= 3 && health > 0) {
        health += -1
        basic.pause(2500)
    }
    
})
basic.forever(function on_forever3() {
    if (health > 6) {
        basic.showIcon(IconNames.Happy)
    }
    
    if (health <= 6 && health > 3) {
        basic.showIcon(IconNames.Confused)
    }
    
    if (health <= 3 && health > 0) {
        basic.showIcon(IconNames.Sad)
    }
    
    if (health <= 0) {
        basic.showIcon(IconNames.Skull)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Funeral), music.PlaybackMode.UntilDone)
    }
    
})
