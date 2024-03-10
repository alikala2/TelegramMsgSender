# TelegramMsgSender

A very simple script to send your desired texts to a server or host outside of your country to send monitoring messages or your desired messages in Telegram via the API.

By default, it sends and receives data using port 5000.

Currently, it does not support encryption methods and relies on the host system's firewall for access control.

It is useful for sending monitoring messages, but its use is not recommended for sending sensitive information.

This script can be used to monitor servers that are only accessible on the local network.

Here are some additional details about the script:

It is a simple batch script that can be easily edited and customized.
It uses the curl command to send data to the server.
The data is sent in JSON format.
The script can be used to send any type of text, including monitoring messages, alerts, and notifications.
The script can be used to send messages to a Telegram channel or group.
The script can be scheduled to run automatically at regular intervals.
Here are some examples of how the script can be used:

To send a monitoring message to a Telegram channel:
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"{Text}\",\"chat_id\":\"{ChatID}\"}" http://example.com:5000/receive_data

To send an alert to a Telegram group:
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"{Text}\",\"chat_id\":\"{ChatID}\"}" http://example.com:5000/receive_data

To send a notification to a Telegram channel:
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"{Text}\",\"chat_id\":\"{ChatID}\"}" http://example.com:5000/receive_data

I hope this Script is helpful!
