def init_pixivutil2():
    import PixivUtil2
    import PixivDBManager
    import PixivHelper
    import PixivBrowserFactory
    try:
        PixivUtil2.__config__.loadConfig(path=PixivUtil2.configfile)
        PixivHelper.setConfig(PixivUtil2.__config__)
    except BaseException:
        print('Failed to read configuration.')
        log.exception('Failed to read configuration.')
    if PixivUtil2.__br__ is None:
        PixivUtil2.__br__ = PixivBrowserFactory.getBrowser(config=PixivUtil2.__config__)
    PixivUtil2.__dbManager__ = PixivDBManager.PixivDBManager(
        target=PixivUtil2.__config__.dbPath, config=PixivUtil2.__config__)
    PixivUtil2.__dbManager__.createDatabase()
    username = PixivUtil2.__config__.username
    password = PixivUtil2.__config__.password
    PixivUtil2.doLogin(password, username)
    PixivUtil2.start_iv = False
    return PixivUtil2


def process_image_ids(image_ids):
    pu2 = init_pixivutil2()
    __import__('pdb').set_trace()
    for image_id in image_ids:
        pu2.process_image(image_id=int(image_id))
