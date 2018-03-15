Code Notes
==========

Process Image ids
-----------------

.. code:: python

  from pixiv_util2.api import process_image_ids
  process_image_ids([67745033])

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivUtil2.py#L594

.. code:: python

  ...
  referer = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(image_id)

  try:
      filename = 'N/A'
      print('Processing Image Id:', image_id)

      # __config__  # <PixivConfig.PixivConfig object at 0x7f17edc456d8>
      # vars(__config__)
      # {'IrfanViewPath': 'C:\\Program Files\\IrfanView',
      #  'alwaysCheckFileSize': False,
      #  'avatarNameFormat': '',
      #  'backupOldFile': False,
      #  'checkUpdatedLimit': 0,
      #  'configFileLocation': 'config.ini',
      #  'cookie': '2544445_29e964626327235c17fa25c4fa2c242c',
      #  'createApng': False,
      #  'createDownloadLists': False,
      #  'createGif': False,
      #  'createMangaDir': False,
      #  'createUgoira': False,
      #  'createWebm': False,
      #  'dateDiff': 0,
      #  'dateFormat': '',
      #  'dayLastUpdated': 7,
      #  'dbPath': '',
      #  'debugHttp': False,
      #  'deleteUgoira': False,
      #  'deleteZipFile': False,
      #  'downloadAvatar': True,
      #  'downloadDelay': 2,
      #  'downloadListDirectory': '.',
      #  'dumpMediumPage': False,
      #  'dumpTagSearchPage': False,
      #  'enableDump': True,
      #  'enableInfiniteLoop': False,
      #  'ffmpeg': 'ffmpeg',
      #  'ffmpegCodec': 'libvpx-vp9',
      #  'ffmpegParam': '-lossless 1',
      #  'filenameFormat': '%artist% (%member_id%)/%urlFilename% - %title%',
      #  'filenameInfoFormat': '%artist% (%member_id%)/%urlFilename% - %title%',
      #  'filenameMangaFormat': '%artist% (%member_id%)/%urlFilename% - %title%',
      #  'keepSignedIn': 1,
      #  'logLevel': 'DEBUG',
      #  'numberOfPage': 0,
      #  'overwrite': False,
      #  'password': 'movemaker',
      #  'processFromDb': True,
      #  'proxy': {'http': '', 'https': ''},
      #  'proxyAddress': '',
      #  'r18mode': False,
      #  'retry': 3,
      #  'retryWait': 5,
      #  'rootDirectory': '.',
      #  'setLastModified': True,
      #  'skipDumpFilter': '',
      #  'startIrfanSlide': False,
      #  'startIrfanView': False,
      #  'tagsLimit': -1,
      #  'tagsSeparator': ',',
      #  'timeout': 60,
      #  'urlBlacklistRegex': '',
      #  'urlDumpFilename': 'url_list_%Y%m%d',
      #  'useBlacklistMembers': False,
      #  'useBlacklistTags': False,
      #  'useList': False,
      #  'useProxy': False,
      #  'useRobots': True,
      #  'useSuppressTags': False,
      #  'useTagsAsDir': False,
      #  'useragent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
      #  'username': 'foreturiga',
      #  'verifyImage': False,
      #  'writeImageInfo': False,
      #  'writeImageJSON': False,
      #  'writeUgoiraInfo': False,
      #  'writeUrlInDescription': False}

      # check if already downloaded. images won't be downloaded twice - needed in process_image to catch any download
      r = __dbManager__.selectImageByImageId(image_id)
      # r  # None
      if r is not None and not __config__.alwaysCheckFileSize:
          if not __config__.overwrite:
             ...

      # get the medium page
      try:
          # image_id  # 67745033
          # artist  # None
          # bookmark  # False
          # bookmark_count  # -1
          (image, parse_medium_page) = PixivBrowserFactory.getBrowser().getImagePage(
          image_id=image_id, parent=artist, from_bookmark=bookmark, bookmark_count=bookmark_count) 
          # pp vars(image)
          # {'artist': <PixivModel.PixivArtist object at 0x7f17d8767439>,
          #  'bookmark_count': -1,
          #  'dateFormat': '',
          #  'descriptionUrlList': [],
          #  'fromBookmark': False,
          #  'imageCaption': 'This very young space explorer has brought this creature back from one of her expeditions. Unlike what one might think the creature is absolutely '
          #                  'not aggressive: quite the opposite !!\n'
          #                  'Telepathically she persuades girls to * with her. She is tireless and provides hours of * delirium to her happy partner.',
          #  'imageCount': 1,
          #  'imageId': 67745033,
          #  'imageMode': 'bigNew',
          #  'imageTitle': 'pixiv',
          #  'imageUrls': ['https://i.pximg.net/img-original/img/2018/03/15/17/28/24/67745033_p0.jpg'],
          #  'jd_rtc': 6,
          #  'jd_rtv': 108,
          #  'originalArtist': <PixivModel.PixivArtist object at 0x7f17d8767438>,
          #  'worksDate': '3/15/2018 17:28',
          #  'worksDateDateTime': datetime.datetime(2018, 3, 15, 17, 28),
          #  'worksResolution': '2000x1686'}
          # pp vars(image.artist)
          # {'artistAvatar': 'https://i.pximg.net/user-profile/img/2017/07/03/21/05/13/12800072_532e5499464b1dd2bfc4b46440c762c1_170.jpg',
          #  'artistId': 25849856,
          #  'artistName': 'bouba',
          #  'artistToken': 'bouba1',
          #  'haveImages': False,
          #  'isLastPage': True}
          if title_prefix is not None:  # False
              set_console_title(title_prefix + " ImageId: {0}".format(image.imageId))
          else:
              # image.artist.artistId  # 25849856
              # image.imageId  # 67745033
              set_console_title('MemberId: ' + str(image.artist.artistId) + ' ImageId: ' + str(image.imageId))
      except PixivException as ex:
          ...
      except Exception as ex:
          ...

      download_image_flag = True

      # date validation and blacklist tag validation
      if __config__.dateDiff > 0:  # False
          ...
      if __config__.useBlacklistTags:  # False
          ...
      if __config__.useBlacklistMembers:  # False
          ...
      if download_image_flag:  # True
          if artist is None:  # True
              PixivHelper.safePrint('Member Name  : ' + image.artist.artistName)
              print('Member Avatar:', image.artist.artistAvatar)
              print('Member Token :', image.artist.artistToken)
          PixivHelper.safePrint("Title: " + image.imageTitle)
          PixivHelper.safePrint("Tags : " + ', '.join(image.imageTags))
          PixivHelper.safePrint("Date : " + str(image.worksDateDateTime))
          print("Mode :", image.imageMode)

          # get bookmark count
          if ("%bookmark_count%" in __config__.filenameFormat or "%image_response_count%" in __config__.filenameFormat) and image.bookmark_count == -1:  # False
              # __config__.filenameFormat
              # '%artist% (%member_id%)/%urlFilename% - %title%'
              ...

          if __config__.useSuppressTags:  # False
              ...

          # get manga page
          if image.imageMode == 'manga' or image.imageMode == 'big':  # False
              ...
          if user_dir == '':  # Yavos: use config-options  # True
              # __config__.rootDirectory
              # '.'
              target_dir = __config__.rootDirectory
          else:  # Yavos: use filename from list
              target_dir = user_dir

          result = PixivConstant.PIXIVUTIL_OK  # 0
          manga_files = dict()
          page = 0
          # image.imageUrls
          # ['https://i.pximg.net/img-original/img/2018/03/15/17/28/24/67745033_p0.jpg']
          for img in image.imageUrls:
              print('Image URL :', img)
              url = os.path.basename(img)
              split_url = url.split('.')
              if split_url[0].startswith(str(image_id)):  # True
                  # Yavos: filename will be added here if given in list
                  filename_format = __config__.filenameFormat
                  if image.imageMode == 'manga':  # False
                      filename_format = __config__.filenameMangaFormat

                  # filename_format  # '%artist% (%member_id%)/%urlFilename% - %title%'
                  # __config__.tagsSeparator  # ','
                  # __config__.tagsLimit  # -1
                  # url  # '67745033_p0.jpg'
                  # bookmark  # False
                  # search_tags  # ''
                  # filename  # 'N/A'
                  filename = PixivHelper.makeFilename(filename_format, image, tagsSeparator=__config__.tagsSeparator, tagsLimit=__config__.tagsLimit, fileUrl=url, bookmark=bookmark, searchTags=search_tags)
                  # filename  # 'bouba (25849856)/67745033_p0 - pixiv.jpg'
                  # target_dir  # '.'
                  filename = PixivHelper.sanitizeFilename(filename, target_dir)
                  # filename  # '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg'

                  # __config__.createMangaDir  # False
                  if image.imageMode == 'manga' and __config__.createMangaDir: # False
                      ...

                  PixivHelper.safePrint('Filename  : ' + filename)
                  result = PixivConstant.PIXIVUTIL_NOT_OK  # -1
                  try:
                      # img  # 'https://i.pximg.net/img-original/img/2018/03/15/17/28/24/67745033_p0.jpg'
                      # filename  # '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg'
                      # referer  # 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=67745033'
                      # __config__.overwrite  # False
                      # __config__.retry  # 3
                      # __config__.backupOldFile  # False
                      # image_id  # 67745033
                      # page  # 0
                      # set last-modified and last-accessed timestamp
                      (result, filename) = download_image(img, filename, referer, __config__.overwrite, __config__.retry, __config__.backupOldFile, image_id, page)
                      # result  # 4 == PixivConstant.PIXIVUTIL_SKIP_DUPLICATE
                      # filename  # '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg'

                      # __config__.setLastModified  # True
                      if __config__.setLastModified and filename is not None and os.path.isfile(filename):  # True
                          # image.worksDateDateTime  # datetime.datetime(2018, 3, 15, 17, 28)
                          # image.worksDateDateTime.timetuple()
                          # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=15, tm_hour=17, tm_min=28, tm_sec=0, tm_wday=3, tm_yday=74, tm_isdst=-1)
                          ts = time.mktime(image.worksDateDateTime.timetuple())
                          # NOTE:
                          # os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)
                          # Set the access and modified times of the file specified by path.
                          os.utime(filename, (ts, ts))

                      if result == PixivConstant.PIXIVUTIL_NOT_OK:  # False
                          PixivHelper.print_and_log('error', 'Image url not found/failed to download: ' + str(image.imageId))
                      elif result == PixivConstant.PIXIVUTIL_ABORTED:
                          raise KeyboardInterrupt()

                      manga_files[page] = filename
                      # manga_files  # {0: '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg'}
                      page = page + 1  # 1

                  except urllib2.URLError:
                      PixivHelper.print_and_log('error', 'Giving up url: ' + str(img))
                      __log__.exception('Error when download_image(): ' + str(img))
                  print('')

          # __config__.writeImageInfo  # False
          # __config__.writeImageJSON  # False
          if __config__.writeImageInfo or __config__.writeImageJSON:  # False
              ...

          if image.imageMode == 'ugoira_view':  # False
              ...

          if __config__.writeUrlInDescription:  # False
              PixivHelper.writeUrlInDescription(image, __config__.urlBlacklistRegex, __config__.urlDumpFilename)

      # Only save to db if all images is downloaded completely
      # result == PixivConstant.PIXIVUTIL_SKIP_DUPLICATE  # True
      if result == PixivConstant.PIXIVUTIL_OK or result == PixivConstant.PIXIVUTIL_SKIP_DUPLICATE or result == PixivConstant.PIXIVUTIL_SKIP_LOCAL_LARGER:
          try:
          # image.artist.artistId  # 25849856
          # image.imageId  #  67745033
          # image.imageMode  #  'bigNew'
              __dbManager__.insertImage(image.artist.artistId, image.imageId, image.imageMode)
          except BaseException:
              PixivHelper.print_and_log('error', 'Failed to insert image id:{0} to DB'.format(image.imageId))
          # image.imageTitle  # 'pixiv'
          # filename  # '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg'
          __dbManager__.updateImage(image.imageId, image.imageTitle, filename, image.imageMode)

          # manga_files
          # {0: '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg'}
          if len(manga_files) > 0:  # True
              for page in manga_files:
                  # image_id, page, manga_files[0]
                  # (67745033, 1, '/home/q/git/PixivUtil2/bouba (25849856)/67745033_p0 - pixiv.jpg')
                  __dbManager__.insertMangaImage(image_id, page, manga_files[page])

          # map back to PIXIVUTIL_OK (because of ugoira file check)
          result = 0

      # image  # <PixivModel.PixivImage object at 0x7fb0bb5db1d0>
      if image is not None:
          del image
      gc.collect()
      # NOTE: description from python doc
      # gc.collect(generation=2)¶
      # With no arguments, run a full collection.

      # clearall()
      print('\n')
      return result  # 0 == PixivConstant.PIXIVUTIL_OK
  except KeyboardInterrupt:
      raise
  except Exception as ex:
     ...

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivBrowserFactory.py#L530

.. code:: python

  # _browser  # <PixivBrowserFactory.PixivBrowser object at 0x7f17d9365f98>
  # vars(_browser)
  # {'_StatefulBrowser__debug': False,
  #  '_StatefulBrowser__state': <mechanicalsoup.stateful_browser._BrowserState object at 0x7f17d870deb8>,
  #  '_StatefulBrowser__verbose': 0,
  #  '_config': <PixivConfig.PixivConfig object at 0x7f17edc456d8>,
  #  '_finalize': <finalize object at 0x7f17edc9a720; for 'Session' at 0x7f17d9365f28>,
  #  '_myId': 2544445,
  #  'addheaders': [('Accept-Charset', 'utf-8')],
  #  'raise_on_404': False,
  #  'session': <requests.sessions.Session object at 0x7f17d9365f28>,
  #  'soup_config': {'features': 'lxml'}}
  # defaultConfig  # <PixivConfig.PixivConfig object at 0x7f17edc456d8>
  # pp vars(defaultConfig)
  # {'IrfanViewPath': 'C:\\Program Files\\IrfanView',
  #  'alwaysCheckFileSize': False,
  #  'avatarNameFormat': '',
  #  'backupOldFile': False,
  #  'checkUpdatedLimit': 0,
  #  'configFileLocation': 'config.ini',
  #  'cookie': '2544445_29e964626327235c17fa25c4fa2c242c',
  #  'createApng': False,
  #  'createDownloadLists': False,
  #  'createGif': False,
  #  'createMangaDir': False,
  #  'createUgoira': False,
  #  'createWebm': False,
  #  'dateDiff': 0,
  #  'dateFormat': '',
  #  'dayLastUpdated': 7,
  #  'dbPath': '',
  #  'debugHttp': False,
  #  'deleteUgoira': False,
  #  'deleteZipFile': False,
  #  'downloadAvatar': True,
  #  'downloadDelay': 2,
  #  'downloadListDirectory': '.',
  #  'dumpMediumPage': False,
  #  'dumpTagSearchPage': False,
  #  'enableDump': True,
  #  'enableInfiniteLoop': False,
  #  'ffmpeg': 'ffmpeg',
  #  'ffmpegCodec': 'libvpx-vp9',
  #  'ffmpegParam': '-lossless 1',
  #  'filenameFormat': '%artist% (%member_id%)/%urlFilename% - %title%',
  #  'filenameInfoFormat': '%artist% (%member_id%)/%urlFilename% - %title%',
  #  'filenameMangaFormat': '%artist% (%member_id%)/%urlFilename% - %title%',
  #  'keepSignedIn': 1,
  #  'logLevel': 'DEBUG',
  #  'numberOfPage': 0,
  #  'overwrite': False,
  #  'password': 'movemaker',
  #  'processFromDb': True,
  #  'proxy': {'http': '', 'https': ''},
  #  'proxyAddress': '',
  #  'r18mode': False,
  #  'retry': 3,
  #  'retryWait': 5,
  #  'rootDirectory': '.',
  #  'setLastModified': True,
  #  'skipDumpFilter': '',
  #  'startIrfanSlide': False,
  #  'startIrfanView': False,
  #  'tagsLimit': -1,
  #  'tagsSeparator': ',',
  #  'timeout': 60,
  #  'urlBlacklistRegex': '',
  #  'urlDumpFilename': 'url_list_%Y%m%d',
  #  'useBlacklistMembers': False,
  #  'useBlacklistTags': False,
  #  'useList': False,
  #  'useProxy': False,
  #  'useRobots': True,
  #  'useSuppressTags': False,
  #  'useTagsAsDir': False,
  #  'useragent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
  #  'username': 'foreturiga',
  #  'verifyImage': False,
  #  'writeImageInfo': False,
  #  'writeImageJSON': False,
  #  'writeUgoiraInfo': False,
  #  'writeUrlInDescription': False}
  # type(defaultCookieJar)  # <class 'http.cookiejar.LWPCookieJar'>
  # pp vars(defaultCookieJar)
  # '_cookies': {'.pixiv.net': {'/': {'module_orders_mypage': Cookie(version=0, name='module_orders_mypage', value='%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D', port=None, port_specified=False, domain='.pixiv.net', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1552639105, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False),
  #                                   'p_ab_id': Cookie(version=0, name='p_ab_id', value='9', port=None, port_specified=False, domain='.pixiv.net', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1678783086, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False),
  #                                   'p_ab_id_2': Cookie(version=0, name='p_ab_id_2', value='5', port=None, port_specified=False, domain='.pixiv.net', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1678783086, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)}},
  #              'pixiv.net': {'/': {'PHPSESSID': Cookie(version=0, name='PHPSESSID', value='2544445_29e964626327235c17fa25c4fa2c242c', port=None, port_specified=False, domain='pixiv.net', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)}},
  #              'www.pixiv.net': {'/': {'is_sensei_service_user': Cookie(version=0, name='is_sensei_service_user', value='1', port=None, port_specified=False, domain='www.pixiv.net', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1521189486, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)}}},
  # '_cookies_lock': <unlocked _thread.RLock object owner=0 count=0 at 0x7f17d946e960>,
  # '_now': 1521103105,
  # '_policy': <http.cookiejar.DefaultCookiePolicy object at 0x7f17d948a1d0>,
  # 'delayload': False,
  # 'filename': None}
  if _browser is None:
      if config is not None:
          defaultConfig = config
      if cookieJar is not None:
          defaultCookieJar = cookieJar
      if defaultCookieJar is None:
          PixivHelper.GetLogger().info("No default cookie jar available, creating... ")
          defaultCookieJar = cookielib.LWPCookieJar()
      _browser = PixivBrowser(defaultConfig, defaultCookieJar)

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivBrowserFactory.py#L317

.. code:: python

  if self._isWhitecube:  # False
      ...
  else:
      url = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id={0}".format(image_id)
      # response = self.open(url).read()
      response = self.getPixivPage(url, returnParsed=False).read()
      self.handleDebugMediumPage(response, image_id)
      # NOTE: nothing happen on handleDebugMediumPage.
      # TODO: test if it work on python3
  
      parsed = BeautifulSoup(response)
      image = PixivModel.PixivImage(
          image_id, parsed, parent, from_bookmark, bookmark_count, image_response_count, dateFormat=self._config.dateFormat)

      # image_id  # 67745033
      # type(parsed)  # <class 'bs4.BeautifulSoup'>
      # parent  # None
      # from_bookmark  # False
      # bookmark_count  # -1
      # image_response_count  # 1
      # self._config.dateFormat  # ''

      # image.imageMode  # "bigNew"
      if image.imageMode == "ugoira_view" or image.imageMode == "bigNew":  # True
          image.ParseImages(parsed)
      # NOTE: decompose description from bs4
      # Tag.decompose() removes a tag from the tree, then completely destroys it and its contents:
      parsed.decompose()
  
  # image  # <PixivModel.PixivImage object at 0x7f17d8767470>
  # pp vars(image)
  # {'artist': <PixivModel.PixivArtist object at 0x7f17d8767438>,
  #  'bookmark_count': -1,
  #  'dateFormat': '',
  #  'descriptionUrlList': [],
  #  'fromBookmark': False,
  #  'imageCaption': 'This very young space explorer has brought this creature back from one of her expeditions. Unlike what one might think the creature is absolutely '
  #                  'not aggressive: quite the opposite !!\n'
  #                  'Telepathically she persuades girls to * with her. She is tireless and provides hours of * delirium to her happy partner.',
  #  'imageCount': 1,
  #  'imageId': 67745033,
  #  'imageMode': 'bigNew',
  #  'imageTitle': 'pixiv',
  #  'imageUrls': ['https://i.pximg.net/img-original/img/2018/03/15/17/28/24/67745033_p0.jpg'],
  #  'jd_rtc': 6,
  #  'jd_rtv': 108,
  #  'originalArtist': <PixivModel.PixivArtist object at 0x7f17d8767438>,
  #  'worksDate': '3/15/2018 17:28',
  #  'worksDateDateTime': datetime.datetime(2018, 3, 15, 17, 28),
  #  'worksResolution': '2000x1686'}
  # type(response)  # <class 'str'>
  # NOTE: response return the image page html text
  return (image, response)

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivBrowserFactory.py#L127

.. code:: python

  # url  # 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=67745033'
  url = self.fixUrl(url)
  # NOTE: no change on result of self.fixUrl
  retry_count = 0
  while True:
      req = urllib2.Request(url)
      # req  # <urllib.request.Request object at 0x7f17d8718390>
      # referer  # https://www.pixiv.net
      req.add_header('Referer', referer)
      try:
          page = self.open(req)
          if returnParsed:  # False
              ...
          else:
              return page
      except Exception as ex:
          ...

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivModel.py#L250

.. code:: python

  ...

  if page is not None:
      # check is error page
      # NOTE: error is not raised
      ...
  
      # parse artist information
      if self.artist is None:
          self.artist = PixivArtist(page=page, fromImage=True)
          # <PixivModel.PixivArtist object at 0x7f17d7ffc710>
  
      if fromBookmark and self.originalArtist is None:  # False
          self.originalArtist = PixivArtist(page=page, fromImage=True)
      else:
          self.originalArtist = self.artist
  
      # parse image information
      self.ParseInfo(page)
      self.ParseTags(page)
      # self.imageTags
      # ['tag1', 'tag2', 'Cute', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9']
      self.ParseWorksData(page)
      # (Pdb++) pp vars(self)
      # {'artist': <PixivModel.PixivArtist object at 0x7f17d8767438>,
      #  'bookmark_count': -1,
      #  'dateFormat': '',
      #  'descriptionUrlList': [],
      #  'fromBookmark': False,
      #  'imageCaption': 'This very young space explorer has brought this creature back from one of her expeditions. Unlike what one might think the creature is absolutely '
      #                  'not aggressive: quite the opposite !!\n'
      #                  'Telepathically she persuades girls to * with her. She is tireless and provides hours of * delirium to her happy partner.',
      #  'imageId': 67745033,
      #  'imageMode': 'bigNew',
      #  'imageTitle': 'pixiv',
      #  'imageUrls': [],
      #  'jd_rtc': 6,
      #  'jd_rtv': 108,
      #  'originalArtist': <PixivModel.PixivArtist object at 0x7f17d8767438>,
      #  'worksDate': '3/15/2018 17:28',
      #  'worksDateDateTime': datetime.datetime(2018, 3, 15, 17, 28),
      #  'worksResolution': '2000x1686'}

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivModel.py#L69

.. code:: python

  avatar_box = page.find(attrs={'class': '_unit profile-unit'})  # None
  self.artistToken = self.ParseToken(page, fromImage)  # 'bouba1'
  
  if avatar_box is not None:
      ...
  else:
      # Issue #236
      avatar_box = page.find(attrs={'class': '_user-profile-card'})
      # type(avatar_box)  # <class 'bs4.element.Tag'>
      if avatar_box is not None:
          temp = avatar_box.find('a')
          # temp
          # <a class="_user-icon size-80 cover-texture" href="/member.php?id=25849856"
          # style="background-image: url('https://i.pximg.net/user-profile/img/2017/07/03/21/05/13/12800072_532e5499464b1dd2bfc4b46440c762c1_170.jpg');"
          # title="bouba"></a>
          self.artistId = int(re.search(r'id=(\d+)', temp['href']).group(1))  # 25849856
          self.artistName = unicode(temp['title'])  # 'bouba'
          self.artistAvatar = avatar_box.find('a')['style'].replace("background-image: url('", "").replace("');", "")
          # 'https://i.pximg.net/user-profile/img/2017/07/03/21/05/13/12800072_532e5499464b1dd2bfc4b46440c762c1_170.jpg'
          return

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivModel.py#L360

.. code:: python

  temp = None
  links = page.find(attrs={'class': 'works_display'}).findAll('a')  # []
  for a in links:
      ...

  if temp is None:  # True
      # changes on pixiv website to handle big image
      self.imageMode = "bigNew"
  else:
      ...
  
  # remove premium-introduction-modal so we can get caption from work-info
  # somehow selecting section doesn't works
  premium_introduction_modal = page.findAll('div', attrs={'id': 'premium-introduction-modal'})
  premium_introduction_modal.extend(page.findAll('div', attrs={'id': 'popular-search-trial-end-introduction-modal'}))  # []
  for modal in premium_introduction_modal:  # False
      ...

  # new layout on 20160319
  temp_titles = page.findAll('h1', attrs={'class': 'title'})
  for tempTitle in temp_titles:  # True
      ...
  # self.imageTitle  # 'pixiv'
  
  description_para = page.findAll("p", attrs={'class': PixivImage.__re_caption})
  for tempCaption in description_para:  # True
      ...
  # print(self.imageCaption)
  # This very young space explorer has brought this creature back from one of her expeditions. Unlike what one might think the creature is absolutely not aggressive: quite the opposite !!
  # Telepathically she persuades girls to * with her. She is tireless and provides hours of * delirium to her happy partner.

  # stats
  view_count = page.find(attrs={'class': 'view-count'})
  if view_count is not None:
      self.jd_rtv = int(view_count.string)  # 108
  # Issue#182 fix
  rated_count = page.find(attrs={'class': 'rated-count'})
  if rated_count is not None:
      self.jd_rtc = int(rated_count.string)  # 6
  
  if description_para is not None and len(description_para) > 0:
      ...
  # self.descriptionUrlList  # []

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivModel.py#L443

.. code:: python

  temp = page.find(attrs={'class': 'meta'}).findAll('li')
  # 07/22/2011 03:09|512×600|RETAS STUDIO
  # 07/26/2011 00:30|Manga 39P|ComicStudio 鉛筆 つけペン
  # 1/05/2011 07:09|723×1023|Photoshop SAI  [ R-18 ]
  # 2013年3月16日 06:44 | 800×1130 | Photoshop ComicStudio | R-18
  # 2013年12月14日 19:00 855×1133 PhotoshopSAI
  
  self.worksDate = PixivHelper.toUnicode(temp[0].string, encoding=sys.stdin.encoding)
  # '3/15/2018 17:28'
  self.worksDateDateTime = PixivHelper.ParseDateTime(self.worksDate, self.dateFormat)
  # datetime.datetime(2018, 3, 15, 17, 28)
  
  self.worksResolution = unicode(temp[1].string).replace(u'×', u'x')  # '2000x1686'
  toolsTemp = page.find(attrs={'class': 'meta'}).find(attrs={'class': 'tools'})
  if toolsTemp is not None and len(toolsTemp) > 0:
      tools = toolsTemp.findAll('li')
      for tool in tools:
          self.worksTools = self.worksTools + ' ' + unicode(tool.string)
      self.worksTools = self.worksTools.strip()

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivModel.py#L499

.. code:: python

  if page is None:
      raise PixivException('No page given', errorCode=PixivException.NO_PAGE_GIVEN)
  if mode is None:
      mode = self.imageMode  # bigNew
  
  # self.imageUrls  # []
  del self.imageUrls[:]
  if mode == 'big' or mode == 'bigNew':  # True
      # type(page)  # <class 'bs4.BeautifulSoup'>
      # _br  # None
      self.imageUrls.append(self.ParseBigImages(page, _br))
  elif mode == 'manga':
      self.imageUrls = self.CheckMangaType(page, _br)
  elif mode == 'ugoira_view':
      self.imageUrls.append(self.ParseUgoira(page))
  if len(self.imageUrls) == 0:
      raise PixivException('No images found for: ' + str(self.imageId), errorCode=PixivException.NO_IMAGES, htmlPage=page)
  # self.imageUrls
  # ['https://i.pximg.net/img-original/img/2018/03/15/17/28/24/67745033_p0.jpg']
  return self.imageUrls

https://github.com/Nandaka/PixivUtil2/blob/0f3a8d5d8ab44524d3dda3cca18be2bb5a42c11e/PixivModel.py#L516

.. code:: python

  self.imageCount = 1
  
  # Issue #224
  # work manga
  temp = page.find('a', attrs={'class': ' _work manga '})  # None
  if temp is not None:
      ...
  
  # new layout for big 20141216
  temp = page.find('img', attrs={'class': 'original-image'})
  # temp 
  # <img alt="Erotic Alien" class="original-image"
  # data-src="https://i.pximg.net/img-original/img/2018/03/15/17/28/24/67745033_p0.jpg"
  # height="1686" width="2000"/>
  if temp is not None:
      return str(temp['data-src'])
  ...
