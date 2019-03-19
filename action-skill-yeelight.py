from yeelight import Bulb
try:
  bulb = Bulb("192.168.0.108")
except:
  print("Could not connect to bulb")

request = intentMessage.slots.onOff.first().value

if bulb:
  if request == "an":
    bulb.turn_on()
  if request == "aus":
    bulb.turn_off()
  msg = "Okay. Schalte Licht " + request + "."
else:
  msg = "Konnte mich nicht mit der Lampe verbinden."

current_session_id = intentMessage.session_id
hermes.publish_end_session(current_session_id, text=msg)