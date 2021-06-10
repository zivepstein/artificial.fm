import numpy as np

def compute_adj_mat(df):
	out = []
	for i,r in df.iterrows():
	    row = []
	    for j,l in df.iterrows():
	        row.append(np.linalg.norm(r.values.astype(np.float) - l.values.astype(np.float)))
	    out.append(row)
	return out

def apply_fadeout(audio, sr, duration=3.0):
    # convert to audio indices (samples)
    length = int(duration*sr)
    end = audio.shape[0]
    start = end - length

    # compute fade out curve
    # linear fade
    fade_curve = np.linspace(1.0, 0.0, length)

    # apply the curve
    audio[start:end] = audio[start:end] * fade_curve