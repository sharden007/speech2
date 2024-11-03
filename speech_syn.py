import pyttsx3

class SpeechSynthesizer:
    def __init__(self, voice_type='male', rate=150, volume=1.0):
        """
        Initializes the SpeechSynthesizer with default settings.
        
        :param voice_type: 'male' or 'female' to specify the voice gender
        :param rate: Speech rate (words per minute)
        :param volume: Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 engine
        
        # Set voice type
        self.set_voice(voice_type)
        
        # Set speech rate
        self.set_rate(rate)
        
        # Set volume
        self.set_volume(volume)

    def set_voice(self, voice_type):
        """
        Set the voice type to either male or female.

        :param voice_type: 'male' or 'female'
        """
        voices = self.engine.getProperty('voices')
        
        # Male is usually the first voice, female the second on Windows
        if voice_type.lower() == 'female':
            self.engine.setProperty('voice', voices[1].id)
        else:
            # Default to male if not specified or any other input
            self.engine.setProperty('voice', voices[0].id)
    
    def set_rate(self, rate):
        """
        Set the speech rate.

        :param rate: Integer indicating words per minute
        """
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """
        Set the volume of the speech.

        :param volume: Float between 0.0 and 1.0
        """
        self.engine.setProperty('volume', volume)

    def speak(self, text):
        """
        Convert the given text to speech.

        :param text: The text to be spoken
        """
        self.engine.say(text)
        self.engine.runAndWait()

# Example module usage
if __name__ == "__main__":
    # Example: Create a speech synthesizer object with a female voice, slower rate, and lower volume
    synthesizer = SpeechSynthesizer(voice_type='female', rate=120, volume=0.8)
    
    # Speak some example phrases
    synthesizer.speak("Processing started.")
    synthesizer.speak("Processing complete.")