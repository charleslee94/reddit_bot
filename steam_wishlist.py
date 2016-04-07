from lxml import html
import requests

def get_steam_wishlist(steam_id):
    """ 
    param: steam_id id of steam user you want to have the wishlist of
    return: list of games in steam_id's user wishlist
    """
    url =  'http://steamcommunity.com/id/{}/wishlist'.format(steam_id)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    games = tree.xpath('//h4[@class="ellipsis"]/text()')
    return games

