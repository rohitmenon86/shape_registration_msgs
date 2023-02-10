#!/usr/bin/env python

import sys
import rospy
from shape_registration_msgs.srv import PredictShape, PredictShapeRequest
from sensor_msgs.msg import PointCloud2 


class PredictShapeClient:

    def __init__(self):

        self.sub_point_cloud = rospy.Subscriber("cloud_pcd", PointCloud2, self.point_cloud_callback)
        self.pub_pred_point_cloud = rospy.Publisher("pred_cloud", PointCloud2, queue_size=10)
    

    def point_cloud_callback(self, data):

        

        req = PredictShapeRequest()
        req.observed_point_cloud = data

        var = 'a'

        print(" Recd command to process")
        try:
            rospy.wait_for_service('predict_shape')
            self.predict_shape_client = rospy.ServiceProxy('predict_shape', PredictShape)
            res = self.predict_shape_client(req)
            print(res.result_text)
            print(res.rigid_local_transform)
            #res.predicted_point_cloud.header.
            self.pub_pred_point_cloud.publish(res.predicted_point_cloud)

        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)


if __name__ == "__main__":

    rospy.init_node('client')
    try:
        client = PredictShapeClient()
    except rospy.Exception as e:
        print("Client init failed: %s"%e)

    print("Client init")
    rospy.spin()    