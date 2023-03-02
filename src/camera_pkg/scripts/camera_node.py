#!/usr/bin/env python

import rospy
import roslaunch

rospy.init_node('usb_cam_node')

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

cli_args = ['camera_pkg', 'usb_cam.launch']
launch = roslaunch.parent.ROSLaunchParent(uuid, cli_args)
launch.start()

rospy.spin()

launch.shutdown()
