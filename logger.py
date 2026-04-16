from datetime import datetime

def log(action, decision, reason):
    timestamp = datetime.now()

    print("------ SENTINEL LOG ------")
    print("Time:", timestamp)
    print("Action:", action)
    print("Decision:", decision)
    print("Reason:", reason)
    print("--------------------------")
