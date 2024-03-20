import requests

# url = f'https://api-mifit-cn.huami.com/v1/data/band_data.json?&t={t}'
# head = {
#     "apptoken": app_token,
#     "Content-Type": "application/x-www-form-urlencoded"
# }
#
# data = f'userid={userid}&last_sync_data_time=1597306380&device_type=0&last_deviceid=DA932FFFFE8816E7&data_json={data_json}'

# response = requests.post(url, data=data, headers=head).json()

qqtalk = 'https://qmsg.zendee.cn/send/e6b0c2a37b9836dc40912ccd583618c7?msg=' + "修改步数："  + '&qq=*'
requests.get(qqtalk)
