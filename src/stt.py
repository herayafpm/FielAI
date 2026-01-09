import whisper
import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile
import os

class SpeechToText:
    def __init__(self, model_size="base"):
        """
        Initialize Speech-to-Text with Whisper model.
        
        Args:
            model_size: Size of Whisper model (tiny, base, small, medium, large)
        """
        print(f"Loading Whisper model: {model_size}...")
        self.model = whisper.load_model(model_size)
        print("✓ Whisper model loaded successfully")
        
    def record_audio(self, duration=5, samplerate=16000):
        """
        Record audio from microphone.
        
        Args:
            duration: Recording duration in seconds
            samplerate: Sample rate for recording
            
        Returns:
            tuple: (audio_data, samplerate)
        """
        print(f"🎤 Recording for {duration} seconds...")
        audio = sd.rec(
            int(duration * samplerate), 
            samplerate=samplerate, 
            channels=1, 
            dtype='float32'
        )
        sd.wait()
        print("✓ Recording finished!")
        return audio, samplerate
    
    def transcribe(self, audio, samplerate):
        """
        Convert audio to text using Whisper.
        
        Args:
            audio: Audio data
            samplerate: Sample rate of audio
            
        Returns:
            str: Transcribed text
        """
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            temp_filename = f.name
            sf.write(temp_filename, audio, samplerate)
            
            try:
                result = self.model.transcribe(temp_filename, language="id")
                text = result["text"].strip()
            finally:
                # Clean up temp file
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
                    
        return text
    
    def listen(self, duration=5):
        """
        Record audio and transcribe to text.
        
        Args:
            duration: Recording duration in seconds
            
        Returns:
            str: Transcribed text
        """
        audio, sr = self.record_audio(duration)
        text = self.transcribe(audio, sr)
        return text

if __name__ == "__main__":
    # Test STT
    print("Testing Speech-to-Text...")
    stt = SpeechToText(model_size="base")
    
    print("\nSpeak now...")
    text = stt.listen(duration=5)
    print(f"\nTranscribed: {text}")
