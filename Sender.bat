@echo off

REM Send POST request
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"%*\",\"chat_id\":\"{TelegramChatId}\"}" http://Example.com:5000/receive_data
