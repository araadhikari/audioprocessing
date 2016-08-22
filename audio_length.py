import os

import sys
#getting a list of all audio .csv file names
audios_dir= "C:\\Users\\Aradhana\\audioprocessing\\WaveChunksFiles"
audios_wav_folder_dir="C:\\Users\\Aradhana\\audioprocessing\\conv_org\\"
audios_wav_split_folder_dir="C:\\Users\\Aradhana\\audioprocessing\\conv_org_audio_split\\"
audio_csv_files=[]
for root, subdirs, files in os.walk(audios_dir):
    for file in files:
        if file.endswith('.csv'):
            audio_csv_files.append(file)

#splits audio file into smaller chuncks for each file
for filename in audio_csv_files:
    with open(audios_dir+"\\"+filename,"r") as csvfile:
        values=csvfile.readlines()
        for i in range(len(values)):
            values[i]=values[i].strip('\n')
        #values.append('')
        values.pop(0)
        values.insert(0,'0')
        #print(values)
        trim_string=""
        if len(values)>1: #atleast two value
            for i in range(len(values)-1):
                start=int(values[i])/1000
                end=int(values[i+1])/1000
                difference=end-start
                #print(difference)
                if i==0:
                    trim_string+=" trim 0 "+str(difference)+" channels 1 rate 16000"
                else:
                    trim_string+=" : newfile trim 0 "+str(difference)+" channels 1 rate 16000"

        string='sox '+audios_wav_folder_dir+filename[:-4]+'_birdseyeview_converted.wav '+audios_wav_split_folder_dir+filename[:-4]+'_'+'%1n'+".wav"+trim_string
        print(string)
        os.system(string)
