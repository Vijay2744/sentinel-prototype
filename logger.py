from datetime import datetime

def log(action, decision, reason, risk):
    timestamp = datetime.now()

    print("------ SENTINEL LOG ------")
    print("Time:", timestamp)
    print("Action:", action)
    print("Risk Level:", risk)
    print("Decision:", decision)
    print("Reason:", reason)
    print("--------------------------")
