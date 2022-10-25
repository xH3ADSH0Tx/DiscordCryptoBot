from logging import fatal
import discord
from pycoingecko import CoinGeckoAPI
import os

client = discord.Client()
cg = CoinGeckoAPI()

coinIdDict = {
    'Bitcoin' : 'bitcoin',
    'Ethereum' : 'ethereum',
    'Litecoin' : 'litecoin',
    'Dogecoin' : 'dogecoin',
    'Bitcoin Cash' : 'bitcoin-cash',
    'Cardano' : 'cardano',
    'Matic Network' : 'matic-network',
    'Decentraland [MANA]' : 'decentraland',
    'Gala' : 'gala',
    'MBOX' : 'mobox',
    'Avalanche': 'avalanche-2',
    'Polkadot' : 'polkadot',
    'Solana' : 'solana',
    'Terra Luna' : 'terra-luna',
    'Basic Attention Token' : 'bat',
}

fiatIdDict = {
    'US Dollars' : 'usd',
    'Indian Rupees' : 'inr',
    'Euro' : 'eur',
    'British Pound' : 'gbp',
    'Japanese Yen' : 'jpy',
    'Canadian Dollar' : 'cad',
    'Australian Dollar' : 'aud'
}

fiatSymbolDict = {
    'usd' : '$',
}

def getPrice(cryptoId, fiatId):
    return cg.get_price(ids=cryptoId, vs_currencies=fiatId)


def displayCoinList():
    str = ''
    for coin in coinIdDict:
        str += f'🆔: {coinIdDict[coin]} -> {coin}\n\n'
    
    return str

def displayFiatList():
    str = ''
    for fiat in fiatIdDict:
        str += f'🆔: {fiatIdDict[fiat]} -> {fiat} ({fiatSymbolDict[fiatIdDict[fiat]]})\n\n'
    
    return str

def getCommandList():
    return """.commands -> Get the list of commands
.coinList -> Get the list of supported Cryptocurrencies and their code 🪙
.fiatList -> Get the list of supported Fiat Currencies and their code 💵
.getPrice <cryptoId> <fiatId> -> Get the current price of Cryptocurrencies in the mentioned Fiat Currency. 🪙 ➡️ 💵
NOTE: 
    Please mention the crypto currencies and Fiat currency with their respective ids. You can find the Id using .coinList and .fiatList commands
    While specifing multiple currencies, give the ids using commands and without space. 
    Eg: bitcoin,ethereum,dogecoin and not as bitcoin, ethereum, dogecoin
Support the Project on Github:
https://github.com/srivathsanvenkateswaran/Crypto-Discord-Bot
    
    """

def parsePriceJson(priceJson, fiat):
    str = ''
        
    for coin in priceJson:
        str += '{} -> '.format(coin.capitalize())
        for fiat in priceJson[coin]:
            str += '\n\t\t{} {:,.2f}'.format(fiatSymbolDict[fiat], priceJson[coin][fiat])
        str += '\n\n'
    
    return str

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('.coinList'):
        await message.channel.send(displayCoinList())
    if message.content.startswith('.fiatList'):
        await message.channel.send(displayFiatList())
    if message.content.startswith('.commands'):
        await message.channel.send(getCommandList())
    if message.content.startswith('.getPrice'):
        contents = message.content.strip()
        contents = contents.split(' ')

        crypto = contents[-2].strip()
        fiat = contents[-1].strip()

        await message.channel.send(parsePriceJson(getPrice(crypto, fiat), fiat))        

CRYPTO_BOT_TOKEN = os.environ.get('MTAzNDQ2NzUyNTAxNjE2NjQ2Mg.GzwoAX.bZRc1rA5tGJPnVAw8gmps7EX7xNRb3T9JOuW0I')
client.run(CRYPTO_BOT_TOKEN)

'https://discord.com/api/oauth2/authorize?client_id=1034467525016166462&permissions=8&scope=bot'


'MTAzNDQ2NzUyNTAxNjE2NjQ2Mg.GzwoAX.bZRc1rA5tGJPnVAw8gmps7EX7xNRb3T9JOuW0I'
