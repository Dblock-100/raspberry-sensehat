#Parameter       Type     Valid values  #Explanation
#compass_enabled Boolean (TrueORFalse)  #Whether or not the compass should be enabled.
#gyro_enabled    Boolean (TrueORFalse)  #Whether or not the gyroscope should be enabled.
#accel_enabled   Boolean (TrueORFalse)  #Whether or not the accelerometer should be enabled.

#e.g. sense.set_imu_config(False, True, False)  # gyroscope only
################################################
from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(True, True, True)  #All three parameters = True/On