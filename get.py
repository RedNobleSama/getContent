import requests


class GetByCDN:
    def __init__(self):
        self.uri = "https://cdn.xcx.huochaibox.com/"

    def getdata(self, units: list) -> list:
        data = []
        for i in units:
            if i["type"] == 1:
                res = self.uri + i['uri']
                data.append(res)
            else:
                res = requests.get(self.uri + i['uri'])
                data.append(res.text)
        return data

    def download_pic(self, img_url):
        hr = requests.get(img_url, stream=True)
        path = "pic/1.jpg"
        if hr.status_code == 200:
            open('pic/1.jpg', 'wb').write(hr.content)  # 将内容写入图片
        del hr
        return path

# cdn = GetByCDN()
# cdn.getdata()
