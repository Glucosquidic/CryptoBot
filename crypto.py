import discord



def crypto_message(data, coin):
    message = discord.Embed(title = f'Current Price in USD for {coin.upper()} is ${data}', description = 'Do you hold, sell, or buy more?', color = 0xfb8500)
    return message


def error_message(coin):
    coin = coin.title()
    return discord.Embed(
    title = 'Error',
    description = f'Oh no! Try again. There was an error receiving the current price for the {coin} coin. Try again by typing the abbreviation in all caps.',
    color = 0xe63946
    )
