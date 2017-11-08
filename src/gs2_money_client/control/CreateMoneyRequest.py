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


class CreateMoneyRequest(Gs2BasicRequest):

    class Constant(Gs2Money):
        FUNCTION = "CreateMoney"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateMoneyRequest, self).__init__(params)
        if params is None:
            self.__use_verify_receipt = None
            self.__name = None
            self.__google_key = None
            self.__priority = None
            self.__currency = None
            self.__share_free = None
            self.__apple_key = None
            self.__description = None
        else:
            self.set_use_verify_receipt(params['useVerifyReceipt'] if 'useVerifyReceipt' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_google_key(params['googleKey'] if 'googleKey' in params.keys() else None)
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)
            self.set_currency(params['currency'] if 'currency' in params.keys() else None)
            self.set_share_free(params['shareFree'] if 'shareFree' in params.keys() else None)
            self.set_apple_key(params['appleKey'] if 'appleKey' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)

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
        :rtype: CreateMoneyRequest
        """
        self.set_use_verify_receipt(use_verify_receipt)
        return self

    def get_name(self):
        """
        仮想通貨名を取得
        :return: 仮想通貨名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        仮想通貨名を設定
        :param name: 仮想通貨名
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        仮想通貨名を設定
        :param name: 仮想通貨名
        :type name: unicode
        :return: this
        :rtype: CreateMoneyRequest
        """
        self.set_name(name)
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
        :rtype: CreateMoneyRequest
        """
        self.set_google_key(google_key)
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
        :rtype: CreateMoneyRequest
        """
        self.set_priority(priority)
        return self

    def get_currency(self):
        """
        通貨を取得
        :return: 通貨
        :rtype: unicode
        """
        return self.__currency

    def set_currency(self, currency):
        """
        通貨を設定
        :param currency: 通貨
        :type currency: unicode
        """
        self.__currency = currency

    def with_currency(self, currency):
        """
        通貨を設定
        :param currency: 通貨
        :type currency: unicode
        :return: this
        :rtype: CreateMoneyRequest
        """
        self.set_currency(currency)
        return self

    def get_share_free(self):
        """
        無償仮想通貨を異なるスロットで共有するかを取得
        :return: 無償仮想通貨を異なるスロットで共有するか
        :rtype: bool
        """
        return self.__share_free

    def set_share_free(self, share_free):
        """
        無償仮想通貨を異なるスロットで共有するかを設定
        :param share_free: 無償仮想通貨を異なるスロットで共有するか
        :type share_free: bool
        """
        self.__share_free = share_free

    def with_share_free(self, share_free):
        """
        無償仮想通貨を異なるスロットで共有するかを設定
        :param share_free: 無償仮想通貨を異なるスロットで共有するか
        :type share_free: bool
        :return: this
        :rtype: CreateMoneyRequest
        """
        self.set_share_free(share_free)
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
        :rtype: CreateMoneyRequest
        """
        self.set_apple_key(apple_key)
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
        :rtype: CreateMoneyRequest
        """
        self.set_description(description)
        return self
