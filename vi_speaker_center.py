import os
import numpy as np

single_id_path = "speaker_embedding"
center_id_path = "speaker_embedding_center"

os.makedirs(f"./{center_id_path}")

for speaker in os.listdir(single_id_path):
    if os.path.isdir(f"./{single_id_path}/{speaker}"):
        print(f"---->{speaker}<----")
        subfile_num = 0
        speaker_cen = 0
        for file in os.listdir(f"./{single_id_path}/{speaker}"):
            if file.endswith(".npy"):
                source_embed = np.load(f"./{single_id_path}/{speaker}/{file}")
                source_embed = source_embed.astype(np.float32)
                speaker_cen = speaker_cen + source_embed
                subfile_num = subfile_num + 1
        speaker_cen = speaker_cen / subfile_num
        np.save(f"./{center_id_path}/{speaker}.npy", speaker_cen, allow_pickle=False)
