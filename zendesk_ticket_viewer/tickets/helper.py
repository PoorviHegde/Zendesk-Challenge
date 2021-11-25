import requests
import auth as a

def get_tickets():
    response = requests.get('https://'+a.SUB_DOMAIN+'.zendesk.com/api/v2/tickets',auth=(a.USERNAME,a.PASSWORD))
    return response