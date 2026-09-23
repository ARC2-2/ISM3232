# week5_lab.py
# Author: Aaron Contente
# Business domain:

event_name = "Hamilton"
status = "Available"
tickets_requested = 4
ticket_price = 125.00
is_group_booking = ticket_price * tickets_requested > 1000

print(
    type(event_name),
    type(tickets_requested),
    type(ticket_price),
    type(is_group_booking),
)

subtotal = ticket_price * tickets_requested
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

print("\n=== Theater Ticket Sales Summary ===")
print(f"Event:            {event_name}")
print(f"Status:           {status}")
print(f"Tickets:          {tickets_requested}")
print(f"Subtotal:         ${subtotal:.2f}")
print(f"Tax:              ${tax:.2f}")
print(f"Total:            ${total:.2f}")
print(f"Requires manager: {requires_approval}")

user_qty = int(input("\nEnter a new ticket quantity: "))
new_total = ticket_price * user_qty * 1.07
print(f"New total for {user_qty} tickets: ${new_total:.2f}")
print(f"Requires manager: {new_total > 1000}")
