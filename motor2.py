import grove_i2c_motor_driver as motor
import time
m = motor.motor_driver()

print("Starting Motor 1")
m.MotorSpeedSetAB(0,100)
m.MotorDirectionSet(0b1010)
time.sleep(10)

print("Stopping Motor 1")
m.MotorSpeedSetAB(0,0)

print("Starting Motor 2")
m.MotorSpeedSetAB(100,0)
m.MotorDirectionSet(0b1010)
time.sleep(10)

print("Stopping Motor 2")
m.MotorSpeedSetAB(0,0)



