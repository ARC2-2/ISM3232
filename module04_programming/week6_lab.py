# week6_lab.py
# Author: Aaron Contente

records = [
    {
        "id": 1,
        "name": "Taylor",
        "show": "Hamilton",
        "amount": 250,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "show": "Wicked",
        "amount": 120,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "show": "The Lion King",
        "amount": 480,
        "status": "Approved",
    },
    {
        "id": 4,
        "name": "Riley",
        "show": "Chicago",
        "amount": 85,
        "status": "Pending",
    },
    {
        "id": 5,
        "name": "Alex",
        "show": "Hadestown",
        "amount": 310,
        "status": "Pending",
    },
]

LIMIT = 150
HIGH = 300
total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        total += rec["amount"]
        if rec["amount"] > LIMIT:
            flagged.append(rec)
        if rec["amount"] > HIGH:
            high_value.append(rec)

import os

os.makedirs("data", exist_ok=True)

lines = [
    f"Pending total:   ${total:,.2f}",
    f"Needs review:    {len(flagged)}",
    f"High-value:      {len(high_value)}",
]
for line in lines:
    print(line)

with open("data/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for r in flagged:
    print(f"  ID {r['id']}: {r['name']} - ${r['amount']:,.2f}")
