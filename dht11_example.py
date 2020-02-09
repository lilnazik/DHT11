import RPi.GPIO as GPIO
import dht11
import time
import datetime
import matplotlib.pyplot as plt
# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

temp =[]
hum = []
timey =[]

# read data using pin 14
instance = dht11.DHT11(pin=14)
loop = 1
ex = 0
try:
	while True:
		result = instance.read()
		if result.is_valid():
			t = datetime.datetime.now()
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %-3.1f C" % result.temperature)
			print(result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)

			time.sleep(10)
			temp.append(result.temperature)
			hum.append(result.humidity)
			timey.append(str(t.hour)+":"+str(t.minute)+":"+str(t.second))
			loop = loop + 1
			print("Loop is :" + str(loop))
			if loop == 6:
				plt.plot(timey,temp)
				plt.ylabel("temp")
				plt.xlabel("time")
				plt.grid()
				plt.savefig("temp"+ str(ex) +".png")
				plt.clf()
				plt.plot(timey,hum)
				plt.ylabel("hum")
				plt.xlabel("time")
				plt.grid()
				plt.savefig("hum"+ str(ex) +".png")
				plt.clf()
				loop = 1
				ex = ex + 1
				temp = []
				hum = []
				timey=[]
			if ex == 2:
				break

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()
