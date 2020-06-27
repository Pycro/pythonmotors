import grove_i2c_motor_driver as motor
import time
m = motor.motor_driver()

print("Stopping Motor 1")
m.MotorSpeedSetAB(0,0)
m.MotorDirectionSet(0b1010) ##0b0101 for reverse




