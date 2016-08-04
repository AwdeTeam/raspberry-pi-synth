import RPi.GPIO as gpio
import time
#this is a comment

gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT)



Pitches = {
			"R":0.0,
			"C3":130.81,
			"C#3":138.59,
			"D3":146.83,
			"Eb3":155.56,
			"E3":164.81,
			"F3":174.61,
			"F#3":185.00,
			"G3":196.00,
			"Ab3":207.65,
			"A3":220.00,
			"Bb3":233.08,
			"B3":246.94,
			"C4":261.63,
			"C#4":277.18,
			"D4":293.66,
			"Eb4":311.13,
			"E4":329.63,
			"F4":349.23,
			"F#4":369.99,
			"G4":392.00,
			"Ab4":415.30,
			"A4":440.00,
			"Bb4":466.16,
			"B4":493.88,
			"C5":523.25
		}


print("I should be doing something")

class Note:
	pitch = 440
	duration = .25
	def __init__(self, pitch, duration = .25):
		self.pitch = Pitches[pitch]
		self.duration = duration

def playNote(note):
	frequency = note.pitch
	duration = note.duration
	duration *= 2

	if frequency == 0:
		time.sleep(duration)
		return
	
	frequency *= 2
	loops = int(frequency * duration)
	print("Frequency: " + str(frequency))
	print("sleep time is " + str(float(1.0 / frequency)))

	pinOn = False
	for i in range(0, loops):
		if pinOn == False:
			gpio.output(40, True)
			pinOn = True
		else:
			gpio.output(40, False)
			pinOn = False
		time.sleep(float(1.0 / frequency))

def playSong(notes):
	for note in notes:
		playNote(note)

# 329.64
# 261.63
# 196.00
#song = [Note(329.64),Note(329.64),Note(329.64),Note(261.63, .125),Note(329.64),Note(392, .5),Note(196, 1)]
#song = [Note("E3"),Note("E3"),Note("E3"),Note("C3",.125),Note("E3"),Note("G3",.5),Note("G4",1)]

#d3 (16) d3 (16) d4 (8) A4(dot8) A3b (16) 16rest G3 (8) F3 (8) D3 F3 G3
#a3 b3 Bb3
song = [Note("D3", .061),Note("D3", .061),Note("D4", .125),Note("A4", .186),Note("Ab3", .061),Note("R",.061), Note("G3", .125), Note("F3", .125), Note("D3", .061), Note("F3", .061), Note("G3", .061), Note("A3", .061),Note("A3", .061),Note("D4", .125),Note("A4", .186),Note("Ab3", .061),Note("R",.061), Note("G3", .125), Note("F3", .125), Note("D3", .061), Note("F3", .061), Note("G3", .061), Note("B3", .061),Note("B3", .061),Note("D4", .125),Note("A4", .186),Note("Ab3", .061),Note("R",.061), Note("G3", .125), Note("F3", .125), Note("D3", .061), Note("F3", .061), Note("G3", .061), Note("Bb3", .061),Note("Bb3", .061),Note("D4", .125),Note("A4", .186),Note("Ab3", .061),Note("R",.061), Note("G3", .125), Note("F3", .125), Note("D3", .061), Note("F3", .061), Note("G3", .061)] 


#for note in song:
	#note.pitch *= 2

playSong(song)

		
gpio.output(40, False)
print("I should be done doing something")
