import csv
from time import sleep
import pathlib
from timeit import default_timer as timer
import datetime
import urllib3
import instaloader

# Get instance
L = instaloader.Instaloader()

# Login or load session

#L.login('username', 'password')        # (login)
L.interactive_login('gucciolives')      # (ask password on terminal)

pathlib.Path('downloads/').mkdir(parents=True, exist_ok=True)

http = urllib3.PoolManager()

start = timer()
curr = str(datetime.datetime.now())

def wait_for_internet_connection():
    while True:
        try:
            response = http.request('GET', 'http://www.google.com')
            return
        except:
            print('No internet connection.\nTrying after 5 seconds.\n')
            sleep(5)


pro = input("profile to scrape: ")

print('\n\nGetting followers from',pro)
filename = 'downloads/' + pro + '_followers.csv'
with open(filename,'a',newline='',encoding="utf-8") as csvf:
    csv_writer = csv.writer(csvf)
    csv_writer.writerow(['user_id','username'])

profile = instaloader.Profile.from_username(L.context, pro)
main_followers = profile.followers
count = 0
total=0
# Print list of followers
for person in profile.get_followers():
    try:
        total+=1
        user_id = person.userid
        username = person.username
        with open(filename,'a',newline='') as csvf:
            csv_writer = csv.writer(csvf)
            csv_writer.writerow([user_id,username])
        print('--------------------------------------------------------------------------------\nTotal followers scraped:',total,' out of',main_followers)
        print('Time:',str(datetime.timedelta(seconds=(timer()-start))))
        print('Current Account:', user_id)
    except Exception as e:
        print(e)

print('\n\nGetting followees from',pro)
filename = 'downloads/' + pro + '_followees.csv'
with open(filename,'a',newline='',encoding="utf-8") as csvf:
    csv_writer = csv.writer(csvf)
    csv_writer.writerow(['user_id','username'])

#profile = instaloader.Profile.from_username(L.context, pro)
main_followees = profile.followees
count = 0
total=0
# Print list of followees
for person in profile.get_followees():
    try:
        total+=1
        user_id = person.userid
        username = person.username
        with open(filename,'a',newline='') as csvf:
            csv_writer = csv.writer(csvf)
            csv_writer.writerow([user_id,username])
        print('--------------------------------------------------------------------------------\nTotal followees scraped:',total,' out of',main_followees)
        print('Time:',str(datetime.timedelta(seconds=(timer()-start))))
        print('Current Account:', user_id)
    except Exception as e:
        print(e)
