from speech_syn import SpeechSynthesizer  # Assume the class is saved in speech_synthesizer.py

def main():
    synthesizer = SpeechSynthesizer(voice_type='female', rate=140, volume=1.0)
    
    # Example usage in a processing function
    synthesizer.speak("Training has begun.")
    
    # Simulate some processing logic
    process_data()
    
    synthesizer.speak("Task has completed.")

def process_data():
    # Simulate a task
    import time
    time.sleep(2)

if __name__ == "__main__":
    main()