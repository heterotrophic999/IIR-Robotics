import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt8
import pandas as pd
import pymongo

def get_responce(client):
    db = client.get_default_database()
    docs = pd.DataFrame(db.get_collection('logs').find())
    try:
        with db.watch(
                [{'$match': {'operationType': 'insert'}}]) as stream:
            for insert_change in stream:
                rospy.loginfo(insert_change)
    except pymongo.errors.PyMongoError:
    # The ChangeStream encountered an unrecoverable error or the
    # resume attempt failed to recreate the cursor.
       rospy.loginfo("error")
    return str
  

def talker():
    MONGODB_URI = ''
    client = pymongo.MongoClient(MONGODB_URI)  # тут должен быть ваш адрес mongo
    db = client.get_default_database()
    pub = rospy.Publisher('alice', UInt8, queue_size=10)
    rospy.init_node('alice_pub', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    rospy.loginfo("Подключение...")
    try:
        with db.watch(
                [{'$match': {'operationType': 'insert'}}]) as stream:
            for insert_change in stream:   
                rospy.loginfo("Получил данные")
                docs = pd.DataFrame(db.get_collection('logs').find())
                move = docs.move[-1:].iloc[0]
                rospy.loginfo(move)
                pub.publish(move)
    except pymongo.errors.PyMongoError:
# The ChangeStream encountered an unrecoverable error or the
# resume attempt failed to recreate the cursor.
        rospy.loginfo("error")

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
