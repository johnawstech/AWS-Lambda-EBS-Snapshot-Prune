import datetime
import calendar
#import pytz
import time
import os
import boto3

def lambda_handler(event, context):
    now = datetime.datetime.now()
    print("Now: ", now)
    ec = boto3.client('ec2')
    os.environ['TZ'] = 'UTC'
    #present = datetime.datetime()
    ts = time.time()
    DayOfWeek = datetime.datetime.fromtimestamp(ts).strftime('%w')
    Year = datetime.datetime.fromtimestamp(ts).strftime('%Y')
    Month = datetime.datetime.fromtimestamp(ts).strftime('%m')
    DayOfMonth = datetime.datetime.fromtimestamp(ts).strftime('%d')
    HourOfDay = datetime.datetime.fromtimestamp(ts).strftime('%-H')
    MinuteOfDay = datetime.datetime.fromtimestamp(ts).strftime('%M')
    SecOfDay = datetime.datetime.fromtimestamp(ts).strftime('%S')
    print(DayOfWeek)
    print(Year)
    print(Month)
    print(DayOfMonth)
    print(HourOfDay)
    print(MinuteOfDay)
    print(SecOfDay)
    nowepoch = time.time()
    response = ec.describe_snapshots(
        Filters=[
            {
                'Name': 'tag:deleteTime',
                'Values': [
                    'SomeTimeSoon',
                    ]
            },
                ],
        OwnerIds=[
            '386874538391',
                ],
                                    )
    #print response   ### PRINTS EVERYTHING!!! I MEAN EVERYTHING!!
    #print response['SnapshotId'] ## It hated this, straight error
    #print response[0] ## It hated this too, straight error
    for snapshots in response['Snapshots']:
        #print snapshots
        StartTime = snapshots['StartTime']
        SnapshotID = snapshots['SnapshotId']
        #print "Description: ", Description
        #print "State: ", State
        #print "StartTime: ", StartTime
        #print "SnapshotID: ", SnapshotID
        # 2018-03-15 19:00:48+00:00
        StartTime = str(StartTime)
        StartTime = StartTime[:-6]
        Hour = StartTime[11:]
        Hour = Hour[:-6]
        #print "HOUR: ", Hour
        #StartTime = datetime(StartTime)
        #print "StartTimeAgain: ", StartTime
        #print StartTime
        pattern = '%Y-%m-%d %H:%M:%S'
        epoch = int(time.mktime(time.strptime(StartTime, pattern)))
        #print epoch
        secs = nowepoch - epoch
        #print secs
        if(Hour == "01" or Hour == "03" or Hour == "05" or Hour == "07" or Hour == "09" or Hour == "11" or Hour == "13" or Hour == "15" or Hour == "17" or Hour == "19" or Hour == "21" or Hour == "23"):
            if secs >= 345600:  # 4 days 345600
                print("DELETE")
                print(StartTime)
                print(secs)
                try: 
                    ec.delete_snapshot(SnapshotId=SnapshotID)
                except:
                    print ("Delete did not work")
        if(Hour == "02" or Hour == "04" or Hour == "08" or Hour == "10" or Hour == "14" or Hour == "16" or Hour == "20" or Hour == "22"):
            if secs >= 518400:  # 6 days
                print("DELETE")
                print(StartTime)
                print(secs)
                try: 
                    ec.delete_snapshot(SnapshotId=SnapshotID)
                except:
                    print ("Delete did not work")
        if(Hour == "06" or Hour == "18"):
            if secs >= 691200:  # 8 days
                print("DELETE")
                print(StartTime)
                print(secs)
                try: 
                    ec.delete_snapshot(SnapshotId=SnapshotID)
                except:
                    print ("Delete did not work")
        if(Hour == "12"):
            if secs >= 864000:  # 10 days
                print("DELETE")
                print(StartTime)
                print(secs)
                try: 
                    ec.delete_snapshot(SnapshotId=SnapshotID)
                except:
                    print ("Delete did not work")
        if Hour == "00":
            if secs >= 7776000:  # 90 days
                print("DELETE")
                print(StartTime)
                print(secs)
                try: 
                    ec.delete_snapshot(SnapshotId=SnapshotID)
                except:
                    print ("Delete did not work")
