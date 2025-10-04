import random
import time
import datetime

OUT_LOG = "./simulated_logs.txt"
usernames = ["root","admin","test","ubuntu","pi"]
passwords = ["password","123456","admin","root","toor","welcome"]

def simulate_once():
    u = random.choice(usernames)
    p = random.choice(passwords)
    src_ip = f"192.0.2.{random.randint(1,250)}"  # reserved IP range for testing
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    line = f"{ts} - SRC={src_ip} LOGIN_ATTEMPT user={u} pass={p}\n"
    with open(OUT_LOG, "a", encoding="utf-8") as f:
        f.write(line)
    print(line.strip())

if __name__ == "__main__":
    for i in range(30):
        simulate_once()
        time.sleep(0.1)
    print("Wrote simulated logs to", OUT_LOG)
