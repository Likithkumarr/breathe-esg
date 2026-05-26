# Data Models

## RawRecord

Stores uploaded raw CSV records.

Fields:
- source_type
- file_name
- raw_data
- suspicious
- created_by

---

## NormalizedEmission

Stores normalized ESG emission records.

Fields:
- raw_record
- category
- activity_type
- activity_value
- unit
- normalized_unit
- approved

---

## AuditLog

Stores review activity logs.

Fields:
- row_id
- action
- old_value
- new_value
- changed_by
- timestamp