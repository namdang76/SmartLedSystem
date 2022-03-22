def test():
    global counter
    counter += 1
    if counter >= 5:
        counter = 0
        NPNLCD.show_string("INFRA: " + str(NPNBitKit.analog_sound(AnalogPin.P1)), 0, 0)
        NPNLCD.show_string("SOUND: " + str(NPNBitKit.analog_sound(AnalogPin.P2)), 0, 1)
        serial.write_string("!3:INFRA:" + str(NPNBitKit.analog_sound(AnalogPin.P1)) + "#")
        serial.write_string("!4:SOUND:" + str(NPNBitKit.analog_sound(AnalogPin.P2)) + "#")

def on_data_received():
    global cmd
    cmd = serial.read_until(serial.delimiters(Delimiters.HASH))
    if cmd == "0":
        pins.digital_write_pin(DigitalPin.P4, 0)
        pins.digital_write_pin(DigitalPin.P5, 0)
    elif cmd == "1":
        pins.digital_write_pin(DigitalPin.P4, 0)
        pins.digital_write_pin(DigitalPin.P5, 1)
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

cmd = ""
counter = 0
led.enable(False)
NPNLCD.lcd_init()
counter = 0
pins.digital_write_pin(DigitalPin.P4, 0)
pins.digital_write_pin(DigitalPin.P5, 0)

def on_forever():
    test()
    basic.pause(100)
basic.forever(on_forever)
