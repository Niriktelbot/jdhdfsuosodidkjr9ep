import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import time
import vkcoin
token = "vk1.a.AHV3zftVRBU8lutelu8AXRkSClSfcWXCJ9-kJJ7Q5cNHsevpGzg2PpjfdGXG_lBE1MvfRazkODDmc5fqvHFpDMltigYwyF8_I4pTWlFVxIlA9sB2t_X8j99eDPzeuAhYnWwo31rvS7EVNC27s6azskd_19GPX63WzjPiDLKQ_lnRZJmAugb30raVWYMGH8tZ"
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
vk = vk_api.VkApi(token=token)
vk._auth_token()
gr_id=213096773
mgr_id=-213096773
chars = 'abcdefghijklnopqrstuvwxyz1234567890'
lastt=1
admin_id=634288269
password=[]
popol=1
for f in range(1000):
    for n in range(1):
        passwordd =''
        for i in range(6):
            passwordd += random.choice(chars)
        password.append(passwordd)
longpoll = VkBotLongPoll(vk_session,gr_id)
merchant = vkcoin.VKCoin(user_id=admin_id, key="wAg[B*;m1G0s;TTH,A!o5hzF[N3iWS*tD8yjr.20U]YMk.q*AN")
pol=[]
try:
    file=open("priz.txt","r")
    file.close()
except:
    file=open("priz.txt","w")
    file.write("10000")
    file.close()
try:
    file=open("players.txt","r")
    file.close()
except:
    file=open("players.txt","w")
    file.write("0")
    file.close()
try:
    file=open("clickers.txt","r")
    file.close()
except:
    file=open("clickers.txt","w")
    file.write("0")
    file.close()
try:
    file=open("top_balans.txt","r")
    file.close()
except:
    file=open("top_balans.txt","w")
    file.write("Пока тут никого нет!")
    file.close()
try:
    file=open("top_click.txt","r")
    file.close()
except:
    file=open("top_click.txt","w")
    file.write("Пока тут никого нет!")
    file.close()
try:
    file=open("top.txt","r")
    file.close()
except:
    file=open("top.txt","w")
    file.write("Пока тут никого нет!")
    file.close()
try:
    file=open("click.txt","r")
    file.close()
except:
    file=open("click.txt","w")
    file.write("200")
    file.close()
def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    if response == "начать" or response == "назад" or response == "выйти":
        keyboard.add_button("👆 Клик", color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button("👤 Статистика")
        keyboard.add_button("🔥 Реф")
        keyboard.add_button("🏦 Магазин")
        keyboard.add_line()
        keyboard.add_button("💛 Бонус")
        keyboard.add_button("😎 Топы")
        keyboard.add_button("🤭 Отзывы")
        keyboard.add_line()
        keyboard.add_button("🤑 Профиль")
        keyboard.add_button("🔼 Пополнить 🔼")
        keyboard.add_button("🔥 Вывод")
    elif "магазин" in response:
        keyboard.add_button("🖱 Мышка", color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button("🎮 Джойстик", color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button("🖨 Машина", color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button("Назад", color=VkKeyboardColor.NEGATIVE)
    elif "пополнить" in response:
        keyboard.add_button("Проверить", color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button("Назад", color=VkKeyboardColor.NEGATIVE)
    elif response == "админка":
        keyboard.add_button("Выдать баланс", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button("Обнулить баланс", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button("Сброс топа", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button("Обнулить клики", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button("Выйти", color=VkKeyboardColor.NEGATIVE)
    elif "топы" in response:
        keyboard.add_button("Топ баланс", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button("Топ кликов", color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button("Ежедневный топ кликов", color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button("Назад", color=VkKeyboardColor.NEGATIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard
def send_message(peer_id, session_api=session_api, message=None, attachment=None, keyboard=None,
                 payload=None): session_api.messages.send(peer_id=peer_id, message=message,
                                                          random_id=random.randint(-2147483648, +2147483648),
                                                          attachment=attachment, keyboard=keyboard, payload=payload)
while True:
    try:
        for event in longpoll.listen():
            new=time.time()
            vsego=new-lastt
            vsego=round(vsego)
            if vsego >= 1800:
                #топ баланс
                dd=[]
                file=open("top_balans.txt","w")
                file.write("")
                file.close()
                t0p=[]
                d=vk.method("messages.searchConversations",{"group_id" : gr_id,"count": 100})
                items=d["items"]
                for x in items:
                    peer=x["peer"]
                    ids=peer["id"]
                    try:
                        file = open(str(ids)+".txt","r")
                        k=file.read()
                        file.close()
                        k=int(k)
                        t0p.append(k)
                        dd.append(ids)
                    except:
                        continue
                t0p.sort()
                t0p.reverse()
                print(t0p)
                print(dd)
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[0] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("1 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("1. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[1] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("2 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("2. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[2] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("3 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("3. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[3] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("4 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("4. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[4] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("5 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("5. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[5] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("6 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("6. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[6] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("7 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("7. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[7] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("8 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("8. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[8] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("9 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("9. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open(str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[9] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("10 место нашелся")
                            file=open("top_balans.txt","a+")
                            file.write("10. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+" VKCoin\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                file=open("top_balans.txt","r")
                sam_top=file.read()
                file.close()
                #ежед. топ кликов
                dd=[]
                file=open("top.txt","w")
                file.write("")
                file.close()
                t0p=[]
                d=vk.method("messages.searchConversations",{"group_id" : gr_id,"count": 100})
                items=d["items"]
                for x in items:
                    peer=x["peer"]
                    ids=peer["id"]
                    try:
                        file = open("vtop."+str(ids)+".txt","r")
                        k=file.read()
                        file.close()
                        k=int(k)
                        t0p.append(k)
                        dd.append(ids)
                    except:
                        continue
                t0p.sort()
                t0p.reverse()
                print(t0p)
                print(dd)
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[0] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("1 место нашелся")
                            file=open("top.txt","a+")
                            file.write("1. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[1] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("2 место нашелся")
                            file=open("top.txt","a+")
                            file.write("2. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[2] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("3 место нашелся")
                            file=open("top.txt","a+")
                            file.write("3. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[3] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("4 место нашелся")
                            file=open("top.txt","a+")
                            file.write("4. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[4] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("5 место нашелся")
                            file=open("top.txt","a+")
                            file.write("5. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[5] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("6 место нашелся")
                            file=open("top.txt","a+")
                            file.write("6. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[6] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("7 место нашелся")
                            file=open("top.txt","a+")
                            file.write("7. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[7] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("8 место нашелся")
                            file=open("top.txt","a+")
                            file.write("8. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[8] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("9 место нашелся")
                            file=open("top.txt","a+")
                            file.write("9. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("vtop."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[9] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("10 место нашелся")
                            file=open("top.txt","a+")
                            file.write("10. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except:
                    pass
                file=open("top.txt","r")
                sam_top=file.read()
                file.close()
                dd=[]
                file=open("top_click.txt","w")
                file.write("")
                file.close()
                t0p=[]
                d=vk.method("messages.searchConversations",{"group_id" : gr_id,"count": 100})
                items=d["items"]
                for x in items:
                    peer=x["peer"]
                    ids=peer["id"]
                    try:
                        file = open("skok."+str(ids)+".txt","r")
                        k=file.read()
                        file.close()
                        k=int(k)
                        t0p.append(k)
                        dd.append(ids)
                    except:
                        continue
                t0p.sort()
                t0p.reverse()
                print(t0p)
                print(dd)
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[0] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("1 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("1. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[1] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("2 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("2. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(ddхмхз
)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[2] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("3 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("3. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[3] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("4 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("4. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[4] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("5 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("5. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[5] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("6 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("6. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[6] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("7 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("7. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[7] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("8 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("8. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[8] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("9 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("9. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                try:
                    for uf in range(len(dd)):
                        file=open("skok."+str(dd[uf])+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        if t0p[9] == bal:
                            users = vk.method("users.get", {"user_ids": dd[uf]})
                            fullname = users[0]['first_name']
                            print("10 место нашелся")
                            file=open("top_click.txt","a+")
                            file.write("10. @id"+str(dd[uf])+"("+str(fullname)+") - "+str(bal)+"\n")
                            file.close()
                            dd.remove(dd[uf])
                            uf=0
                            break
                except Exception as e:
                    print(e)
                    pass
                file=open("top_click.txt","r")
                sam_top=file.read()
                file.close()
                lastt=time.time()
            if event.obj.ref != None:
                try:
                    file=open("ref"+str(event.obj.peer_id)+".txt","r")
                    file.close()
                    send_message(peer_id=event.obj.peer_id, message="Напишите начать")
                except:
                    if event.obj.from_id == event.obj.ref:
                        send_message(peer_id=event.obj.peer_id, message="Напишите начать")
                    else:
                        file=open(str(event.obj.ref)+".txt","r")
                        bal=file.read()
                        file.close()
                        bal=int(bal)
                        bal=bal+100000
                        bal=str(bal)
                        file=open(str(event.obj.ref)+".txt","w")
                        file.write(bal)
                        file.close()
                        send_message(peer_id=event.obj.ref, message="Вы получили 100000 VKC за приглашенного "+"@id"+str(event.obj.peer_id)+" (игрока)")
                        try:
                            file=open(str(event.obj.peer_id)+".txt","r")
                            bal=file.read()
                            file.close()
                            bal=int(bal)
                            bal=bal+100000
                            bal=str(bal)
                            file=open(str(event.obj.peer_id)+".txt","w")
                            file.write(bal)
                            file.close()
                            send_message(peer_id=event.obj.peer_id, message="Вы получили 100000 VKC за переход по реферальной ссылке "+"@id"+str(event.obj.ref)+" (игрока)")
                            file=open("ref"+str(event.obj.peer_id)+".txt","w")
                            file.write(str(event.obj.ref))
                            file.close()
                            send_message(peer_id=event.obj.peer_id, message="Напишите начать")
                        except:
                            file=open(str(event.obj.peer_id)+".txt","w")
                            file.write("100000")
                            file.close()
                            send_message(peer_id=event.obj.peer_id, message="Вы получили 100000 VKC за переход по реферальной ссылке "+"@id"+str(event.obj.ref)+" (игрока)")
                            file=open("ref"+str(event.obj.peer_id)+".txt","w")
                            file.write(str(event.obj.ref))
                            file.close()
                            send_message(peer_id=event.obj.peer_id, message="Напишите начать")
            elif event.type == VkBotEventType.WALL_REPOST:
                token = "123"
                vk = vk_api.VkApi(token=token)
                vk._auth_token()
                zakrep=vk.method("wall.get",{"owner_id" : mgr_id,"count" : 1})
                items=zakrep["items"]
                items=items[0]
                id_zak=items["id"]
                if id_zak == event.obj.copy_history[0]['id']:
                    if event.obj.from_id in pol:
                        pass
                    else:
                        file = open("vtop."+str(event.obj.from_id)+".txt","r")
                        vtop=file.read()
                        file.close()
                        vtop=int(vtop)
                        if vtop < 300:
                            fd=300-vtop
                            send_message(peer_id=event.obj.from_id, message="Чтобы получить бонус за репост вам надо кликнуть "+str(fd)+" раз")
                        else:
                            file = open("priz.txt","r")
                            priz=file.read()
                            priz=int(priz)
                            file.close()
                            send_message(peer_id=event.obj.from_id, message="Вы получили "+str(priz)+" VKCoin на баланс в боте за репост")
                            file = open(str(event.obj.from_id)+".txt","r")
                            balik=file.read()
                            file.close()
                            balik=int(balik)
                            new=balik+priz
                            new=str(new)
                            file = open(str(event.obj.from_id)+".txt","w")
                            file.write(new)
                            file.close()
                            pol.append(event.obj.from_id)
            elif event.type == VkBotEventType.MESSAGE_NEW:
                response = event.obj.text.lower()
                keyboard = create_keyboard(response)
                if response == "начать" or response == "назад" or response == "выйти":
                    try:
                        file=open(str(event.obj.peer_id)+".txt","r")
                        file.close()
                    except:
                        file=open(str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                    try:
                        file=open("skok."+str(event.obj.peer_id)+".txt","r")
                        file.close()
                    except:
                        file=open("skok."+str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                    try:
                        file=open("vtop."+str(event.obj.peer_id)+".txt","r")
                        file.close()
                    except:
                        file=open("vtop."+str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                    try:
                        file=open("kap."+str(event.obj.peer_id)+".txt","r")
                        file.close()
                    except:
                        file=open("kap."+str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                    try:
                        file=open("click."+str(event.obj.peer_id)+".txt","r")
                        file.close()
                    except:
                        file=open("click."+str(event.obj.peer_id)+".txt","w")
                        file.write("150")
                        file.close()
                        file=open("players.txt","r")
                        players=file.read()
                        file.close()
                        players=int(players)
                        players+=1
                        players=str(players)
                        file=open("players.txt","w")
                        file.write(players)
                        file.close()
                    send_message(peer_id=event.obj.peer_id,message="Меню",keyboard=keyboard)
                elif "магазин" in response:
                    try:
                        file=open("lvl1."+str(event.obj.peer_id)+".txt","r")
                        lvl1=file.read()
                        lvl1=int(lvl1)
                        file.close()
                        file=open("lvl2."+str(event.obj.peer_id)+".txt","r")
                        lvl2=file.read()
                        lvl2=int(lvl2)
                        file.close()
                        file=open("lvl3."+str(event.obj.peer_id)+".txt","r")
                        lvl3=file.read()
                        lvl3=int(lvl3)
                        file.close()
                        lvl1=lvl1*1.5*600000
                        lvl1=round(lvl1)
                        lvl2=lvl2*1.5*1570000
                        lvl2=round(lvl2)
                        lvl3=lvl3*1.5*4400000
                        lvl3=round(lvl3)
                        if lvl1 == 0:
                            send_message(peer_id=event.obj.peer_id,message="🖱 Мышка — добавляет 100 за клик, цена — 600000"
                            +"\n🎮 Джойстик — добавляет 200 за клик, цена — 1570000"
                            +"\n🖨 Машина — добавляет 500 за клик, цена — 4400000",keyboard=keyboard)
                    except:
                        file=open("lvl1."+str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                        file=open("lvl2."+str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                        file=open("lvl3."+str(event.obj.peer_id)+".txt","w")
                        file.write("0")
                        file.close()
                        send_message(peer_id=event.obj.peer_id,message="🖱 Мышка — добавляет 100 за клик, цена — 600000.\n🎮 Джойстик — добавляет 200 за клик, цена — 1570000.\n🖨 Машина — добавляет 500 за клик, цена — 4400000.",keyboard=keyboard)
                elif "репост" in response:
                    if event.obj.peer_id == admin_id:
                        a=list(response)
                        a.pop(0)
                        a.pop(0)
                        a.pop(0)
                        a.pop(0)
                        a.pop(0)
                        a.pop(0)
                        a.pop(0)
                        priz = "".join(a)
                        priz=str(priz)
                        file=open("priz.txt","w")
                        file.write(priz)
                        file.close()
                        pol=[]
                        send_message(peer_id=event.obj.peer_id,message="Успешно! приз: "+str(priz)+" VKCoin")
                elif response == "админка":
                    if event.obj.peer_id == admin_id:
                        send_message(peer_id=event.obj.peer_id, message="Меню",keyboard=keyboard)
                elif response == "выдать баланс":
                    if event.obj.peer_id == admin_id:
                        send_message(peer_id=event.obj.peer_id, message="Используйте: Выдать [сумма]")
                elif "заклик" in response:
                    if event.obj.peer_id == admin_id:
                        a=list(response)
                        for fdsfsdfsd in range(7):
                            a.pop(0)
                        a="".join(a)
                        file=open("click.txt","w")
                        file.write(a)
                        file.close()
                elif "статистика" in response:
                    file=open("players.txt","r")
                    players=file.read()
                    file.close()
                    file=open("clickers.txt","r")
                    clickers=file.read()
                    file.close()
                    send_message(peer_id=event.obj.peer_id,message=
                        "🔥 Статистика :\n"+
                        "✅ Всего кликов : "+clickers+"\n"+
                        "⚡ Игроков : "+players)
                elif "бонус" in response:
                    try:
                        file=open("bonus."+str(event.obj.peer_id)+".txt","r")
                        btime=file.read()
                        file.close()
                        btime=float(btime)
                        stime=time.time()
                        full=stime-btime
                        full=round(full)
                        if full >= 43200:
                            file=open("vtop."+str(event.obj.peer_id)+".txt","r")
                            skoka=file.read()
                            file.close()
                            skoka=int(skoka)
                            if skoka < 70:
                                sf=70-skoka
                                send_message(peer_id=event.obj.peer_id,
                                        message="Чтобы получить бонус вам надо кликнуть "+str(sf)+" раз(а)")
                            else:
                                ran = random.randint(1,50000)
                                send_message(peer_id=event.obj.peer_id,
                                             message="Ты получил "+str(ran)+" VKCoin")
                                file=open(str(event.obj.peer_id)+".txt","r")
                                ballans=file.read()
                                file.close()
                                ballans=int(ballans)
                                y=ballans+ran
                                y=str(y)
                                file=open(str(event.obj.peer_id)+".txt","w")
                                file.write(y)
                                file.close()
                                btime=time.time()
                                btime=str(btime)
                                file=open("bonus."+str(event.obj.peer_id)+".txt","w")
                                file.write(btime)
                                file.close()
                        else:
                            sled=43200-full
                            sled=sled/3600
                            sled=round(sled)
                            send_message(peer_id=event.obj.peer_id,
                                        message="Получить бонус можно через ~"+str(sled)+" часов")
                    except:
                        file=open("vtop."+str(event.obj.peer_id)+".txt","r")
                        skoka=file.read()
                        file.close()
                        skoka=int(skoka)
                        if skoka < 70:
                            sf=70-skoka
                            send_message(peer_id=event.obj.peer_id,
                                    message="Чтобы получить бонус вам надо кликнуть "+str(sf)+" раз(а)")
                        else:
                            file=open("bonus."+str(event.obj.peer_id)+".txt","w")
                            btime=time.time()
                            btime=str(btime)
                            file.write(btime)
                            file.close()
                            ran = random.randint(1,50000)
                            file=open(str(event.obj.peer_id)+".txt","r")
                            ballans=file.read()
                            file.close()
                            ballans=int(ballans)
                            y=ballans+ran
                            y=str(y)
                            file=open(str(event.obj.peer_id)+".txt","w")
                            file.write(y)
                            file.close()
                            send_message(peer_id=event.obj.peer_id,message="Ты получил "+str(ran)+" VKCoin")
                elif "пополнить" in response:
                    send_message(peer_id=event.obj.peer_id,
                                         message="Вот ссылка: https://vk.com/coin#t"+str(admin_id),keyboard=keyboard)
                elif "проверить" in response:
                    a=merchant.get_transactions(tx=[2])
                    last=a[0]
                    id_from_id=last["from_id"]
                    amount=last["amount"]
                    amount=int(amount)
                    popol=int(popol)
                    last2=a[1]
                    id_from=last2["from_id"]
                    amount2=last2["amount"]
                    amount2=int(amount2)
                    if id_from_id == event.obj.peer_id:
                        amount=amount/1000
                        if amount < popol:
                            send_message(peer_id=event.obj.peer_id,
                                         message="Минимально "+str(popol)+" VKCoin!")
                        else:
                            file=open(str(event.obj.peer_id)+".txt","r")
                            x=file.read()
                            file.close()
                            x=int(x)
                            amount=int(amount)
                            amount=round(amount)
                            try:
                                if amount == last_don and last_id == event.obj.peer_id:
                                    send_message(peer_id=event.obj.peer_id,
                                            message="Ошибка! Вы пополнили туже сумму, что и раньше! Попробуйте другую.")
                                else:
                                    y=x+amount
                                    y=str(y)
                                    file=open(str(event.obj.peer_id)+".txt","w")
                                    file.write(y)
                                    file.close()
                                    send_message(peer_id=event.obj.peer_id,
                                                         message="На ваш баланс зачислено "+str(amount)+" VKCoin")
                                    last_don=amount
                                    last_id=event.obj.peer_id
                            except:
                                y=x+amount
                                y=str(y)
                                file=open(str(event.obj.peer_id)+".txt","w")
                                file.write(y)
                                file.close()
                                send_message(peer_id=event.obj.peer_id,
                                                     message="На ваш баланс зачислено "+str(amount)+" VKCoin")
                                last_don=amount
                                last_id=event.obj.peer_id
                    elif id_from == event.obj.peer_id:
                        amount2=amount2/1000
                        if amount2 < popol:
                            send_message(peer_id=event.obj.peer_id,
                                         message="Минимально "+str(popol)+" VKCoin!")
                        else:
                            file=open(str(event.obj.peer_id)+".txt","r")
                            x=file.read()
                            file.close()
                            x=int(x)
                            amount2=int(amount2)
                            amount2=round(amount2)
                            try:
                                if amount2 == last_don2 and last_id2 == event.obj.peer_id:
                                    send_message(peer_id=event.obj.peer_id,
                                            message="Ошибка! Вы пополнили туже сумму, что и раньше! Попробуйте другую.")
                                else:
                                    y=x+amount
                                    y=str(y)
                                    file=open(str(event.obj.peer_id)+".txt","w")
                                    file.write(y)
                                    file.close()
                                    send_message(peer_id=event.obj.peer_id,
                                                         message="На ваш баланс зачислено "+str(amount2)+" VKCoin")
                            except:
                                y=x+amount2
                                y=str(y)
                                file=open(str(event.obj.peer_id)+".txt","w")
                                file.write(y)
                                file.close()
                                send_message(peer_id=event.obj.peer_id,
                                                     message="На ваш баланс зачислено "+str(amount2)+" VKCoin")
                                last_don2=amount2
                                last_id2=event.obj.peer_id
                    else:
                       send_message(peer_id=event.obj.peer_id,
                                         message="Вашего перевода не найдено! Если ошибка, то пишите - vk.com/id"+str(admin_id))
                elif "выдать" in response:
                    if event.obj.peer_id == admin_id:
                        try:
                            a=list(response)
                            for xx in range(7):
                                a.pop(0)
                            a="".join(a)
                            file=open("komy."+str(event.obj.peer_id)+".txt","r")
                            komy=file.read()
                            file.close()
                            file=open(komy+".txt","r")
                            balans=file.read()
                            file.close()
                            balans=int(balans)
                            a=int(a)
                            balans=a+balans
                            balans=str(balans)
                            file=open(komy+".txt","w")
                            file.write(balans)
                            users = vk.method("users.get", {"user_ids": komy,"name_case" : "gen"})
                            fullname = users[0]['first_name'] +  ' ' + users[0]['last_name']
                            send_message(peer_id=event.obj.peer_id, message="Баланс "+fullname+" был пополнен на "+str(a)+" VKC")
                            send_message(peer_id=komy, message="❗ Ваш баланс был пополнен на "+str(a)+" VKC")
                        except Exception as E:
                            print(E)
                            send_message(peer_id=event.obj.peer_id, message="Ошибка! Возможно вы не скинули ссылку на пользователя")
                elif response == "сброс топа":
                    if event.obj.peer_id == admin_id:
                        send_message(peer_id=event.obj.peer_id, message="Начинаю сброс...")
                        d=vk.method("messages.searchConversations",{"group_id" : gr_id,"count": 225})
                        items=d["items"]
                        for x in items:
                            peer=x["peer"]
                            ids=peer["id"]
                            try:
                                file=open("vtop."+str(ids)+".txt","w")
                                file.write("0")
                                file.close()
                            except:
                                continue
                        send_message(peer_id=event.obj.peer_id, message="Топ успешно сброшен!")
                elif response == "обнулить баланс":
                    if event.obj.peer_id == admin_id:
                        try:
                            file=open("komy."+str(event.obj.peer_id)+".txt","r")
                            komy = file.read()
                            file.close()
                            file=open(komy+".txt","w")
                            file.write("0")
                            file.close()
                            users = vk.method("users.get", {"user_ids": komy,"name_case" : "gen"})
                            fullname = users[0]['first_name'] +  ' ' + users[0]['last_name']
                            send_message(peer_id=event.obj.peer_id, message="Баланс "+fullname+" был обнулен")
                        except Exception as e:
                            print(e)
                            send_message(peer_id=event.obj.peer_id, message="Произошла ошибка, возможно вы не скинули ссылку на пользователя боту")
                elif "https" in response:
                    if event.obj.peer_id == admin_id:
                        a=list(response)
                        for xf in range(15):
                            a.pop(0)
                        egos="".join(a)
                        ego=vk.method("utils.resolveScreenName",{"screen_name" : egos})
                        ego=ego["object_id"]
                        file=open("komy."+str(event.obj.peer_id)+".txt","w")
                        ego=str(ego)
                        file.write(ego)
                        file.close()
                        users = vk.method("users.get", {"user_ids": ego,"name_case" : "dat"})
                        fullname = users[0]['first_name'] +  ' ' + users[0]['last_name']
                        send_message(peer_id = event.obj.peer_id,
                                         message="Отлично! Теперь напиши что сделать"+" @id"+str(ego)+" ("+fullname+")")
                elif "vk.com" in response and not "https" in response:
                    if event.obj.peer_id == admin_id:
                        a=list(response)
                        for xf in range(7):
                            a.pop(0)
                        egos="".join(a)
                        ego=vk.method("utils.resolveScreenName",{"screen_name" : egos})
                        ego=ego["object_id"]
                        file=open("komy."+str(event.obj.peer_id)+".txt","w")
                        ego=str(ego)
                        file.write(ego)
                        file.close()
                        users = vk.method("users.get", {"user_ids": ego,"name_case" : "dat"})
                        fullname = users[0]['first_name'] +  ' ' + users[0]['last_name']
                        send_message(peer_id = event.obj.peer_id,
                                         message="Отлично! Теперь напиши что сделать"+" @id"+str(ego)+" ("+fullname+")")
                elif "мышка" in response:
                    file=open("lvl1."+str(event.obj.peer_id)+".txt","r")
                    lvl1=file.read()
                    file.close()
                    lvl1=int(lvl1)
                    if lvl1 == 0:
                        price = 600000
                    else:
                        price = lvl1*1.5*600000
                    price=round(price)
                    file=open(str(event.obj.peer_id)+".txt","r")
                    bal=file.read()
                    file.close()
                    bal=int(bal)
                    if bal <= 0 or bal < price:
                        send_message(peer_id=event.obj.peer_id,message="Недостаточно VKC для покупки")
                    else:
                        bal=bal-price
                        bal=str(bal)
                        file=open(str(event.obj.peer_id)+".txt","w")
                        file.write(bal)
                        file.close()
                        file=open("click."+str(event.obj.peer_id)+".txt","r")
                        clicks=file.read()
                        file.close()
                        clicks=int(clicks)
                        clicks=clicks+100
                        clicks=str(clicks)
                        file=open("click."+str(event.obj.peer_id)+".txt","w")
                        file.write(clicks)
                        file.close()
                        file=open("lvl1."+str(event.obj.peer_id)+".txt","r")
                        lvl1=file.read()
                        file.close()
                        lvl1=int(lvl1)
                        lvl1+=1
                        lvl1=str(lvl1)
                        file=open("lvl1."+str(event.obj.peer_id)+".txt","w")
                        file.write(lvl1)
                        file.close()
                        send_message(peer_id=event.obj.peer_id,message="Вы купили мышку")
                elif "джойстик" in response:
                    file=open("lvl1."+str(event.obj.peer_id)+".txt","r")
                    lvl1=file.read()
                    file.close()
                    lvl1=int(lvl1)
                    if lvl1 == 0:
                        price = 1570000
                    else:
                        price = lvl1*1.5*1570000
                    price=round(price)
                    file=open(str(event.obj.peer_id)+".txt","r")
                    bal=file.read()
                    file.close()
                    bal=int(bal)
                    if bal <= 0 or bal < price:
                        send_message(peer_id=event.obj.peer_id,message="Недостаточно VKC для покупки")
                    else:
                        bal=bal-price
                        bal=str(bal)
                        file=open(str(event.obj.peer_id)+".txt","w")
                        file.write(bal)
                        file.close()
                        file=open("click."+str(event.obj.peer_id)+".txt","r")
                        clicks=file.read()
                        file.close()
                        clicks=int(clicks)
                        clicks=clicks+200
                        clicks=str(clicks)
                        file=open("click."+str(event.obj.peer_id)+".txt","w")
                        file.write(clicks)
                        file.close()
                        file=open("lvl2."+str(event.obj.peer_id)+".txt","r")
                        lvl2=file.read()
                        file.close()
                        lvl2=int(lvl2)
                        lvl2+=1
                        lvl2=str(lvl2)
                        file=open("lvl2."+str(event.obj.peer_id)+".txt","w")
                        file.write(lvl2)
                        file.close()
                        send_message(peer_id=event.obj.peer_id,message="Вы купили джойстик")
                elif response == "обнулить клики":
                    if event.obj.peer_id == admin_id:
                        try:
                            a=list(response)
                            for xx in range(7):
                                a.pop(0)
                            a="".join(a)
                            file=open("komy."+str(event.obj.peer_id)+".txt","r")
                            komy=file.read()
                            file.close()
                            file=open("click."+komy+".txt","w")
                            file.write("150")
                            file.close()
                            users = vk.method("users.get", {"user_ids": komy,"name_case" : "gen"})
                            fullname = users[0]['first_name'] +  ' ' + users[0]['last_name']
                            send_message(peer_id=event.obj.peer_id, message="Баланс "+fullname+" был пополнен на "+str(a)+" VKC")
                        except Exception as E:
                            print(E)
                            send_message(peer_id=event.obj.peer_id, message="Ошибка! Возможно вы не скинули ссылку на пользователя")
                elif "машина" in response:
                    file=open("lvl1."+str(event.obj.peer_id)+".txt","r")
                    lvl1=file.read()
                    file.close()
                    lvl1=int(lvl1)
                    if lvl1 == 0:
                        price = 4400000
                    else:
                        price = lvl1*1.5*4400000
                    price=round(price)
                    file=open(str(event.obj.peer_id)+".txt","r")
                    bal=file.read()
                    file.close()
                    bal=int(bal)
                    if bal <= 0 or bal < price:
                        send_message(peer_id=event.obj.peer_id,message="Недостаточно VKC для покупки")
                    else:
                        bal=bal-price
                        bal=str(bal)
                        file=open(str(event.obj.peer_id)+".txt","w")
                        file.write(bal)
                        file.close()
                        file=open("click."+str(event.obj.peer_id)+".txt","r")
                        clicks=file.read()
                        file.close()
                        clicks=int(clicks)
                        clicks=clicks+500
                        clicks=str(clicks)
                        file=open("click."+str(event.obj.peer_id)+".txt","w")
                        file.write(clicks)
                        file.close()
                        file=open("lvl3."+str(event.obj.peer_id)+".txt","r")
                        lvl1=file.read()
                        file.close()
                        lvl3=int(lvl3)
                        lvl3+=1
                        lvl3=str(lvl3)
                        file=open("lvl3."+str(event.obj.peer_id)+".txt","w")
                        file.write(lvl3)
                        file.close()
                        send_message(peer_id=event.obj.peer_id,message="Вы купили машину")
                elif "отзывы" in response:
                    send_message(peer_id=event.obj.peer_id,message=
                    "😕 Ты что сомневаешься в нашей прозрачности\n"+
                    "🔥 Ссылка — https://vk.com/topic-198478017_45190794 \n"+
                    "🤭Так же видел отчёт — https://vk.com/topic-198478017_45191457")
                elif "вывод" in response:
                    file=open(str(event.obj.peer_id)+".txt","r")
                    balans=file.read()
                    file.close()
                    balans=int(balans)
                    if balans <= 0:
                        send_message(peer_id=event.obj.peer_id,message="У вас нету VKCoin")
                    else:
                        try:
                            merchant.send_payment(event.obj.peer_id, balans*1000)
                            file=open(str(event.obj.peer_id)+".txt","w")
                            file.write("0")
                            file.close()
                            user = vk.method("users.get", {"user_ids": event.obj.peer_id})
                            fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
                            send_message(peer_id=event.obj.peer_id,message="Мы отправили вам "+str(balans)+" VKC. Не забудьте оставить отзыв https://vk.com/topic-198478017_45190794")
                            #vk.method("board.createComment",{"group_id" : gr_id,"topic_id" : 45212154,"from_group" : 1,"message" : "@id"+str(event.obj.peer_id)+" ("+fullname+") вывел"+str(balans)+" VKCoin"})
                            #send_message(peer_id=2000000028,message="👤 Юзер — @id"+str(event.obj.peer_id)+" ("+fullname+")\n"
                            #+"✅ Сумма вывода — "+str(balans)+" VKCoin\n")
                        except Exception as E:
                            print(E)
                            send_message(peer_id=event.obj.peer_id,message="На балансе бота недостаточно средств. Ждите пополнения")
                elif response == "топ баланс":
                    file=open("top_balans.txt","r")
                    top=file.read()
                    file.close()
                    send_message(peer_id=event.obj.peer_id,message=top)
                elif "реф" in response:
                    cc=vk.method("utils.getShortLink",{"url" : "https://vk.me/public"+str(gr_id)+"?ref="+str(event.obj.peer_id)})
                    cc=cc["short_url"]
                    send_message(peer_id=event.obj.peer_id,message="🔥 100 000 — за друга, так же 10% от клика.\n"
                                 +"✅ Ваша реферальная ссылка — "+cc)
                elif response == "топ кликов":
                    file=open("top_click.txt","r")
                    top=file.read()
                    file.close()
                    send_message(peer_id=event.obj.peer_id,message=top)
                elif response == "ежедневный топ кликов":
                    file=open("top.txt","r")
                    top=file.read()
                    file.close()
                    send_message(peer_id=event.obj.peer_id,message=top)
                elif "топы" in response:
                    send_message(peer_id=event.obj.peer_id,message="Выбирай топ. Обновление топа раз в 30 минут",keyboard=keyboard)
                elif "профиль" in response:
                    file=open(str(event.obj.peer_id)+".txt","r")
                    balans=file.read()
                    file.close()
                    file=open("skok."+str(event.obj.peer_id)+".txt","r")
                    skok=file.read()
                    file.close()
                    file=open("vtop."+str(event.obj.peer_id)+".txt","r")
                    vtop=file.read()
                    file.close()
                    send_message(peer_id=event.obj.peer_id,message=
                    "Ваш баланс: "+balans+" VKC\n"+
                    "Всего кликов: "+skok+"\n"+
                    "Сегодня кликов: "+vtop)
                elif "клик" in response:
                    file=open("kap."+str(event.obj.peer_id)+".txt","r")
                    kap=file.read()
                    file.close()
                    kap=int(kap)
                    if kap >= 60:
                        ran=random.choice(password)
                        print(ran)
                        send_message(peer_id=event.obj.peer_id,message="Чтобы продолжить кликать, напишите: "+ran)
                    else:
                        file=open("kap."+str(event.obj.peer_id)+".txt","w")
                        kap+=1
                        kap=str(kap)
                        file.write(kap)
                        file=open(str(event.obj.peer_id)+".txt","r")
                        balans=file.read()
                        file.close()
                        balans=int(balans)
                        file=open("click."+str(event.obj.peer_id)+".txt","r")
                        click=file.read()
                        file.close()
                        click=int(click)
                        file=open("click.txt","r")
                        bon=file.read()
                        file.close()
                        bon=int(bon)
                        xf=click+bon
                        balans=balans+click+bon
                        balans=str(balans)
                        file=open(str(event.obj.peer_id)+".txt","w")
                        file.write(balans)
                        file=open("skok."+str(event.obj.peer_id)+".txt","r")
                        skok=file.read()
                        file.close()
                        skok=int(skok)
                        skok+=1
                        skok=str(skok)
                        file=open("skok."+str(event.obj.peer_id)+".txt","w")
                        file.write(skok)
                        file=open("vtop."+str(event.obj.peer_id)+".txt","r")
                        vtop=file.read()
                        file.close()
                        vtop=int(vtop)
                        vtop+=1
                        vtop=str(vtop)
                        file=open("vtop."+str(event.obj.peer_id)+".txt","w")
                        file.write(vtop)
                        file.close()
                        file=open("clickers.txt","r")
                        clickers=file.read()
                        file.close()
                        clickers=int(clickers)
                        clickers+=1
                        clickers=str(clickers)
                        file=open("clickers.txt","w")
                        file.write(clickers)
                        file.close()
                        try:
                            file=open("ref"+str(event.obj.peer_id)+".txt","r")
                            referal=file.read()
                            file.close()
                            file=open(referal+".txt","r")
                            balans=file.read()
                            file.close()
                            balans=int(balans)
                            pr=xf/10
                            pr=round(pr)
                            balans=balans+pr
                            balans=str(balans)
                            file=open(referal+".txt","w")
                            file.write(balans)
                            file.close()
                        except:
                            pass
                        send_message(peer_id=event.obj.peer_id,message="Вы кликнули и получили "+str(xf)+" VKC")
                elif response in password:
                    file=open("kap."+str(event.obj.peer_id)+".txt","w")
                    file.write("0")
                    file.close()
                    send_message(peer_id=event.obj.peer_id,message="Вы написали капчу и можете дальше кликать")
    except Exception as Y:
        print(Y)
