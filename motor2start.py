import grove_i2c_motor_driver as motor
import time
m = motor.motor_driver()

print("Starting Motor 2")
m.MotorSpeedSetAB(0,100)
m.MotorDirectionSet(0b1010) ##0b0101 for reverse




