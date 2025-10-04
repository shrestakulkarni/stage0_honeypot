from faker import Faker
import os
import datetime

fake = Faker()
OUT_DIR = "./honeypot_files"
os.makedirs(OUT_DIR, exist_ok=True)

def make_report(i):
    fname = os.path.join(OUT_DIR, f"financial_report_{datetime.date.today()}_{i}.txt")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(f"Company: {fake.company()}\n")
        f.write(f"Author: {fake.name()}\n")
        f.write(f"Department: {fake.job()}\n")
        f.write(f"Date: {fake.date()}\n\n")
        f.write(fake.paragraph(nb_sentences=8))
        f.write("\n\n-- internal use only --\n")

if __name__ == "__main__":
    for i in range(5):
        make_report(i)
    print("Created decoy files in", OUT_DIR)
