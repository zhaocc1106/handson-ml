#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
Tools.

Authors: zhaochaochao(zhaochaochao@baidu.com)
Date:    2019/11/7 上午9:24
"""
import urllib.request as req


def set_proxy():
    """Set http https ftp proxy. The proxy ip and port is yours proxy. I use
    Bandwagon as proxy. Many pictures can't access if not set proxy.

    Returns:

    """
    handler = req.ProxyHandler({'http': '127.0.0.1:1080',
                                'https': '127.0.0.1:1080',
                                'ftp': '127.0.0.1:1080'})
    opener = req.build_opener(handler)
    req.install_opener(opener)
