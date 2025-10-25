from pyrogram import Client

api_id = 26578856  # no input(), just the number
api_hash = "40d3f23cf16aae72714c07a6a486a3cf"  # string in quotes

with Client("session", api_id=api_id, api_hash=api_hash) as app:
    print("\nYour session string:\n")
    print(app.export_session_string())