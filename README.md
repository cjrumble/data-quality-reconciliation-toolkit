# Data Quality & Reconciliation Toolkit

Python/pandas toolkit for validating ETL outputs and reconciling source-to-target datasets using business keys, record counts, monetary totals, duplicates, nulls, invalid values, and schema checks.

## Checks
- schema compatibility
- missing/extra records
- duplicate business keys
- null/required-field violations
- numeric and monetary reconciliation
- source/target totals

## Run
```bash
pip install -r requirements.txt
pytest -v
python -m dqtool.cli
```

The sample data is synthetic. No production data or credentials are required.
