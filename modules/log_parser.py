import os

LOG_DIR = "C:/DevOps/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def parse_logs():
    log_files = [f for f in os.listdir(LOG_DIR) if f.endswith(".log")]
    if not log_files:
        print("No log files found in", LOG_DIR)
        return

    for filename in log_files:
        with open(os.path.join(LOG_DIR, filename), "r") as f:
            errors = [line for line in f if "ERROR" in line]
            if errors:
                print(f"\n{filename}:")
                for e in errors:
                    print(e.strip())

if __name__ == "__main__":
    parse_logs()
