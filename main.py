from O365 import Account, MSGraphProtocol, FileSystemTokenBackend
from presence import Presence
import light
import time
from datetime import datetime, timedelta
import configparser

conf = configparser.ConfigParser()
conf.read('config.cfg')
client_id = conf.get('o365','client_id')
credentials = (client_id,)
protocol = MSGraphProtocol(api_version='beta')
token_backend = FileSystemTokenBackend(token_path='.', token_filename='my_token.txt')
account = Account(credentials, auth_flow_type='public',protocol=protocol,token_backend=token_backend)
scopes = ['https://graph.microsoft.com/Presence.Read']
colors = {
    'Offline': 'blue',
    'Busy': 'red',
    'DoNotDisturb': 'red',
    'Available': 'green',
    'Away': 'yellow',
    'BeRightBack': 'yellow'
}
presence = Presence(con=account.connection,protocol=protocol)

while True:

    now = datetime.now()
    # if later than 17.00 or later than Friday (4) => sleep
    if now.hour > 17 or now.weekday() > 4:
        print('time to rest!')
        tomorrow = now + timedelta(days=1)
        t = tomorrow
        tomorrow_morning = datetime(t.year, t.month, t.day, 8, 0)
        seconds_to_sleep = (tomorrow_morning - now).total_seconds()
        time.sleep(seconds_to_sleep)

    if not account.is_authenticated:
        account.authenticate(scopes=scopes)

    availability = presence.get_my_presence()
    print(f'availability {availability}')

    color = colors.get(availability, lambda:'Availability color not set yet')
    light.set_color(color)
    time.sleep(60)
