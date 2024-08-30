from simplegmail import Gmail
import csv

gmail = Gmail()

# Unread messages in your inbox
messages = gmail.get_unread_inbox(
    attachments='ignore')

# Starred messages
# messages = gmail.get_starred_messages()

with open('emails.csv','w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    fields = ['to', 'from', 'subject', 'date', 'preview']
    writer.writerow(fields)

    # Print them out!
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)
        # print("Message Body: " + message.plain)  # or message.html
        writer.writerow([
            message.recipient,
            # bytes(message.recipient, 'utf-8').decode('utf-8', 'ignore'),
            message.sender,
            # bytes(message.sender, 'utf-8').decode('utf-8', 'ignore'),
            message.subject,
            # bytes(message.subject, 'utf-8').decode('utf-8', 'ignore'),
            message.date,
            message.snippet
            # bytes(message.snippet, 'utf-8').decode('utf-8', 'ignore')
        ])