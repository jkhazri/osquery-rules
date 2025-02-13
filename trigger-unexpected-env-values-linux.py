import os
import time
import subprocess

def set_suspicious_env():
    print("[*] Setting up suspicious environment variables...")

    # Modify HISTFILE to an unusual location
    os.environ["HISTFILE"] = "/tmp/.hidden_history"

    # Set an unexpected LD_PRELOAD path
    os.environ["LD_PRELOAD"] = "/tmp/preload.so"

    # Set an environment variable with an excessively long value
    os.environ["EVIL_VAR"] = "A" * 2048  # Over 1024 characters

    print("[+] Environment variables set!")

def launch_suspicious_process():
    print("[*] Launching processes with suspicious environment variables...")

    # Run a simple command with modified environment variables
    subprocess.Popen(["/bin/bash", "-c", "echo 'Evil command executed'"], env=os.environ)

    # Run a command that manipulates security settings
    subprocess.Popen(["/bin/bash", "-c", "chattr -i /etc/passwd"], env=os.environ)

    print("[+] Suspicious processes started!")

def main():
    print("[*] Simulating unexpected environment values for osquery detection...")

    set_suspicious_env()
    launch_suspicious_process()

    print("[*] Waiting for the query interval to pass...")
    time.sleep(10)

    print("[*] Simulation completed. Run your osquery query now.")

if __name__ == "__main__":
    main()
