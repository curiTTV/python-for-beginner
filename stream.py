# 
# booL: True / False
# string: "ahd7gai2fbaigbia"
# int(eger): 92385327
# float: 123123123.900
# 

# ==
# !=


# ===
# !==


# "2" == 2 -> true
# 2.0 == 2 -> true
# 2.0 == "2" -> true
# "2" == 1 -> false

# "2" !== 2 -> false
# 2.0 === 2 -> false
# 2.0 === "2" -> false

# 10 > 2 -> true
# 10 >= 10 -> true
# 10 >= "5" -> true

print(2 + 4)
print(2 - 4)
print(2 / 4)
print(2 * 4)

# rest
print(4 % 2)
print(5 % 2)

# floor division
print(5 // 2)

print("----------------------")

bla_bla = "asd"

print(bla_bla)

print("----------------------")

chat_message = "Hallo Welt"

if chat_message == "":
    print("chat message is empty")
else:
    print(chat_message)

print("----------------------")

chat_message = "   "

if chat_message.strip() == "":
    print("chat message is empty - checked with strip")
else:
    print(f"msg: {chat_message}")

print("----------------------")

is_logged_in = True
chat_message = "Hi, bin neu hier"

# alternativ
# if is_logged_in:
if is_logged_in is True and chat_message != "":
    print("user is logged in")
    print(chat_message)
else:
    print("user is NOT logged in")

# if is_logged_in is True:
#     print("user is logged in")
#     if chat_message != "":
#         print(chat_message)
# else:
#     print("user is NOT logged in")

print("----------------------")

messages = [
    ":D",
    "wir könnten am Ende das Primfaktor-Kata machen. ^^",
    "Keine Heapallokierung?",
    "xD",
    "Alles nur Stack based?",
    "Ok ;)",
    "Inhaltvergleich",
    "\"is\" st der Referenzvergleich",
    "Danke @achereto",
    "Hello there",
    "again xD"
]

for message in messages:
    print(message)

print("----------------------")

print("using i")

messages_count = len(messages)
i = 0
while i < messages_count:
    print(messages[i])
    i += 1

print("----------------------")

messages = [
    {
        "username": "user1",
        "message": ":D"
    },
    {
        "username": "user2",
        "message": "wir könnten am Ende das Primfaktor-Kata machen. ^^"
    },
    {
        "username": "user1",
        "message": "Keine Heapallokierung?"
    },
    {
        "username": "user2",
        "message": "xD"
    },
    {
        "username": "user2",
        "message": "Alles nur Stack based?"
    },
    {
        "username": "user1",
        "message": "Ok ;)"
    },
    {
        "username": "user2",
        "message": "Inhaltvergleich"
    },
    {
        "username": "user2",
        "message": "\"is\" st der Referenzvergleich"
    },
    {
        "username": "user1",
        "message": "Danke @achereto"
    },
    {
        "username": "user2",
        "message": "Hello there"
    },
    {
        "username": "user1",
        "message": "again xD"
    }
]

for message in messages:
    # print(message["username"] + ": " + message["message"])
    print(f'{message["username"]}: {message["message"]}')

print("----------------------")

def format_chat_message(username, message):
    return f"{username}: {message}"

chat_message = format_chat_message("curi", "hallo")
print(chat_message)

print(format_chat_message("curi", "hallo"))

for message in messages:
    print(format_chat_message(message["username"], message["message"]))

print("----------------------")

# typecasting

integer = 123
string = "foobar"

print(integer)
print(string)

print(str(integer) + string)

print(f"{integer} {string}")

print("----------------------")

print(5 * "foo")
