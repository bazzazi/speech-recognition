###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #



# Auto post Bot for instagram
# Developer: Mohammad Ali Bazzazi (me)
# by only drag and drop, post an image or video in your inta account Easily
# Don't forget to follow me
# enjoy  :)

########################### START ###########################

from os import system

# installing requirements
# Note: connect to internet
system("pip install speechrecognition")
system("pip install pipwin")
system("pipwin install pyaudio")


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("\n########################")
    print("speak anything...")
    r.adjust_for_ambient_noise(source)
    voice = r.listen(source)
    try:
        text = r.recognize_google(voice)
        print(f"you said => {text}")
    except:
        print("ops! something went wrong!")
    print("########################")
########################### END ###########################
