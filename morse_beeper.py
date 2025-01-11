import winsound
from time import sleep
# import threading
# import pyaudio
alphabet={"A":[1,3],"B":[3,1,1,1],"C":[3,1,3,1],"D":[3,1,1],"E":[1],"F":[1,1,3,1],"G":[3,3,1],"H":[1,1,1,1],"I":[1,1],"J":[1,3,3,3],"K":[3,1,3],"L":[1,3,1,1],"M":[3,3],"N":[3,1],"O":[3,3,3],"P":[1,3,3,1],"Q":[3,3,1,3],"R":[1,3,1],"S":[1,1,1],"T":[3],"U":[1,1,3],"V":[1,1,1,3],"W":[1,3,3],"X":[3,1,1,3],"Y":[3,1,3,3],"Z":[3,3,1,1],"1":[1,3,3,3,3],"2":[1,1,3,3,3],"3":[1,1,1,3,3],"4":[1,1,1,1,3],"5":[1,1,1,1,1],"6":[3,1,1,1,1],"7":[3,3,1,1,1],"8":[3,3,3,1,1],"9":[3,3,3,3,1],"0":[3,3,3,3,3],".":[1,3,1,3,1,3],",":[3,3,1,1,3,3],"?":[1,1,3,3,1,1],"!":[1,1,1,1,1,1,1]}
speed=50

message="KI5KAL testing testing, working on my keyer."#input("Message> ")
for letter in message.upper():
    if letter==" ":
        sleep(speed*7/1000)
        print()
    else:
        morse=alphabet[letter]
        for time in morse:
            print("." if time==1 else "-",end="")
            winsound.Beep(641,int(speed*time))
            sleep(speed/1000)
        sleep(speed*3/1000)
        print("    ",end="")
test=[]
for i in alphabet.keys():
    test+=alphabet[i]+[-3]

# test=[[0,20],[1,1],[0,1],[1,3],[0,3],[1,3],[0,1],[1,1],[0,1],[1,1],[0,1],[1,1],[0,7]]#bit time


# word=""
# buffer=[]
# last=None
# dot=None
# for i in test:
#     if dot==None:
#         dot=i[0]
#     if len(buffer)
#     if i[0]==1:
#         buffer.append(i[1])
#     elif i[0]==0:
#         if i[1]==1:
#             pass
#         elif i[1]==3:
#             for k in alphabet.keys():
#                 if alphabet[k]==buffer:
#                     word+=k
#                     break
#             buffer=[]
#         elif i[1]==7:
#             for k in alphabet.keys():
#                 if alphabet[k]==buffer:
#                     word+=k
#                     break
#             print(word)
#             buffer=[]

    last=i








    # buffer.append(i)
    # if len(buffer)>1:
    #     if 2.9<buffer[-1][1]/buffer[-2][1]<3.1:
    #         buffer2.append(buffer[-2][1])
    #         if i[0]:
    #             buffer3.append(i)
    #     elif 0.2<buffer[-1][1]/buffer[-2][1]<0.4:
    #         buffer2.append(buffer[-1][1])
    #         if i[0]:
    #             buffer3.append(i)
    #     elif buffer[-2][1]/buffer[-1][1]>6.9:
    #         print([i/(sum(buffer2)/len(buffer2)) for i in buffer3])
    #     else:
    #         del buffer[-1]
        # print(buffer)
        # print(buffer2)
        # print(buffer3)
        
    # print(round(min(buffer)),round(max(buffer)))

    # letter.append(i)
    # if len(letter)>0:
    #     bits=[n[0] for n in letter]
    #     times=[n[1] for n in letter]
    #     mn=min(times)
    #     mx=max(times)
    #     # if len(letter)==1:
    #     #     dot=i[1]
    #     if 3.25>(mx/mn)>2.75:
    #         dot=mn
    #     if i[0]==0:
    #         if dot+.25>(i[1])>dot-.25:
    #             print("t",end="")
    #         elif dot+3.25>(i[1])>dot+.25:
    #             print("n",end="")
    #             for k in alphabet.keys():
    #                 if len(alphabet[k])==len(logic):
    #                     if logic==alphabet[k]:
    #                         print(k)
    #                         break
    #             letter=[]
    #             logic=[]
    #         # else:
    #         #     print("n",end="")
    #         #     for k in alphabet.keys():
    #         #         if len(alphabet[k])==len(logic):
    #         #             if logic==alphabet[k]:
    #         #                 print(k)
    #         #     letter=[]
    #         #     logic=[]
    #     elif i[0]==1:
    #         if dot+.25>(i[1])>dot-.25:
    #             print(".",end="")
    #             logic.append(1)
    #         elif dot+3.25>(i[1])>dot+.25:
    #             print("-",end="")
    #             logic.append(3)




# buffer=[]
# dot=None
# for i in test:
#     if i!=-3:
#         buffer.append(i)
#     if buffer==[]:
#         dot=i
#     else:
#         mn=min(buffer)
#         mx=max(buffer)
#         if 3.25>(mx/mn)>2.75:
#             dot=mn
#         if i==-3:
#             print("----")
#             for k in alphabet.keys():
#                 # print()
#                 if len(alphabet[k])==len(buffer) and [(alphabet[k][n]/buffer[n]) for n in range(len(buffer))]==[1 for n in range(len(buffer))]:
#                     # print([(alphabet[k][n]/buffer[n]) for n in range(len(buffer))],[1 for n in range(len(buffer))])
#                     print(k)
#                     # break
#             buffer=[]
#             dot=None
#     # print(dot)







# import pyaudio
# import wave

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()