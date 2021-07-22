from pprint import pprint
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

__version__ = '0.1.0'


def get_user_id(client, real_name):
    members = client.users_list()['members']
    for memb in members:
        if memb['real_name'] == real_name:
            return memb['id']
            
            
def get_bot_member_channel_ids(client):
    member_channels = []
    for channel in client.conversations_list()['channels']:
        if channel['is_member']:
            member_channels.append(channel['id'])
    return member_channels
                

def get_most_recent_message_timestamp(client, channel_id, user_name, text):
    history = client.conversations_history(channel=channel_id)
    messages = history['messages']
    for msg in messages:
        is_bot = msg['user'] == get_user_id(client, user_name)
        is_auto_msg = text in msg['text']
        if is_bot and is_auto_msg:
            return msg['ts']
            
            
bot_token = os.environ['SLACK_BOT_TOKEN']
bot_name = os.environ['SLACK_BOT_NAME']
bot_text = os.environ['SLACK_BOT_TEXT']
    
client = WebClient(token=bot_token)

member_channel_ids = get_bot_member_channel_ids(client)

for channel_id in member_channel_ids:

    recent_message_timestamp = get_most_recent_message_timestamp(
        client, 
        channel_id, 
        bot_name, 
        bot_text
    )

    if recent_message_timestamp:
        print(f"Deleting recent message in {channel_id} at {recent_message_timestamp}")
        client.chat_delete(
            channel = channel_id,
            ts = recent_message_timestamp
        )

    
    response = client.chat_postMessage(
        channel=channel_id, 
        text=bot_text
    )

    print("posted new message")
    print(response)
        

	