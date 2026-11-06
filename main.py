from pydub import AudioSegment
import requests
import io
import time
import wave
import numpy as np
import deepspeech

stream_url = "http://19473.live.streamtheworld.com:80/CHSUFM_ADP_SC"
duration_seconds = 10  # Adjust this based on your needs

# Path to the DeepSpeech model
model_path = "/Users/joeygidda/Documents/Projects/RadioListener/deepspeech-0.9.3-models.pbmm"
scorer_path = "/Users/joeygidda/Documents/Projects/RadioListener/deepspeech-0.9.3-models.scorer"

model = deepspeech.Model(model_path)

while True:
    response = requests.get(stream_url, stream=True)
    audio_stream = io.BytesIO(response.content)

    # Assuming the stream is in AAC format
    audio = AudioSegment.from_file(audio_stream, format="aac")

    # Convert AudioSegment to a numpy array
    samples = np.array(audio.get_array_of_samples())

    # Create a WAV file in memory
    wav_file = io.BytesIO()
    with wave.open(wav_file, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(audio.frame_rate)
        wav.writeframes(samples.tobytes())

    # Reset the WAV file pointer to the beginning
    wav_file.seek(0)

    # Perform speech-to-text using DeepSpeech
    text = model.stt(wav_file.read().tobytes())

    # Print or use the transcribed text as needed
    print("Transcription:", text)

    time.sleep(duration_seconds)  # Adjust this to control the chunk size
