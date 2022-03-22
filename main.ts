function test () {
    counter += 1
    if (counter >= 5) {
        counter = 0
        NPNLCD.ShowString("INFRA: " + NPNBitKit.AnalogSound(AnalogPin.P1), 0, 0)
        NPNLCD.ShowString("SOUND: " + NPNBitKit.AnalogSound(AnalogPin.P2), 0, 1)
        serial.writeString("!3:INFRA:" + NPNBitKit.AnalogSound(AnalogPin.P1) + "#")
        serial.writeString("!4:SOUND:" + NPNBitKit.AnalogSound(AnalogPin.P2) + "#")
    }
}
serial.onDataReceived(serial.delimiters(Delimiters.Hash), function () {
    cmd = serial.readUntil(serial.delimiters(Delimiters.Hash))
    if (cmd == "0") {
        pins.digitalWritePin(DigitalPin.P4, 0)
        pins.digitalWritePin(DigitalPin.P5, 0)
    } else if (cmd == "1") {
        pins.digitalWritePin(DigitalPin.P4, 0)
        pins.digitalWritePin(DigitalPin.P5, 1)
    }
})
let cmd = ""
let counter = 0
led.enable(false)
NPNLCD.LcdInit()
counter = 0
pins.digitalWritePin(DigitalPin.P4, 0)
pins.digitalWritePin(DigitalPin.P5, 0)
basic.forever(function () {
    test()
    basic.pause(100)
})
