'''
' Filename: models.py
' Author: Gabriel 'solstice' Ryan
' Description: I can't be bothered to fill this in right now lololol
'
'
'''
import json

current_alerts = {}

def store_alert(alert):
    
    global current_alerts

    _id = alert['id']

    new_alert = False
    if _id not in current_alerts:
        new_alert = True
    current_alerts[_id] = alert

    print 'adding to', json.dumps(current_alerts, indent=4, sort_keys=True)

    return new_alert

def retrieve_alerts():

    all_alerts = []
   
    return current_alerts.values()

def retrieve_alert(a):

    return current_alerts[a['id']]

def remove_alerts(alerts):
    
    global current_alerts

    print 'removing from', json.dumps(current_alerts, indent=4, sort_keys=True)
    for a in alerts:

        del current_alerts[a['id']]
