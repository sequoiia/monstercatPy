import tools

def main():
    conf = tools.Conf()
    print "Input cookie"
    conf.cookie = raw_input()

    print "Input save location path"
    conf.dlpath = raw_input()

    releases = tools.getReleases()

    downloader = tools.MonstercatDownloader()
    downloader.init(conf)

    counter = 0
    itemscount = len(releases["results"])

    for release in releases["results"]:
        releaseid = release["_id"]
        filename = downloader.download(releaseid)
        counter = counter + 1
        print '{}/{} - {} downloaded'.format(counter, itemscount, filename)

main()
