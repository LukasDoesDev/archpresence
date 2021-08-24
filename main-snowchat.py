from pypresence import Presence
import time

client_id = "879777732521754685" # Lukas client id, this hosts the snowchat logo
RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect() # Start the handshake loop
RPC.update(
    details="Free, Open-Source, Selfhostable",
    state="Chat Platform",
    large_image="logo-brand",
    large_text="Snowchat",
    small_text="ThatOneLukas",
    start=int(time.time()),
    buttons=[
        {
            'label': 'Discord Server',
            'url': 'https://discord.gg/gmMNzdyvM7'
        },
        {
            'label': 'Git Repository',
            'url': 'https://gitlab.com/snowchat/snowchat'
        }
    ]
) # Updates our presence

while True:
    try:
        time.sleep(15)
    except KeyboardInterrupt:
        break

