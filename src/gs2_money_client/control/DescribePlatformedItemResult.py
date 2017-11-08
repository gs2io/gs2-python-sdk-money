# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_money_client.model import *


class DescribePlatformedItemResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__next_page_token = unicode(response['nextPageToken']) if 'nextPageToken' in response.keys() and response['nextPageToken'] is not None else None
        
        self.__items = list(
            map(
                lambda data:
                PlatformedItem(data)
                ,
                response['items']
            )
        )

    def get_next_page_token(self):
        """
        次のページを読み込むためのトークンを取得
        :return: 次のページを読み込むためのトークン
        :rtype: unicode
        """
        return self.__next_page_token

    def get_items(self):
        """
        プラットフォーム個別商品を取得
        :return: プラットフォーム個別商品
        :rtype: list[PlatformedItem]
        """
        return self.__items

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return { 
            'nextPageToken': self.__next_page_token,
        
            'items': map(lambda item: item.to_dict(), self.__items),
        
        }