import os
import time

# List of directories where lock files will be created
lock_dirs = [
    "/dev/mqueue",
    "/dev/shm",
    "/tmp",
    "/var/run",
    "/var/tmp"
]

# List of lock file names
lock_files = [
    "malicious.lock",
    ".hidden_malicious.lock",
    "exploit.lock",
    "temp_script.lock",
    "unauthorized.lock"
]

def create_lock_files():
    print("[*] Creating suspicious lock files...")

    for directory in lock_dirs:
        for lock_file in lock_files:
            lock_path = os.path.join(directory, lock_file)
            try:
                # Ensure the directory exists
                os.makedirs(directory, exist_ok=True)
                
                # Create the lock file
                with open(lock_path, "w") as f:
                    f.write("Simulating unexpected lock file")

                # Change permissions to make it world-readable and writable
                os.chmod(lock_path, 0o666)  # rw-rw-rw- (world-readable)

                print(f"[+] Created: {lock_path}")

            except Exception as e:
                print(f"[-] Failed to create {lock_path}: {e}")

def main():
    print("[*] Simulating unexpected global lock file activity for osquery detection...")

    create_lock_files()

    print("[*] Waiting for the query interval to pass...")
    time.sleep(10)

    print("[*] Simulation completed. Run your osquery query now.")

if __name__ == "__main__":
    main()
