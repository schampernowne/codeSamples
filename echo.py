
#We have a set of tasks, each running at least daily, which are scheduled with a simplified cron. We want to find when each of them will next run.

#The scheduler config looks like this:

#30 15 daily
#45 * hourly
#* * minute
#* 19 sixty_times

#The first field is the minutes past the hour, the second field is the hour of the day and the third is the command to run. For both cases * means 
#that it should run for all values of that field. In the above example run_me_daily has been set to run at 3:30pm every day and run_me_hourly at 45 minutes 
#past the hour every hour. The fields are whitespace separated and each entry is on a separate line.

#write a command line program that when fed this config to stdin and the current time in the format HH:MM as command line argument outputs 
#the soonest time at which each of the commands will fire and whether it is today or tomorrow. When it should fire at the current time 
#that is the time you should output, not the next one.

#For example given the above examples as input and the command-line argument 16:10 the output should be

#15:30 tomorrow-daily
#16:45 today-hourly
#16:10 today-minute
#19:00 today-sixty_times

#INSTRUCTIONS: this is run from the command prompt as an executable file. run as "python echo.py <currentTime>". The program will then wait for a prompt.
#enter the rule for when event x occurs (example: 30 15 daily).
# Here is an example from the terminal:
#sarah@UBUNTUVB:~/Desktop$ python echo.py 16:10
#30 15 daily
#15:30 tomorrow-daily
#45 * hourly
#16:45 today-hourly
#* * minute
#16:10 today-minute
#* 19 sixty_times
#19:00 today-sixty_times




#!/usr/bin/env python
#!/usr/bin/python
import sys

time = sys.argv[1]
[hourstr,minutestr] = time.split(":") #separate hour and minute from first argument
#check that we didn't get numbers that aren't valid times of day. 
try:
	int(hourstr)
	int(minutestr) 
except:
	print "bad input"
	exit(0) 
		
	
if int(hourstr) > 23 or int(hourstr) < 0: 
	print "invalid time entered"
if int(minutestr) > 60 or int(minutestr) < 0:
	print "invalid time entered"

#outer loop to read input then prompt for more input until a blank line is entered
while 1:

#reset hour and minute to original integers provided by command argument, 
#read in new line, split into fields, provide integer value for targetm and targeth
	
	hour = int(hourstr)
	minute = int(minutestr)
	line = sys.stdin.readline()
	field = line.split()
	targeth = -1 #simply doing this because targeth and targetm need to be integer type for comparison later
	targetm = -1
#if field[0] and field[1] are not "*", then make sure they are integers (targetm and targeth) so we can compare them to hour and minute
#terminate the program if user inputs blank line	
	if field == []:
		exit(0)
	try:
		if field[1] != "*":
			targeth = int(field[1])
		if field[0] != "*":
			targetm = int(field[0])
	except:
		print "bad input to fields"
		continue
		

		
	day = "today"

#loop to check the hours and minutes, this loop increments hour until it gets the right 
#hour (it increments by one again if, when the minutes are checked, that is necessary). 
#Once we have a matching hour, we increment the minutes (increacing hour by 1 if minute goes past 60)
 
	while 1:
		if hour ==24:
			hour = 0
			if day == "tomorrow":
				print "Something went wrong"
				break
			day = "tomorrow"
		elif hour != targeth and field[1] != "*":
			hour += 1
			minute = 0
		elif minute != targetm and field[0] != "*":
			minute += 1
			if minute == 60:
				hour += 1 
				minute = 0
		else: 
#unsophisticated piece of code to make sure we get "01" instead of "1" in the minutes. 
#I did not do this for hours because none of the examples dealt with that case and it reads the same.		
			if minute < 10:
				print str(hour) + ":" + "0" + str(minute) + " " + day + "-" + field[2]
			
			else: print str(hour) + ":" + str(minute) + " " + day + "-" + field[2] 
			break 
			 
			
		
		
	
	


