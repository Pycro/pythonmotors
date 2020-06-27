import grove_i2c_motor_driver as motor
import time
m = motor.motor_driver()

print("Starting Motor 1")
m.MotorSpeedSetAB(100,0)
m.MotorDirectionSet(0b1010) ##0b0101 for reverse




