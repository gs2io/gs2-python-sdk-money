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


class DescribeReceiptByUserAndSlotRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "DescribeReceiptByUserAndSlot"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeReceiptByUserAndSlotRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
            self.__user_id = None
            self.__slot = None
            self.__begin = None
            self.__end = None
            self.__page_token = None
            self.__limit = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_slot(params['slot'] if 'slot' in params.keys() else None)
            self.set_begin(params['begin'] if 'begin' in params.keys() else None)
            self.set_end(params['end'] if 'end' in params.keys() else None)
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
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
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        仮想通貨の名前を設定
        :param money_name: 仮想通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
        """
        self.set_money_name(money_name)
        return self

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
        """
        self.set_user_id(user_id)
        return self

    def get_slot(self):
        """
        スロット番号を取得
        :return: スロット番号
        :rtype: int
        """
        return self.__slot

    def set_slot(self, slot):
        """
        スロット番号を設定
        :param slot: スロット番号
        :type slot: int
        """
        self.__slot = slot

    def with_slot(self, slot):
        """
        スロット番号を設定
        :param slot: スロット番号
        :type slot: int
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
        """
        self.set_slot(slot)
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
        self.__begin = begin

    def with_begin(self, begin):
        """
        データの取得開始日時(エポック秒)を設定
        :param begin: データの取得開始日時(エポック秒)
        :type begin: int
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
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
        self.__end = end

    def with_end(self, end):
        """
        データの取得終了日時(エポック秒)を設定
        :param end: データの取得終了日時(エポック秒)
        :type end: int
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
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
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
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
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeReceiptByUserAndSlotRequest
        """
        self.set_limit(limit)
        return self
