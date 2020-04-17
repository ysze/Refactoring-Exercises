import random

buyers = "Madeleine Fredrik Hanna-Maria Ante Anne Mats Hakan".split()
previous_recipients = "Mats Ante Hakan Hanna-Maria Madeleine Anne Fredrik".split()
remaining_buyers = set(buyers.copy())

for buyer, previous_recipient in zip(buyers, previous_recipients):
    recipient = random.choice(list(remaining_buyers - {buyer, previous_recipient}))
    remaining_buyers.discard(recipient)
    print(f"{buyer}: {recipient}")
