import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt8
import pandas as pd
import pymongo

def get_responce():
  MONGODB_URI = 'mongodb+srv://mrdanhik:0321@loser.2mlzec4.mongodb.net/alice?retryWrites=true&w=majority'
  client = pymongo.MongoClient(MONGODB_URI)  # тут должен быть ваш адрес mongo
  db = client.get_default_database()
  docs = pd.DataFrame(db.get_collection('logs').find())
  str = docs.move[-1:].iloc[0]
  return str

def talker():
    pub = rospy.Publisher('alice', UInt8, queue_size=10)
    rospy.init_node('alice_pub', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo("Подключение...")
        move = get_responce()
        rospy.loginfo("Получил данные")
        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass