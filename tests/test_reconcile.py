from dqtool.reconcile import reconcile

def test_reconcile():
    r=reconcile("data/source.csv","data/target.csv")
    assert r["row_count_match"] and r["amount_total_match"]
