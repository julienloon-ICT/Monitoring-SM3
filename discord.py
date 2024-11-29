#!/usr/bin/env python3
# Notify via Discord

import os
import requests
import sys

USERNAME = "CheckMK | Julian Loontjens"
AVATARURL = "https://www.gartner.com/pi/vendorimages/checkmk_infrastructure-monitoring-tools_1698154864463.png"

COLORS = {
    "CRITICAL": "15597568",
    "DOWN": "15597568",
    "WARNING": "16768256",
    "OK": "52224",
    "UP": "52224",
    "UNKNOWN": "13421772",
    "UNREACHABLE": "13421772",
}

def discord_msg(context):
    """Build the message for discord"""
    facts = []
    if context.get('WHAT', None) == "SERVICE":
        state = context["SERVICESTATE"]
        color = COLORS.get(state)
        subtitle = "Service Notification"
        facts.append({"name": "Service:", "value": context["SERVICEDESC"]})
        output = context["SERVICEOUTPUT"] if context["SERVICEOUTPUT"] else ""
    else:
        state = context["HOSTSTATE"]
        color = COLORS.get(state)
        subtitle = "Host Notification"
        output = context["HOSTOUTPUT"] if context["HOSTOUTPUT"] else ""

    facts.extend([
        {
            "name": "Host:",
            "value": context["HOSTNAME"]
        },
        {
            "name": "State:",
            "value": state
        }
    ])

    return {
        "username": USERNAME,
        "avatar_url": AVATARURL,
        "embeds": [
        {
            "title": subtitle,
            "color": color,
            "fields": facts,
            "footer": {
               "text": output
           }
        }
        ]
    }

def collect_context():
    return {
        var[7:]: value
        for (var, value) in os.environ.items()
        if var.startswith("NOTIFY_")
    }

def post_request(message_constructor, success_code=204):
    context = collect_context()

    url = context.get("PARAMETERS")
    r = requests.post(url=url, json=message_constructor(context))

    if r.status_code == success_code:
        sys.exit(0)
    else:
        sys.stderr.write(
            "Failed to send notification. Status: %i, Response: %s\n" % (r.status_code, r.text))
        sys.exit(2)

if __name__ == "__main__":
    post_request(discord_msg)