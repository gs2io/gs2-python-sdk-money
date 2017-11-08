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


class UpdateMoneyRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "UpdateMoney"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateMoneyRequest, self).__init__(params)
        if params is None:
            self.__money_name = None
            self.__priority = None
            self.__use_verify_receipt = None
            self.__google_key = None
            self.__description = None
            self.__apple_key = None
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)
            self.set_use_verify_receipt(params['useVerifyReceipt'] if 'useVerifyReceipt' in params.keys() else None)
            self.set_google_key(params['googleKey'] if 'googleKey' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_apple_key(params['appleKey'] if 'appleKey' in params.keys() else None)

    def get_money_name(self):
        """
        取得する仮想通貨の名前を取得
        :return: 取得する仮想通貨の名前
        :rtype: unicode
        """
        return self.__money_name

    def set_money_name(self, money_name):
        """
        取得する仮想通貨の名前を設定
        :param money_name: 取得する仮想通貨の名前
        :type money_name: unicode
        """
        self.__money_name = money_name

    def with_money_name(self, money_name):
        """
        取得する仮想通貨の名前を設定
        :param money_name: 取得する仮想通貨の名前
        :type money_name: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_money_name(money_name)
        return self

    def get_priority(self):
        """
        支払い優先度を取得
        :return: 支払い優先度
        :rtype: unicode
        """
        return self.__priority

    def set_priority(self, priority):
        """
        支払い優先度を設定
        :param priority: 支払い優先度
        :type priority: unicode
        """
        self.__priority = priority

    def with_priority(self, priority):
        """
        支払い優先度を設定
        :param priority: 支払い優先度
        :type priority: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_priority(priority)
        return self

    def get_use_verify_receipt(self):
        """
        ストアプラットフォームのレシートの検証機能を利用するかを取得
        :return: ストアプラットフォームのレシートの検証機能を利用するか
        :rtype: bool
        """
        return self.__use_verify_receipt

    def set_use_verify_receipt(self, use_verify_receipt):
        """
        ストアプラットフォームのレシートの検証機能を利用するかを設定
        :param use_verify_receipt: ストアプラットフォームのレシートの検証機能を利用するか
        :type use_verify_receipt: bool
        """
        self.__use_verify_receipt = use_verify_receipt

    def with_use_verify_receipt(self, use_verify_receipt):
        """
        ストアプラットフォームのレシートの検証機能を利用するかを設定
        :param use_verify_receipt: ストアプラットフォームのレシートの検証機能を利用するか
        :type use_verify_receipt: bool
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_use_verify_receipt(use_verify_receipt)
        return self

    def get_google_key(self):
        """
        Google のレシート検証用公開鍵を取得
        :return: Google のレシート検証用公開鍵
        :rtype: unicode
        """
        return self.__google_key

    def set_google_key(self, google_key):
        """
        Google のレシート検証用公開鍵を設定
        :param google_key: Google のレシート検証用公開鍵
        :type google_key: unicode
        """
        self.__google_key = google_key

    def with_google_key(self, google_key):
        """
        Google のレシート検証用公開鍵を設定
        :param google_key: Google のレシート検証用公開鍵
        :type google_key: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_google_key(google_key)
        return self

    def get_description(self):
        """
        説明文(1024文字以内)を取得
        :return: 説明文(1024文字以内)
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文(1024文字以内)を設定
        :param description: 説明文(1024文字以内)
        :type description: unicode
        """
        self.__description = description

    def with_description(self, description):
        """
        説明文(1024文字以内)を設定
        :param description: 説明文(1024文字以内)
        :type description: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_description(description)
        return self

    def get_apple_key(self):
        """
        Apple のアプリケーションバンドルIDを取得
        :return: Apple のアプリケーションバンドルID
        :rtype: unicode
        """
        return self.__apple_key

    def set_apple_key(self, apple_key):
        """
        Apple のアプリケーションバンドルIDを設定
        :param apple_key: Apple のアプリケーションバンドルID
        :type apple_key: unicode
        """
        self.__apple_key = apple_key

    def with_apple_key(self, apple_key):
        """
        Apple のアプリケーションバンドルIDを設定
        :param apple_key: Apple のアプリケーションバンドルID
        :type apple_key: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_apple_key(apple_key)
        return self
