# WAP that scans an email address and forms a tuple of username and domain
email = input("Enter the email address: ")
email = email.split("@")
email_tuple = tuple(email)
print(email_tuple)
