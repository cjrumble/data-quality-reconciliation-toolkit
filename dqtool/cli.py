from .reconcile import reconcile

if __name__ == "__main__":
    import json
    print(json.dumps(reconcile("data/source.csv","data/target.csv"), indent=2))
