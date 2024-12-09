import whisper
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # Not a fan, but needed to get whisper to work on my laptop

source_folder = "audio_source"

for (folders, labels, files) in os.walk(source_folder):
    for file in files:
        if "mp3" in file:
            full_path = f"{source_folder}/{file}"
            file_id = file.split(".")[0]
            print(f"Now transcribing {file}")

            model = whisper.load_model("base")
            result = model.transcribe(full_path)
            print(result["text"])

            with open(f"{source_folder}/{file_id}.txt", "w") as text_output:
                text_output.write(result["text"])

