#!/usr/bin/env python
#上の宣言によってスクリプトがpythonとして読み込まれるようになる
import rospy
from opencv_apps.msg import RotatedRectStamped
from image_view2.msg import ImageMarker2
from geometry_msgs.msg import Point
#rospy:ROS Nodeを書くときに必ず必要、残りはメッセージの型を配信に再利用するため

def cb(msg):
    print msg.rect#ターミナルにmsgの情報を出力する
    marker = ImageMarker2()#変数markerがImageMarker2のかたであることを初期化
    marker.type = 0#markerのタイプは0であることを代入
    marker.position = Point(msg.rect.center.x, msg.rect.center.y, 0)#markerの位置はmsgのcenterに代入されたx,y座標である
    pub.publish(marker)#markerの情報を送信する

rospy.init_node('client')#rospyにノード名がclientであることを通知する。rospyがこの情報を得てはじめて、ROSのMasterと通信を始める。
rospy.Subscriber('/camshift/track_box', RotatedRectStamped, cb)#ROS Nodeであるcamshift/track_boxというトピックから RotatedRectStampedというメッセージのタイプで受信することを宣言、メッセージがトピックに到着するたびに、cbが行われる
pub = rospy.Publisher('/image_marker', ImageMarker2)#ROSのNodeであるimage_markerというトピックに ImageMarker2というメッセージのタイプで送っていることを宣言
rospy.spin()#自ノードを終了させないようにする
