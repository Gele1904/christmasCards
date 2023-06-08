import os


def create_christmas_cards():
    with open("employees.txt", "r") as file:
        recipients = file.read().splitlines()

    with open("template.txt", "r") as file:
        template = file.read()

    if not os.path.exists("christmasCards"):
        os.mkdir("christmasCards")

    for recipient in recipients:
        card_content = template.replace("NAME", recipient)

        with open(f"christmasCards/{recipient}.txt", "w") as file:
            file.write(card_content)

    print("Christmas cards created successfully!")


create_christmas_cards()
