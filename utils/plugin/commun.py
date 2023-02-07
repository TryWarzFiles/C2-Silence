import os
from colorama import Fore
from os import system, name

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def clear():
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')

class Title:
    def home(self):
        clear()
        print(center(Fore.CYAN + f"""
      ╔═╗┬┬  ┌─┐┌┐┌┌─┐┌─┐  ╔╗╔┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─
      ╚═╗││  ├┤ ││││  ├┤   ║║║├┤  │ ││││ │├┬┘├┴┐
      ╚═╝┴┴─┘└─┘┘└┘└─┘└─┘  ╝╚╝└─┘ ┴ └┴┘└─┘┴└─┴ ┴
{Fore.LIGHTCYAN_EX}        ══╦═════════════════════════════════╦══
╔═════════╩═════════════════════════════════╩═════════╗
║ {Fore.LIGHTWHITE_EX} Welcome To The Main Screen Of Silence{Fore.LIGHTCYAN_EX}              ║
║ {Fore.LIGHTWHITE_EX} Type [help] to see the Commands{Fore.LIGHTCYAN_EX}                    ║
║ {Fore.LIGHTWHITE_EX} Join Telegram : https://t.me/silencenetworks{Fore.LIGHTCYAN_EX}       ║
╚═════════════════════════════════════════════════════╝"""))
        print("\n")
        
    
    def help(self):
        clear()
        print(center(Fore.CYAN + f"""
                                                     ╦ ╦╔═╗╦  ╔═╗             
                                                     ╠═╣║╣ ║  ╠═╝             
                                                     ╩ ╩╚═╝╩═╝╩
                                        {Fore.LIGHTCYAN_EX}══╦═════════════════════════════════╦══
                                ╔═════════╩═════════════════════════════════╩═════════╗
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}layer7   {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Show Layer7 Methods                    {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}layer4   {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Show Layer4 Methods                    {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.YELLOW}vip      {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Show Methods VIP                       {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}tools    {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Show tools                             {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}credit   {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Show credit                            {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}exit     {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Exit Silence DDoS                      {Fore.LIGHTCYAN_EX}║
                                ╠═════════════════════════════════════════════════════╣
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}THANK    {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Thanks for using Silence.              {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}YOU♥     {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} I Love you :)                          {Fore.LIGHTCYAN_EX}║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}Telegram {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} https://t.me/silencenetworks           {Fore.LIGHTCYAN_EX}║
                                ╚═════════════════════════════════════════════════════╝"""))
        print("\n")
    
    def layer4(self):
        clear()
        print(center(Fore.CYAN + f"""
                                                    ╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦             
                                                    ║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣             
                                                    ╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩              
                                          {Fore.LIGHTCYAN_EX}══╦═════════════════════════════════╦══
                                ╔═══════════╩═════════════════════════════════╩═══════════╗
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}DNS-AMP {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}AMP {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}MIX-AMP {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}AMP {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}NTP-AMP {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}AMP {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}WSD-AMP {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}AMP {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}TCP-SYN {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}SYN {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}TCP-SYN-ACK {Fore.LIGHTCYAN_EX}        | {Fore.LIGHTWHITE_EX}SYN + ACK {Fore.LIGHTCYAN_EX}                      ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}UDP-PPS {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}PPS {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}UDP-RAW {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}RAW {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HOME {Fore.LIGHTCYAN_EX}               | {Fore.LIGHTWHITE_EX}AMP {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}PROTOCOL-RANDOM {Fore.LIGHTCYAN_EX}    | {Fore.LIGHTWHITE_EX}LAYER 3 {Fore.LIGHTCYAN_EX}                        ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}BBHOST-STANDARD {Fore.LIGHTCYAN_EX}    | {Fore.LIGHTWHITE_EX}STANDARD {Fore.LIGHTCYAN_EX}                       ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}BBHOST-PRO-DEFAULT{Fore.LIGHTCYAN_EX}  | {Fore.LIGHTWHITE_EX}PRO TCP {Fore.LIGHTCYAN_EX}                        ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}BBHOST-PRO-FIVEM{Fore.LIGHTCYAN_EX}    | {Fore.LIGHTWHITE_EX}PRO FIVEM {Fore.LIGHTCYAN_EX}                      ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}ECXON-BYPASS{Fore.LIGHTCYAN_EX}        | {Fore.LIGHTWHITE_EX}BYPASS {Fore.LIGHTCYAN_EX}                         ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}TYNAHOST{Fore.LIGHTCYAN_EX}            |{Fore.LIGHTWHITE_EX} BYPASS {Fore.LIGHTCYAN_EX}                         ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HETZNER {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}BYPASS {Fore.LIGHTCYAN_EX}                         ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}OVH-HANDSHAKE {Fore.LIGHTCYAN_EX}      | {Fore.LIGHTWHITE_EX}TCP BYPASS {Fore.LIGHTCYAN_EX}                     ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}OVH-UDP {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}UDP BYPASS {Fore.LIGHTCYAN_EX}                     ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}OVH-GAMING {Fore.LIGHTCYAN_EX}         | {Fore.LIGHTWHITE_EX}GAME BYPASS {Fore.LIGHTCYAN_EX}                    ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HANDSHAKE {Fore.LIGHTCYAN_EX}          | {Fore.LIGHTWHITE_EX}TCP BYPASS {Fore.LIGHTCYAN_EX}                     ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}TIBIA-BYPASS{Fore.LIGHTCYAN_EX}        | {Fore.LIGHTWHITE_EX}TIBIA [ BYPASS ] {Fore.LIGHTCYAN_EX}               ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}MINECRAFT-BYPASS{Fore.LIGHTCYAN_EX}    | {Fore.LIGHTWHITE_EX}MINECRAFT [ BOT'S JOIN + MOTD ]{Fore.LIGHTCYAN_EX} ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}MINECRAFT-MCPE{Fore.LIGHTCYAN_EX}      | {Fore.LIGHTWHITE_EX}MINECRAFT [ MCPE BYPASS ] {Fore.LIGHTCYAN_EX}      ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}FIVEM-BYPASS {Fore.LIGHTCYAN_EX}       | {Fore.LIGHTWHITE_EX}FIVEM [ BYPASS ] {Fore.LIGHTCYAN_EX}               ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}SAMP{Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}SAMP [ BYPASS ] {Fore.LIGHTCYAN_EX}                ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}MTA-BYPASS {Fore.LIGHTCYAN_EX}         | {Fore.LIGHTWHITE_EX}MTA [ BYPASS ] {Fore.LIGHTCYAN_EX}                 ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}RUST-UDP {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}RUST [ UDP ] {Fore.LIGHTCYAN_EX}                   ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}VALVE-UDP {Fore.LIGHTCYAN_EX}          | {Fore.LIGHTWHITE_EX}VALVE [ BYPASS ] {Fore.LIGHTCYAN_EX}               ║
                                ╚═════════════════════════════════════════════════════════╝ 
        """))
        print("\n")

    def layer7(self):
        clear()
        print(center(Fore.CYAN + f"""
                                                     ╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗             
                                                     ║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝       
                                                     ╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩    
                                            {Fore.LIGHTCYAN_EX}══╦═════════════════════════════════╦══
                                ╔═════════════╩═════════════════════════════════╩═════════════╗
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTP-RAW {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}RAW {Fore.LIGHTCYAN_EX}                                ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTPS-RAW {Fore.LIGHTCYAN_EX}          | {Fore.LIGHTWHITE_EX}RAW  {Fore.LIGHTCYAN_EX}                               ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTP-MIX-BYPASS {Fore.LIGHTCYAN_EX}    | {Fore.LIGHTWHITE_EX}MIX BYPASS {Fore.LIGHTCYAN_EX}                         ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTP-MIX-BYPASS {Fore.LIGHTCYAN_EX}    | {Fore.LIGHTWHITE_EX}MIX BYPASS  {Fore.LIGHTCYAN_EX}                        ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTPS-BROWSER {Fore.LIGHTCYAN_EX}      | {Fore.LIGHTWHITE_EX}BROWSER {Fore.LIGHTCYAN_EX}                            ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}CF-UAM-BYPASS {Fore.LIGHTCYAN_EX}      | {Fore.LIGHTWHITE_EX}UAM BYPASS {Fore.LIGHTCYAN_EX}                         ║
                                ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}CF-PRO-BYPASS {Fore.LIGHTCYAN_EX}      | {Fore.LIGHTWHITE_EX}PRO BYPASS {Fore.LIGHTCYAN_EX}                         ║
                                ╚═════════════════════════════════════════════════════════════╝"""))
        print("\n")

    def method(self):
        clear()
        print(center(Fore.CYAN + f"""
                                  ╦  ╦ ╦ ╔═╗
                                  ╚╗╔╝ ║ ╠═╝
                                   ╚╝  ╩ ╩    
                    {Fore.LIGHTCYAN_EX}══╦═════════════════════════════════╦══
        ╔═════════════╩═════════════════════════════════╩═════════════╗
        ║ {Fore.BLUE}LAYER 4{Fore.LIGHTCYAN_EX}                                                     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}DNS-PROVIDERS {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}AMP 50GBPS{Fore.LIGHTCYAN_EX}                     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}NTP-PROVIDERS {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}AMP 100GBPS{Fore.LIGHTCYAN_EX}                    ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}DVR-PROVIDERS {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}AMP 40GBPS{Fore.LIGHTCYAN_EX}                     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}MIX-PROVIDERS {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}AMP 50GBPS{Fore.LIGHTCYAN_EX}                     ║
        ║ {Fore.LIGHTGREEN_EX}BOTNET{Fore.LIGHTCYAN_EX}                                                      ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}SYN-BOTNET {Fore.LIGHTCYAN_EX}              | {Fore.LIGHTWHITE_EX}BOTNET {Fore.LIGHTCYAN_EX}                        ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}VSE-BOTNET {Fore.LIGHTCYAN_EX}              | {Fore.LIGHTWHITE_EX}BOTNET {Fore.LIGHTCYAN_EX}                        ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}STD-BOTNET {Fore.LIGHTCYAN_EX}              | {Fore.LIGHTWHITE_EX}BOTNET {Fore.LIGHTCYAN_EX}                        ║
        ║ {Fore.MAGENTA}METHOD GAMES{Fore.LIGHTCYAN_EX}                                                ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}RUST-UDP {Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}UDP{Fore.LIGHTCYAN_EX}                            ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}FIVEM-BYPASS {Fore.LIGHTCYAN_EX}            | {Fore.LIGHTWHITE_EX}BYPASS{Fore.LIGHTCYAN_EX}                         ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}OVH-GAMING {Fore.LIGHTCYAN_EX}              | {Fore.LIGHTWHITE_EX}GAME BYPASS{Fore.LIGHTCYAN_EX}                    ║
        ║ {Fore.LIGHTYELLOW_EX}LAYER 7{Fore.LIGHTCYAN_EX}                                                     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}CF-BYPASS     {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}BYPASS{Fore.LIGHTCYAN_EX}                         ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}CF-UAM-BYPASS {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}UAM BYPASS{Fore.LIGHTCYAN_EX}                     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}CF-PRO-BYPASS {Fore.LIGHTCYAN_EX}           | {Fore.LIGHTWHITE_EX}PRO BYPASS{Fore.LIGHTCYAN_EX}                     ║
        ║ {Fore.LIGHTBLACK_EX}METHOD BOMB{Fore.LIGHTCYAN_EX}                                                 ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}DNS-BOMB {Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}BOMB 500GBPS{Fore.LIGHTCYAN_EX}                   ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}SYN-BOMB {Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}BOMB 200GBPS{Fore.LIGHTCYAN_EX}                   ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HANDSHAKE-BOMB {Fore.LIGHTCYAN_EX}          | {Fore.LIGHTWHITE_EX}BOMB 100GBPS{Fore.LIGHTCYAN_EX}                   ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}UDP-BOMB {Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}BOMB 200GBPS{Fore.LIGHTCYAN_EX}                   ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTP-BOMB {Fore.LIGHTCYAN_EX}               | {Fore.LIGHTWHITE_EX}HTTP BOMB - 7000000 RQ/S{Fore.LIGHTCYAN_EX}       ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTPS-BOMB {Fore.LIGHTCYAN_EX}              | {Fore.LIGHTWHITE_EX}HTTPS BOMB - 7000000 RQ/S{Fore.LIGHTCYAN_EX}      ║
        ║ {Fore.RED}METHOD NUKE{Fore.LIGHTCYAN_EX}                                                 ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTPS-NUKE {Fore.LIGHTCYAN_EX}              | {Fore.LIGHTWHITE_EX}HTTPS NUKE - 31000000 RQ/S{Fore.LIGHTCYAN_EX}     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}HTTP-NUKE {Fore.LIGHTCYAN_EX}               | {Fore.LIGHTWHITE_EX}HTTPS NUKE - 31000000 RQ/S{Fore.LIGHTCYAN_EX}     ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}SYN-NUKE {Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}SYN NUKE - 500GBS {Fore.LIGHTCYAN_EX}             ║
        ║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}OVH-NUKE {Fore.LIGHTCYAN_EX}                | {Fore.LIGHTWHITE_EX}OVH NUKE - 500GBS {Fore.LIGHTCYAN_EX}             ║
        ╚═════════════════════════════════════════════════════════════╝"""))
        print("\n")


    def tools(self):
        clear()
        print(center(Fore.CYAN + f"""
                    ╔╦╗╔═╗╔═╗╦  ╔═╗             
                     ║ ║ ║║ ║║  ╚═╗             
                     ╩ ╚═╝╚═╝╩═╝╚═╝
        {Fore.LIGHTCYAN_EX}══╦═════════════════════════════════╦══
╔═════════╩═════════════════════════════════╩═════════╗
║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}geoip {Fore.LIGHTCYAN_EX}     |{Fore.LIGHTWHITE_EX} Geo IP Address Lookup{Fore.LIGHTCYAN_EX}                ║
║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}dns   {Fore.LIGHTCYAN_EX}     |{Fore.LIGHTWHITE_EX} Classic DNS Lookup   {Fore.LIGHTCYAN_EX}                ║
║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}mcresolver {Fore.LIGHTCYAN_EX}|{Fore.LIGHTWHITE_EX} Minecraft Resolver   {Fore.LIGHTCYAN_EX}                ║
║ \x1b[38;2;255;20;147m• {Fore.LIGHTWHITE_EX}subnet{Fore.LIGHTCYAN_EX}     |{Fore.LIGHTWHITE_EX} Subnet IP Address Lookup   {Fore.LIGHTCYAN_EX}          ║
╚═════════════════════════════════════════════════════╝"""))
        print('\n')