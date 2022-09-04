from vkbottle.bot import Bot, Message
from vkbottle.keyboard import Keyboard, Text
import random as r
import config
import json

token = config.token
id = config.id
merchant = config.merchant_key
group_id = config.group_id

from vkcoinapi import *
coin = VKCoin(key = merchant, merchantId = id)

bot = Bot(token)

ad = ["\n\n🌿 Hello, хочешь чтобы тут был твой текст? пиши сюда @roman870"]

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = "0"
        data[ "replenish" ][ str( ans.from_id ) ] = "0"
        data[ "received" ][ str( ans.from_id ) ] = "0"
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

main = Keyboard()
main.add_row()
main.add_button( Text( label = "🌀 Клик" ), color = "primary" )
main.add_row()
main.add_button( Text( label = "🙍‍♂ Профиль" ), color = "positive" )
main.add_row()
main.add_button( Text( label = "💰 Баланс" ), color = "default" )
main.add_button( Text( label = "🤑 Вывод" ), color = "default" )

@bot.on.message( text = [ "Начать","Меню" ], lower = True )
async def wrapper( ans: Message ):
    reg( ans )
    await ans( f"🌿 Приветсвую в меню [public{group_id}|бота]\n\n🥺 Реклама: {r.choice(ad)}", keyboard = main )
    
@bot.on.message( text = [ "🌀 Клик","Клик" ], lower = True )
async def wrapper( ans: Message ):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    await ans( f"🌀 Вы кликнули и получили {data[ 'for_click' ]} VKcoin\n\n🥺 Реклама: {r.choice(ad)}", keyboard = main )
    data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int( data[ "for_click" ] )
    data[ "received" ][ str( ans.from_id ) ] = int( data[ "received" ][ str( ans.from_id ) ] ) + int( data[ "for_click" ] )
    json.dump( data, open( "data.json", "w" ) )
    
@bot.on.message( text = [ "🙍‍♂ Профиль","Профиль" ], lower = True )
async def wrapper( ans: Message ):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    await ans( f"""💰 Ваш баланс - {data['balance'][str(ans.from_id)]} VKcoin
 
🤑 Вы вывели - {data['replenish'][ str( ans.from_id ) ]} VKcoin
 
💸 Вы накликали - {data['received'][ str( ans.from_id ) ]} VKcoin

🆔 Ваш игровой ID - {data['id'][ str( ans.from_id ) ]}\n\n🥺 Реклама: {r.choice(ad)}""", keyboard = main )

@bot.on.message( text = [ "💰 Баланс","Баланс" ], lower = True )
async def wrapper( ans: Message ):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    await ans( f"💸 Ваш баланс - {data[ 'balance' ][ str( ans.from_id ) ]}" )
    
@bot.on.message( text = [ "🤑 Вывод","Вывод" ], lower = True ) 
async def wrapper( ans: Message ):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    if str( ans.from_id ) in data[ "user" ]:
        if data[ "balance" ][ str( ans.from_id ) ] != "0":
            bot_balance = coin.getBalance()[ "response" ]
            for i in bot_balance:
                if int( bot_balance[ i ] ) < int( int( data[ "balance" ][ str( ans.from_id ) ] ) * 1000 ):
                    await ans( f"""😔 Извините, но на нашем балансе недостаточно средств для вывода, попробуйте снова позже.
                    
🥺 Реклама: {r.choice(ad)}""", keyboard = main )
                else:
                    coin.sendPayment( ans.from_id, int( data[ 'balance' ][ str( ans.from_id ) ] ) * 1000 )
                    await ans( f"""💸 Выведено {data['balance'][ str( ans.from_id ) ] } VKcoin
                    
🥺 Реклама: {r.choice(ad)}""", keyboard = main )
                    data[ "replenish" ][ str( ans.from_id ) ] = int( data[ "replenish" ][ str( ans.from_id ) ] ) + int( data[ "balance" ][ str( ans.from_id ) ] )
                    data[ "balance" ][ str( ans.from_id ) ] = "0"
                    json.dump( data, open( "data.json", "w" ) )
        else:
            await ans( f"💸 Ваш баланс - 0 VKcoin\n\n🥺 Реклама: {r.choice(ad)}", keyboard = main )
    
@bot.on.message( text = "/click <for_click>", lower = True )
async def wrapper( ans: Message, for_click):
	data = json.load( open( "data.json", "r" ) )
	if str( ans.from_id ) in data[ "admins" ]:
		data[ "for_click" ] = int( for_click )
		json.dump( data, open( "data.json", "w" ) )
		await ans( f"💸 Теперь клик - {for_click}" )

bot.run_polling( skip_updates = False )
