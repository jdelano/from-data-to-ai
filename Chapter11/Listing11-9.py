from datetime import datetime

# Open a log file in append mode
logfile = open("Chapter11/chat_log.txt", "a", encoding="utf-8")

# At the start of each conversation
logfile.write(f"=== Conversation started at {datetime.now()} ===\n")