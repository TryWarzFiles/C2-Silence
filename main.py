import os, getpass, sys, json
from utils.plugin.commun import Title, clear, Fore
from sys import stdout
from utils.attack import SilenceAttack
from utils.subscriber import add_user, remove_user
from utils.Owners import Owners
from utils.AutoReset import resetauto
# Developper : TryWarz#3073
# Co - Owners : BduMix🇦🇱#4266
# Thank using Silence Network
username = getpass.getuser()

def commands():
    stdout.write(Fore.LIGHTCYAN_EX+"╔═══"+Fore.LIGHTCYAN_EX+"["f"{username}"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTCYAN_EX+"Silence"+Fore.CYAN+"]"+Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.WHITE)
    commands = input()
    with open('subscriptions.json', 'r') as f:
            subscriptions = json.load(f)

    if commands == "help":
        clear()
        Title().help()
    elif commands == "layer4":
        clear()
        Title().layer4()
    elif commands == "layer7":
        Title().layer7()
    elif commands == "tools":
        Title().tools()
    elif commands == "vip":
        if username in subscriptions:
            vip = subscriptions[username]['vip']
            if vip == "True":
                Title().method()
            else:
                return print('Upgrade Plan')
        else:
            return print('Buy plan')
    elif commands.startswith('attack'):
        args = commands.split()
        if len(args) < 5:
            print("[>] attack [host] [port] [time] [methods]")
        else:
            SilenceAttack().attack(args[1], args[2], args[3], args[4])
    elif commands.startswith('adduser'):
        if username == "root" or "trywarz":
            args = commands.split()
            if args[2] == 'bronze' or 'sliver' or 'gold' or 'platinum' or 'diamond':
                add_user(args[1], args[2], args[3])
                Owners().logs(commands, args[1], args[2])
            else:
                return print('Plan : [bronze,sliver,gold,platinum,diamond')
        else:
            return print('You have not permission')
    elif commands.startswith('resetplan'):
        if username == "root" or "trywarz":
            args = commands.split()
            remove_user(args[1])
        else:
            return print('You have not permission')
    else:
        print('[>] help or ?')
    
if __name__ == '__main__':
    try:
        clear()
        Title().home()
        while True:
            commands()
    except KeyboardInterrupt:
        sys.exit()
            

            
