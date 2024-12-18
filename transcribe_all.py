import whisper
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # Not a fan, but needed to get whisper to work on my laptop
import torch
torch.cuda.empty_cache()


source_folder = "audio_source"
text_folder = "texts"

for (folders, labels, files) in os.walk(source_folder):
    for file in files:
        if "m4a" in file:
            full_path = f"{source_folder}/{file}"
            file_id = file.split(".")[0]
            print(f"Now transcribing {file}")

            if os.path.exists(f"{text_folder}/{file_id}.txt"):
                print(f"File {file} already transcribed, skipping...")
                continue

            model = whisper.load_model("large") # Change this to a better model if your setup allows
            result = model.transcribe(full_path, language="nl")
            print(result["text"])

            with open(f"{text_folder}/{file_id}.txt", "w") as text_output:
                text_output.write(result["text"])

