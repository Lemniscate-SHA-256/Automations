# bots/slack_bot.py
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import schedule
import time

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

def post_release(version):
    try:
        response = client.chat_postMessage(
            channel="#projects",
            text=f"Neural-dsl v{version} released! Fixed 10 bugs (e.g., WebSocket data). Try `pip install neural-dsl=={version}`. Feedback? [GitHub link]"
        )
    except SlackApiError as e:
        print(f"Error posting to Slack: {e}")

if __name__ == "__main__":
    schedule.every().hour.do(lambda: post_release(os.environ.get("LATEST_VERSION", "0.1.1")))
    while True:
        schedule.run_pending()
        time.sleep(60)