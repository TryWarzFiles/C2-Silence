import requests
import getpass

username = getpass.getuser()
url = "https://discord.com/api/webhooks/1070427581519777792/WIs-0KZylGVHtST1NTIn_3-tuatYPmeFpazg6WCS0tsJkfG8Jz_PT6hXX7Nf_LzZVJrM"

class Owners:
    def logs(self, commands, user, plan):
        
        data = {
        "content" : "",
        "username" : "Silence Logs"
        }
        if commands.startswith("adduser"):
            data["embeds"] = [
            {
            "description" : f"**{username}** à ajouter un nouveau cleints : **{user}** avec le plan **{plan}**",
            "title" : "embed title"
            }
            ]
        if commands.startswith("resetplan"):
            data["embeds"] = [
            {
            "description" : f"**{username}** à supprimer {user}",
            "title" : "embed title"
            }
            ]


        requests.post(url, json=data)