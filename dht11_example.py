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
time =[]

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
			time.append(t.second)
			loop =+ 1
			print("Loop is :" + loop)
			ex =+ 1
			if loop == 6:
				plt.plot(time,temp)
				plt.ylabel("temp")
				plt.xlabel("time")
				plt.grid()
				plt.savefig("temp"+ ex +".png")
				plt.clf()
				plt.plot(time,hum)
				plt.ylabel("hum")
				plt.xlabel("time")
				plt.grid()
				plt.savefig("hum"+ ex +".png")
				plt.clf()
				loop = 1
			if ex == 2:
				break

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()
