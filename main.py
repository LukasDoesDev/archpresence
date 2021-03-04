from pypresence import Presence
import time
import psutil
import subprocess

client_id = "817047477718351893" # Lukas client id, this hosts the arch logo
RPC = Presence(client_id)  # Initialize the Presence client

kernel_cmd = subprocess.run(["uname", "-r"], capture_output=True) # Get kernel version
kernel = str(kernel_cmd.stdout, 'UTF-8') # Convert to string

RPC.connect() # Start the handshake loop
RPC.update(
    details="Linux " + kernel,
    state="Windows? Ew.",
    large_image="archsvg",
    large_text="Arch Linux Logo",
    start=psutil.boot_time(),
    buttons=[
        {
            'label': 'Install Arch Linux',
            'url': 'https://archlinux.org'
        },
        {
            'label': 'What\'s Linux?',
            'url': 'https://en.wikipedia.org/wiki/Linux'
        }
    ]
) # Updates our presence

while True:
    time.sleep(15)

