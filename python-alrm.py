
from playsound import playsound
import winsound, time

number_of_seconds= int(input("Enter the number of seconds : "))

type_music=int(input("1.System Sound 2.Bella Ciao"))

time.sleep(number_of_seconds);

if type_music==1:
	for j in range(10):
		winsound.MessageBeep(-1);
		time.sleep(1)
else:
	playsound('audio.mp3')
