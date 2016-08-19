import os

#getting a list of all audio .csv file names
audios_dir= "C:\\Users\Aradhana\sox\WaveChunksFiles"
audio_csv_files=[]
for root, subdirs, files in os.walk(audios_dir):
    for file in files:
        if file.endswith('.csv'):
            # print(file)
            audio_csv_files.append(file)
print(audio_csv_files)

filename=audio_csv_files[0]

with open(audios_dir+"\\"+filename,"r") as csvfile:
    values=csvfile.readlines()
    for i in range(len(values)):
        values[i]=values[i].strip('\n')
    print(values)