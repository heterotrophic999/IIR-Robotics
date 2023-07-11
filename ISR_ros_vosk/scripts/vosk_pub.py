from vosk import Model, KaldiRecognizer
import pyaudio
from nltk.metrics.distance import edit_distance
from std_msgs.msg import UInt8
import rospy
import numpy as np

class Vosk_pub():

    def __init__(self) -> None:
        self.pub = rospy.Publisher('alice', UInt8, queue_size=10)

        self.model = Model(r"/home/wladimir/catkin_ws/src/ISR_ros_vosk/vosk_ru_small/vosk-model-small-ru-0.22")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1, 
            rate=16000,
            input=True, 
            frames_per_buffer=1000
        )

    @staticmethod
    def detect_commands(words):
        commands = ['', 'танцуй', 'молись', 'вперед', 'назад', 'стой', 'налево', 'направо']
        for i in range(len(commands)):
            for word in words:
                if edit_distance(commands[i], word, substitution_cost=3) <= 2:
                    return i
        return 0

    def inference(self):
        self.stream.start_stream()

        while not rospy.is_shutdown():
            data = self.stream.read(1000)
            if self.rec.AcceptWaveform(data):
                coms = self.rec.Result()[14:-3].split()
                if coms is not None:
                    res = self.detect_commands(coms)
                    print(res)
                    msg = 0
                    if res == 1: msg = 4  # dance
                    if res == 2: msg = 3  # ask
                    if res == 3: msg = 5  # walk forw
                    if res == 4: msg = 6  # walk backw
                    if res == 5: msg = 7  # stop 
                    if res == 6: msg = 2  # rotate left
                    if res == 7: msg = 1  # rotate left

                    self.pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('vosk_pub')
    node = Vosk_pub()
    node.inference()
