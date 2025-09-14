
# PI04048AA7L734606


import pyparrot.Minidrone as droneSDK
import cv2
from time import sleep


drone_MAC = "D0:3A:96:2E:E6:24" # fetch bluetooth address from linux budgie GUI
# drone = droneSDK.BLEConnection(address=drone_MAC,minidrone=droneSDK.Mambo()) # this connection type does not have safe_takeoff and safe_land commands (lower level I think for experiments only)
drone = droneSDK.Mambo(address=drone_MAC, use_wifi=False)
success = drone.connect(num_retries=3)
print("connected: %s" % success)

# wrap in a try except block to ensure that we land and disconnect if there is an error
try:
    if success:
        drone.safe_takeoff(5)
        # use the bottom camera to get a ground photo
        pic_success = drone.take_picture()
        print("picture taken: %s" % pic_success)
        if pic_success:
            # get the last picture taken
            frame = drone.groundcam.get_groundcam_picture(filename="mambo_ground.png",cv2_flag=True)
            if frame is not None:
                cv2.imshow("ground camera", frame)
                cv2.imwrite("mambo_ground.png", frame)
            else:
                print("frame is none")
        drone.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=3)
        drone.safe_land(5)
except Exception as e:
    print("Error occurred: %s" % e)
    drone.land() # try to land if there is an error

drone.disconnect()
print("disconnected: %s" % success)
cv2.waitKey(1000) # display for 1 second
cv2.destroyAllWindows()