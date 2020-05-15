from pathlib import Path
import datetime
import csv


p = Path('.')
csv_files = p.glob("*.csv")

# Please update this in year 2099 :P
current_year = datetime.datetime.now().year - 2000
current_month = datetime.datetime.now().month
graduation_month = 5  # Almost all graduating people leave in May

contacts = """# Contacts

## :warning: DO NOT edit readme.md - Use update.py :warning:

After updating any contacts in CSV, run `update.py` to regenerate the README.

To add any new content except contacts, change text in update.py.

[Current Executives: 2018](2018.csv)

[Current Core Team Members: 2019](2019.csv)

**Executives**
1.  Anjay Goel
2.  Debajyoti Dasgupta
3.  Mukul Mehta
4.  Pankaj Kumar Agarwal
5.  Parth Paradkar
6.  Priyanshu Kumar Singh
7.  Raghavendra Kaushik
8.  Raj Gupta
9.  Shubham Mishra
10. Soumyajit Chakraborty
11. Hemanth Kumar

---

Notes:

- YYYY.csv means people who joined KGP in year YYYY.
- First, Second and Third column should always be `Name`, `Batch` and `Email` respectively.
- `Batch` should end with `'YY`, where YY is the year when they graduate.
---
"""


# Get the email ids to be used in a Google Calendar invite for a physical meeting
email_ids_for_calendar_invite = {}

def has_graduated(batch):
    """
    batch: string e.g. MA '19
    """
    graduation_year = int(batch.split("'")[-1])
    if graduation_year != current_year:
        return current_year > graduation_year
    else:
        return current_month > graduation_month



# Create contacts table with latest batch on top
contacts_table = "# All Contacts\n\n"

for file in sorted(csv_files, reverse=True):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                year = file.name.split('.')[0]
                contacts_table += f"## {year} \n"
                contacts_table += f"| {' | '.join(row)} | \n"
                contacts_table += f"{'| ---- '*len(row)} |\n"
            else:
                contacts_table += f"| {' | '.join(row)} | \n"
                if not has_graduated(row[1]):
                    try:
                        email_ids_for_calendar_invite[file.name].append(row[2])
                    except KeyError:
                        email_ids_for_calendar_invite[file.name] = [row[2]]

        contacts_table += " \n "
        print(f'Processed {line_count} lines.')

calendar_emails = """# Google Calendar Invite

Use these email addresses to send invite for a physical meeting on campus.

*Do not send an invite to kossiitkgp@googlegroups.com*

Copy the text below. Paste in the guest list text box and press Tab!

"""

for key, value in email_ids_for_calendar_invite.items():
    calendar_emails += f"**{key.split('.')[0]}** \n ```"
    calendar_emails += " ".join(value)
    calendar_emails += "```\n\n"

contacts += calendar_emails
contacts += contacts_table

with open("README.md", "w+") as readme:
    readme.write(contacts)
