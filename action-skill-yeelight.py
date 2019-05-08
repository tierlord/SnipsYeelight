#!/usr/bin/env python3

from hermes_python.hermes import Hermes
import yeelight

def callback(hermes, intent_message):
    intent = intent_message.intent.intent_name

    intent = intent[intent.index(':')+1:]
    msg = ""
    bulb = yeelight.Bulb("192.168.0.108")

    if intent == "AnAus":
        request = intent_message.slots.onOff.first().value

        try:
            if request == "an":
                bulb.turn_on()
            if request == "aus":
                bulb.turn_off()
            msg = "Okay. Schalte Licht " + request + "."
        except:
            msg = "Konnte mich nicht mit der Lampe verbinden."

    if intent == "LichtFarbe":
        request = intent_message.slots.farbe.first().value

        try:
            if request == "weiß":
                bulb.set_rgb(255, 255, 255)
            if request == "warmweiß":
                bulb.set_rgb(255, 240, 190)
            if request == "hellblau":
                bulb.set_rgb(20, 190, 255)
            if request == "blau":
                bulb.set_rgb(20, 30, 255)
            if request == "pink":
                bulb.set_rgb(255, 20, 240)
            if request == "grün":
                bulb.set_rgb(30, 255, 30)
            if request == "rot":
                bulb.set_rgb(255, 20, 20)
            msg = "Habe das Licht in " + request + " umgeschaltet."
        except:
            msg = "Es gab einen Fehler. Ist die Lampe an?"

    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, text=msg)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h \
            .subscribe_intent("tierlord:AnAus", callback) \
            .subscribe_intent("tierlord:LichtFarbe", callback) \
            .start()