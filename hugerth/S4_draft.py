import re, requests, datetime, operator, 
from dateutil import parser
from collections import defaultdict

print "YO! This ain't working yet, yo!"

# Define Weekday Dictionary
weekdays = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday', '6': 'Sunday'}

# Get clearance
with open(".password") as secret:
    password = secret.read().strip()

# Find the name of every repo in pythonkurs
all_repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=("hugerth", password))
all_repos = all_repos.json()

wordcount = defaultdict(int)
partialcount = 0
commitcounts = []
lencounts = []
daycount = defaultdict(int)
hourcount = defaultdict(int)

# For each of them, get all commits
for repo in all_repos:
	url = repo['commits_url']
	url = url.split("{")[0]
	commits = requests.get(url)
	commits = commits.json()
	for commit in commits:
		partialcount+=1		#Count commits per user
		message = commit['commit']['message']	# Do fun stuff with the messages
												# This works in iPython, gives error when I try running!
		words = message.split(' ')
		length = len(words)	#Count number of words in commit messages
		lencounts.append(length)
		for word in words:			#Count word frequency in commit messages
			wordcount[word]+=1
		datime = parser.parse(commit['commit']['author']['date']) # Do fun things with the date
		daycount[datime.day] += 1
		hourcount[datime.hour] += 1
	commitcounts.append(partialcount)
	partialcount = 0

## And it's at this point I'm told I have a syntax error. Any insights??

top_word = max(wordcount.iteritems(), key=operator.itemgetter(1))[0]
top_wordcount = max(wordcount.iteritems(), key=operator.itemgetter(1))[1]
top_day = max(daycount.iteritems(), key=operator.itemgetter(1))[0]
top_day = weekdays[top_day]
top_daycount = max(daycount.iteritems(), key=operator.itemgetter(1))[1]
top_hour = max(daycount.iteritems(), key=operator.itemgetter(1))[0]
top_hourcount = max(daycount.iteritems(), key=operator.itemgetter(1))[1]

print "Most common day to commit: " + top_day + " - " + repr(top_daycount) + " commits"
print "Most common hour to commit: " + repr(top_hour) + " - " + repr(top_hourcount) + " commits"
print "Longest commit message: " + repr(max(lencounts)) + " words"
print "Average commit message: " + repr(sum(lencounts)/len(lencounts)) + " words"
print "Most common word in commit messages: " + top_word + " - " + repr(top_wordcount) + " times"
print "Largest number of commits from a single user: " + repr(commitcount)
print "Average number of commits per user: " + repr(sum(commitcounts)/len(commitcounts))
		


## Give: most common day *ok
## Most common hour of the day *ok 
## Max number of commits per user *ok
## Average number of commits per user *ok
## Average length of commit message	*ok
## Length of longest commit message *ok
## Most common words in commit messages * ok

