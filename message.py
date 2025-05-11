import csv

from file_manager import write, read, generate_id, current_time

def send_message():
    receiver = input("Enter teacher's email: ")
    text = input("Enter your message: ")
    messages = read("messages.csv")
    msg_id = generate_id(messages)
    write("messages.csv", [msg_id, receiver, text, current_time(), "unread"])
    print("Message saved successfully!")

def show_messages(teacher_email):
    messages = read("messages.csv")
    unread_count = sum(1 for m in messages if m[1] == teacher_email and m[4] == "unread")
    print(f"Messages received (Unread: {unread_count}):")
    for msg in messages:
        if msg[1] == teacher_email:
            print(f"[{msg[3]}] {msg[2]} ({msg[4]})")
            msg[4] = "read"
    with open("data/messages.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(messages)