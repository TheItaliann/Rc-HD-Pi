from machine import Pin, PWM

servo_pin = 7

servo_pwm = PWM(Pin(servo_pin))

srv=100
                #angle
def servo_position(): #angle
        duty_cycle = int(((srv / 180) * 1000) + 500)
        servo_pwm.duty_u16(duty_cycle)
  

servo_position()