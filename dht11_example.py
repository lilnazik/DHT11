import RPi.GPIO as GPIO
import dht11
import time
import datetime
import matplotlib.pyplot as plt
import telebot, os
from telebot import types
bot = telebot.TeleBot("659141457:AAEf6Qk7v09q9HWffg8qzBX8Aqd27YSx3pk")
chat_id = 638027434
# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

temp =[]
hum = []
timey =[]

# read data using pin 14
instance = dht11.DHT11(pin=14)
loop = 1
try:
	while True:
		result = instance.read()
		if result.is_valid():
			t = datetime.datetime.now()
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %-3.1f C" % result.temperature)
			print(result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)

			time.sleep(120)
			temp.append(result.temperature)
			hum.append(result.humidity)
			timey.append(str(t.hour)+":"+str(t.minute)+":"+str(t.second))
			loop = loop + 1
			print("Loop is :" + str(loop))
			if loop == 30:
				plt.plot(timey,temp)
				plt.ylabel("temp")
				plt.xlabel("time")
				plt.grid()
				plt.savefig("temp.png")
				plt.clf()
				plt.plot(timey,hum)
				plt.ylabel("hum")
				plt.xlabel("time")
				plt.grid()
				plt.savefig("hum.png")
				plt.clf()
				loop = 1
				ex = ex + 1
				temp = []
				hum = []
				timey=[]
				sti = open('temp.png', 'rb')
				bot.send_photo(chat_id, sti)
				sti = open('hum.png', 'rb')
				bot.send_photo(chat_id, sti)

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()
