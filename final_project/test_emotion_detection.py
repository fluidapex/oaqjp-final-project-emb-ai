from EmotionDetection import emotion_detector

def test_emotion_detection():

    test_cases = [
        {
            'text': 'I am glad this happened',
            'expected': 'joy'
        },
        {
            'text': 'I am really mad about this',
            'expected': 'anger'
        },
        {
            'text': 'I feel disgusted just hearing about this',
            'expected': 'disgust'
        },
        {
            'text': 'I am so sad about this',
            'expected': 'sadness'
        },
        {
            'text': 'I am really afraid that this will happen',
            'expected': 'fear'
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        text = test_case['text']
        expected = test_case['expected']

        print(f"\nTest {i}: {expected.upper()} emotion")
        print(f"Input text: '{text}'")

        result = emotion_detector(text)

        print(f"Full result: {result}")
        print(f"Dominant emotion: {result['dominant_emotion']}")

if __name__ == '__main__':
    test_emotion_detection()
    print("Unit testing completed!")