import datetime
import pytz

now = datetime.datetime.now()
openTime = 9
closeTime = 17

Portland = ['Portland', pytz.timezone("America/Los_Angeles")]
New_York = ['New York', pytz.timezone("America/New_York")]
London = ['London', pytz.timezone("Europe/London")]

branches = [Portland, New_York, London]

def checkHours(now):
    print('The current time in Portland is {}'.format(now.astimezone(Portland[1]).strftime('%I:%M %p')))
    for b in branches:
        if int(now.astimezone(b[1]).strftime('%H')) - openTime >= 0 \
           and int(now.astimezone(b[1]).strftime('%H')) - closeTime < 0:
            print('The {} branch is currently open.'.format(b[0]))
        else:
            print('The {} branch is currently closed.'.format(b[0]))
    

if __name__ == "__main__":
    checkHours(now)
