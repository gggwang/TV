a=r'''    {
      "name": "量子",
      "hosts": [
        "vip.lz",
        "v.cdnlz",
        "hd.lz"
      ],
      "regex": [
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:6.433333,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:18.5333,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXTINF.*?\\s+.*?1o.*?\\.ts\\s+"
      ]
    },
    {
      "name": "非凡",
      "hosts": [
        "vip.ffzy",
        "hd.ffzy"
      ],
      "regex": [
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:6.666667,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:25.0666,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXTINF.*?\\s+.*?1o.*?\\.ts\\s+"
      ]
    },
    {
      "name": "暴风",
      "hosts": [
        "bfzy",
        "s5.bfzycdn"
      ],
      "regex": [
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:3,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXTINF.*?\\s+.*?1o.*?\\.ts\\s+"
      ]
    },
    {
      "name": "索尼",
      "hosts": [
        "suonizy"
      ],
      "regex": [
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:15.1666,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:15.2666,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXTINF.*?\\s+.*?1o.*?\\.ts\\s+"
      ]
    },
    {
      "name": "蜗牛",
      "hosts": [
        "vip.123pan.cn",
        "rescdn.wuxivlog.cn"
      ],
      "regex": [
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:10.840000,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:10.120000,[\\s\\S]*?#EXT-X-DISCONTINUITY",
        "#EXTINF.*?\\s+.*?1o.*?\\.ts\\s+"
      ]
    },
    {
      "name": "农民嗅探",
      "hosts": [
        "toutiaovod.com"
      ],
      "regex": [
        "video/tos/cn"
      ]
    },
    {
      "name": "hs",
      "hosts": [
        "huoshan.com"
      ],
      "regex": [
        "item_id="
      ]
    },
    {
      "name": "dy",
      "hosts": [
        "douyin.com"
      ],
      "regex": [
        "is_play_url="
      ]
    },
    {
      "name": "cl",
      "hosts": [
        "magnet"
      ],
      "regex": [
        "最 新",
        "直 播",
        "更 新"
      ]
    }'''

b=a.replace(' ','').replace('\n','')
print(b)

