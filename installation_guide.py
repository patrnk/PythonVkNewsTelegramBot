from os import environ
from sys import exit
import requests


def is_vk_api_app_id_known():
    return environ.get('VK_API_APP_ID') is not None


def ask_user_for_vk_api_app_id():
    print('Create a standalone app here: https://vk.com/editapp?act=create '
          'and assign its app id to VK_API_APP_ID environmental variable.')


def is_vk_access_token_known():
    return environ.get('VK_ACCESS_TOKEN') is not None


def form_vk_user_authorization_url():
    params = {'client_id': environ['VK_API_APP_ID'],
              'scope': 'offline',
              'redirect_uri': 'https://oauth.vk.com/blank.html',
              'display': 'page',
              'v': '5.62',
              'response_type': 'token'
              }
    request = requests.Request('GET', 'https://oauth.vk.com/authorize', params=params)
    return request.prepare().url


def ask_user_for_vk_access_token():
    print('Follow the link below. Authorize your application to use '
          'your VK profile. After that, copy from address bar everything between '
          '"access_token=" and "&" symbol and assign it to VK_ACCESS_TOKEN '
          'environmental variable.')
    print('The link:')
    print(form_vk_user_authorization_url())


def is_telegram_bot_token_known():
    return environ.get('TELEGRAM_BOT_TOKEN') is not None


def ask_user_for_telegram_bot_token():
    print('Write to @BotFather and create your Telegram bot. '
          'More on that: https://core.telegram.org/bots#6-botfather')


if __name__ == '__main__':
    if not is_vk_api_app_id_known():
        print('Step 1:')
        ask_user_for_vk_api_app_id()
        exit()
    if not is_vk_access_token_known():
        print('Step 2:')
        ask_user_for_vk_access_token()
        exit()
    if not is_telegram_bot_token_known():
        print('Step 3:')
        ask_user_for_telegram_bot_token()
        exit()
    print('Congratulations! Everything we need is set up.')
