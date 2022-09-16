# VI-Speaker
Speaker embedding for VI-SVC and VI-SVS, alse for VITS; Use this to replace the ID to implement voice clone.

# code from mozill_tts and Coqpit/TTS
https://github.com/mozilla/TTS/tree/master/TTS/speaker_encoder

pip install coqpit

# download model，or get it at **release**
https://github.com/mozilla/TTS/wiki/Released-Models

Speaker-Encoder by @mueller91	LibriTTS + VCTK + VoxCeleb + CommonVoice

# please read the config
https://drive.google.com/drive/folders/15oeBYf6Qn1edONkVLXe82MzdIi3O_9m3

# use
python vi_speaker_single.py ./saved_models/best_model.pth.tar ./saved_models/config.json -s TEST.wav -t TEST.npy

# batch use
python vi_speaker_batch.py ./saved_models/best_model.pth.tar ./saved_models/config.json ./data/waves ./speaker_embedding

data/
└── waves
    ├── spk1
    │   ├── 000002.wav
    │   ├── 000006.wav
    │   └── 000038.wav
    └── spk2
        ├── 000040.wav
        ├── 000044.wav
        └── 000077.wav

speaker_embedding/
├── spk1
│   ├── 000002.npy
│   ├── 000006.npy
│   └── 000038.npy
└── spk2
    ├── 000040.npy
    ├── 000044.npy
    └── 000077.npy

# compute speaker center
input path = speaker_embedding, output path = speaker_embedding_center

python vi_speaker_center.py

speaker_embedding_center/
├── spk1.npy
└── spk2.npy


# for VI-SVC
mv speaker_embedding_center data/spkid

data/
├── waves
│   ├── 10001
│   ├── 20400
│   │   ├── 20400_001.wav
│   │   ├── 20456_019.wav
│   │   
├── phone
│   ├── 10001
│   ├── 20400
│   │   ├── 20400_001.npy
│   │   ├── 20456_019.npy
│   │   
├── lable
│   ├── 10001
│   ├── 20400
│   │   ├── 20400_001.npy
│   │   ├── 20456_019.npy
│   │   
├── spkid
│   ├── 10001.npy
│   ├── 20400.npy
│   │   



