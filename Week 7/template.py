"""
RECORD CHECK  -  my version
===========================

Name  :Joshua kalengo
Lane  :Cyber
Date  :Friday 6th November 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Clean a cybersecurity record and convert its values."""

    record = {}

    parts = raw_line.strip().split(",")

    for part in parts:
        key, value = part.split("=", 1)

        key = key.strip().lower()
        value = value.strip().lower()

        if key == "attempts":
            value = int(value)

        record[key] = value

    return record

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []   # replace with your code
raw_records = [
    " SRC=10.0.0.5, ATTEMPTS=12, RESULT=FAILED ",
    "src = 192.168.1.10 , attempts = 3 , result = SUCCESS",
    "SRC=172.16.0.4 ,ATTEMPTS=15, result=failed ",
    "src= 10.0.0.8, ATTEMPTS=2 , RESULT=SUCCESS ",
    " Src = 192.168.1.20, Attempts = 8, Result = Failed "
]
# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    pass   # replace with your code
total_records = 0
flagged_records = 0

for raw_record in raw_records:

    cleaned_record = parse_line(raw_record)

    security_status = status_of(cleaned_record)

    print("Cleaned record:", cleaned_record)
    print("Security status:", security_status)

    total_records += 1

    if security_status == "FLAGGED":
        flagged_records += 1

    print("-" * 40)

print("Total records:", total_records)
print("Flagged records:", flagged_records)
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
