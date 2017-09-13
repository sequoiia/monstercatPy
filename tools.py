import requests, re

def getReleases():
    r = requests.get('https://connect.monstercat.com/api/catalog/release?fields=_id')
    return r.json()

class Conf(object):
    cookie = ""
    dlpath = "."

class MonstercatDownloader(object):
    conf = Conf()

    def init(self, conf):
        self.conf = conf
    
    def download(self, releaseid):
        req = requests.Request('GET', 'https://connect.monstercat.com/api/release/{}/download?method=download&type=mp3_320'.format(releaseid))

        s = requests.session()
        s.cookies.set('connect.sid', self.conf.cookie, domain='connect.monstercat.com', path='/')
        req = s.prepare_request(req)
        resp = s.send(req, stream=True)

        d = resp.headers['Content-Disposition']
        filename = re.findall("filename=(.+)", d)
        filename = filename[0]
        filename = filename[1:]
        filename = filename[:-1]

        with open('{}/{}'.format(self.conf.dlpath, filename), 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        
        return filename
