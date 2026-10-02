import pandas as pd

def reconcile(source, target, key="customer_id", amount="amount"):
    s=pd.read_csv(source); t=pd.read_csv(target)
    report={"source_rows":len(s),"target_rows":len(t),"row_count_match":len(s)==len(t),
            "source_total":float(s[amount].sum()),"target_total":float(t[amount].sum())}
    report["amount_total_match"]=report["source_total"]==report["target_total"]
    report["duplicate_source_keys"]=int(s[key].duplicated().sum())
    report["duplicate_target_keys"]=int(t[key].duplicated().sum())
    report["missing_in_target"]=sorted(set(s[key])-set(t[key]))
    report["extra_in_target"]=sorted(set(t[key])-set(s[key]))
    return report
