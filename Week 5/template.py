"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class records:
    def __init__(self, label
value, limit):
        self.label = label
        self.value = self.value
        self.limit = limit

    def percent(self):
        return (self.value / self.limit) * 100
def status(self):
    p = self.percent()
    if p >= 100:
        return "OVER LIMIT"
    elif p >= 90:
        return "WARNING"
    else:
        return "OK"
def is_over(self):
    return self.value > self.limit
# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

records = []   # replace with your code
def load_records(path):
    records = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, v_str, l_str = line.split(',')
records.append(Record(label, float(v_str), float
                      l_str))
    return records
try:
    records = load_records("records_sample.txt")
except FileNotFoundError:
    records = []

records.append(Record("10.0.0.5", 12,400))
records.append(Record("10.0.0.12", 380, 400))
records.append(Record("10.0.0.23", 410, 400))
# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
over_count = 0
for record in records:
    print("=" * 34)
    print(f"RECORD CHECK - {record.label}")
    print("-" * 34)

    st = record.status()
    print(f" Source IP: {record,label}")
    print(f" Failed: {record.value} / {record.limit}")
    print(f" Percent: {record.percent():.1f}%")
    print(f" Status: {st}")

    print("-" * 34)
    if st== "OVER LIMIT":
        over_count += 1
print(f"\nTotal OVER LIMIT:
      {over_count} / {len(records)}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
 z