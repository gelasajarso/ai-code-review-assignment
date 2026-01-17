def count_valid_emails(emails):
    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        email = email.strip()

        if "@" not in email:
            continue

        local, _, domain = email.partition("@")

        if not local or not domain or "." not in domain:
            continue

        count += 1

    return count
