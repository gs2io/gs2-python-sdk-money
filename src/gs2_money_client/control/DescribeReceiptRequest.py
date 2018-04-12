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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_money_client.Gs2Money import Gs2Money


class DescribeReceiptRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "DescribeReceipt"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeReceiptRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
        if params is None:
            self.__begin = None
        else:
            self.set_begin(params['begin'] if 'begin' in params.keys() else None)
        if params is None:
            self.__end = None
        else:
            self.set_end(params['end'] if 'end' in params.keys() else None)
        if params is None:
            self.__page_token = None
        else:
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
        if params is None:
            self.__limit = None
        else:
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

    def get_money_name(self):
        """
        仮想通貨の名前を取得
        :return: 仮想通貨の名前
        :rtype: unicode
        """
        return self.__money_name

    def set_money_name(self, money_name):
        """
        仮想通貨の名前を設定
        :param money_name: 仮想通貨の名前
        :type money_name: unicode
        """
        if not isinstance(money_name, unicode):
            raise TypeError(type(money_name))
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        仮想通貨の名前を設定
        :param money_name: 仮想通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: DescribeReceiptRequest
        """
        self.set_money_name(money_name)
        return self

    def get_begin(self):
        """
        データの取得開始日時(エポック秒)を取得
        :return: データの取得開始日時(エポック秒)
        :rtype: int
        """
        return self.__begin

    def set_begin(self, begin):
        """
        データの取得開始日時(エポック秒)を設定
        :param begin: データの取得開始日時(エポック秒)
        :type begin: int
        """
        if not isinstance(begin, int):
            raise TypeError(type(begin))
        self.__begin = begin

    def with_begin(self, begin):
        """
        データの取得開始日時(エポック秒)を設定
        :param begin: データの取得開始日時(エポック秒)
        :type begin: int
        :return: this
        :rtype: DescribeReceiptRequest
        """
        self.set_begin(begin)
        return self

    def get_end(self):
        """
        データの取得終了日時(エポック秒)を取得
        :return: データの取得終了日時(エポック秒)
        :rtype: int
        """
        return self.__end

    def set_end(self, end):
        """
        データの取得終了日時(エポック秒)を設定
        :param end: データの取得終了日時(エポック秒)
        :type end: int
        """
        if not isinstance(end, int):
            raise TypeError(type(end))
        self.__end = end

    def with_end(self, end):
        """
        データの取得終了日時(エポック秒)を設定
        :param end: データの取得終了日時(エポック秒)
        :type end: int
        :return: this
        :rtype: DescribeReceiptRequest
        """
        self.set_end(end)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        if not isinstance(page_token, unicode):
            raise TypeError(type(page_token))
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeReceiptRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeReceiptRequest
        """
        self.set_limit(limit)
        return self
