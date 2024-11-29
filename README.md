# Monitoring SM3
## Notify via Discord Script
This script is a Python-based utility for sending notifications via Discord webhooks. It is designed to integrate with monitoring tools, such as CheckMK, to notify about host or service state changes.

---

## Features
- **Dynamic Messages**: Constructs messages based on the context (host or service).
- **Customizable Notifications**: Supports multiple states (e.g., CRITICAL, WARNING, OK) with corresponding colors.
- **Effortless Integration**: Uses environment variables to collect necessary context for the notification.
- **Error Handling**: Provides error details if the notification fails.

---

## Requirements
- **Python**: Version 3.x
- **Dependencies**: Install the `requests` library if not already installed:
  ```bash
  pip install requests
- Place this file in path '/omd/sites/{sitename}/local/share/check_mk/notifications.'.
  
---

## Sources
- [Github Gist](https://gist.github.com/n00rm/32f1334b1dd2efc40122fee36551ef17)
- [CheckMK](https://forum.checkmk.com/t/check-mk-discord-notification/29311/)
  
---
© 2024 Julian Loontjens
