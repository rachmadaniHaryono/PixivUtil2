PixivUtil2 Hydrus Server
========================

Hydrus booru + PixivUtil2

Usage
-----

1. Run server with following command

.. code:: bash

  PixivUtil2-server run -p 5005 --debugger --with-threads

2. choose which booru mode to install in Hydrus:

Simple pixivutil imageurl

.. code:: yaml

  !Booru
  _advance_by_page_num: true
  _image_data: '[link]'
  _image_id: null
  _name: pixivutil2
  _search_separator: +
  _search_url: http://127.0.0.1:5005/?query=%tags%
  _tag_classnames_to_namespaces: {tag-page-url: gid page url, tag-picture-subtitle: gid
      subtitle, tag-picture-title: gid title, tag-query: gid query, tag-site: gid site,
    tag-site-title: gid site title}
  _thumb_classname: thumb

Installation
------------

.. code:: bash

   git clone https://github.com/rachmadaniHaryono/PixivUtil2
   pip install .
   pip install .[server]
