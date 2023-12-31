def on_pin_pressed_p0():
    global Food, Money
    if Money > 0:
        Food += 1
        Money += -1
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_down():
    global health
    health = 0
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_pin_pressed_p1():
    global health, Food
    if health < 10 and health > 0:
        music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        health += 1
        Food += -1
        basic.show_icon(IconNames.SILLY)
        basic.pause(1000)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    global health
    health += -2
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Money = 0
health = 0
health = 10
Food = 5
Money = 8

def on_forever():
    global Money
    if health > 6:
        Money += 1
        basic.pause(10000)
basic.forever(on_forever)

def on_forever2():
    global health
    if health <= 10 and health > 6:
        health += -1
        basic.pause(10000)
    if health <= 6 and health > 3:
        health += -1
        basic.pause(5000)
    if health <= 3 and health > 0:
        health += -1
        basic.pause(2500)
basic.forever(on_forever2)

def on_forever3():
    if health > 6:
        basic.show_icon(IconNames.HAPPY)
    if health <= 6 and health > 3:
        basic.show_icon(IconNames.CONFUSED)
    if health <= 3 and health > 0:
        basic.show_icon(IconNames.SAD)
    if health <= 0:
        basic.show_icon(IconNames.SKULL)
        music._play_default_background(music.built_in_playable_melody(Melodies.FUNERAL),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever3)
