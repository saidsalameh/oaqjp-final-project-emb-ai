import unittest
from EmotionDetection import emotion_detector

class TestJoy(unittest.TestCase): 
    def testJoy(self):
        self.assertEquals(emotion_detector("I am glad this happened"),"I am glad this happened")



if __name__ == '__main__':
    unittest.main()
