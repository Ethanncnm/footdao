# -*- encoding: utf-8 -*-"
# @Module  : discord bot
# @Time    : 2022/4/25 13:38
# @Author  : 0xgtr.eth
# @Version : 1.0
# @Contact : bibi45gt@gmail.com
# @License : (C)Copyright 2018-2022, 0xgtr.eth
# That’s weird… It worked yesterday.
import requests
import json
import random
import time

# 填写随机发送的语句
context_list = ["牛逼", "666"]

# 填写要聊天的channel id
channel_list = ['']  # 看web discord 频道url   多个频道 ["channel_id_1", "channel_id_2"]
# 填写用户的token
authorization_list = ['']  # f12抓包 找包名为 science   authorization在Request Headers里面   多个号 ["auth_a", "auth_b"]

# 随机休眠时间 random.randrange(60, 80): 休眠60~80s
sleep_gap = random.randrange(60, 80)


# 随机读取语句 后续可以改成随机从频道中复制一句
def gen_context():
    text = random.choice(context_list)
    return text


def get_context():
    headr = {
        "Authorization": "",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = random.choice(channel_list)
    url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    res = requests.get(url=url, headers=headr)
    result = json.loads(res.content)
    result_list = []
    for context in result:
        if ('<') not in context['content']:
            if ('@') not in context['content']:
                if ('http') not in context['content']:
                    if ('?') not in context['content']:
                        result_list.append(context['content'])

    return random.choice(result_list)


def chat(channel_list, authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        for channel_id in channel_list:
            msg = {

                # "content": get_context(),
                "content": gen_context(),
                "nonce": "964403{}".format(random.randrange(0, 991129047040)),
                "tts": False

            }
            url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg))
                print(res.content)
            except:
                pass
            continue
        time.sleep(sleep_gap)


if __name__ == '__main__':
    while True:
        try:
            chat(channel_list, authorization_list)
            sleeptime = random.randrange(63, 70)
            time.sleep(sleeptime)
        except Exception as e:
            print(e)
            pass
        continue
