import time, random
from pymongo import MongoClient
U="mongodb+srv://miko:1234@cluster0.qfeqp.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

cluster = MongoClient(U)

name = "miko"
db = cluster["base"]
collection = db["data"]
true_c = 0
while True:
    user = collection.find_one({"name": name})
    coins = user["coins"]
    print("u have", coins, "coins")
    cant_bet = True
    while cant_bet:
        bet = int(input("how many coins u want to bet?"))
        if bet <= coins:

            cant_bet = False
        if int(bet) > coins:
            print("u don't have enough coins")
            cant_bet = True
        if int(bet) < 1:
            print("min bet is 1 coin")
            cant_bet = True
    print("your bet has been accepted")
    true_c = 0
    while true_c != 1:
        choose = int(input("type 1 or 2"))
        if choose == 1 or choose == 2:
            true_c = 1
    print("your number is -  ",choose)

    to_roll = random.randint(5, 10)
    roll = 0.2
    prin = 0
    while to_roll > 1:


        if roll == 0.1:
            prin = 2
            print(prin)
            roll = 2
        if roll == 0.2:
            prin = 1
            print(prin)
            roll = 1
        roll /= 10


        to_roll -= 1
        time.sleep((10 - to_roll) / 30)

        if to_roll == 1:

            print("out of roll – rolled", prin)
            to_roll -= 1

    if prin == choose:
        print("u won", bet, "coins!!!!!!")
        collection.update_one({"name": name}, {"$set": {"coins": coins + bet}})
    if prin != choose:
        print("u lose", bet, "coins, try again")
        collection.update_one({"name": name}, {"$set": {"coins": coins - bet}})


