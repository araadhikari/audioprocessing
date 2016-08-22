import os
path = './'
for filename in os.listdir(path):
    if filename.endswith('.wav'):
	    print(filename)
	    prefix1, prefix2, num = filename[:-4].split('_')
	    num = num.zfill(3)
	    new_filename = prefix1 + "_" + prefix2 + "_" + num + "_conv.wav"
	    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
