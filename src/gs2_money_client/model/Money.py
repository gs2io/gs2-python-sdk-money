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

class Money(object):

    def __init__(self, params=None):
        if params is None:
            self.__use_verify_receipt = None
            self.__money_id = None
            self.__name = None
            self.__google_key = None
            self.__priority = None
            self.__currency = None
            self.__share_free = None
            self.__create_at = None
            self.__owner_id = None
            self.__balance = None
            self.__update_at = None
            self.__apple_key = None
            self.__description = None
        else:
            self.set_use_verify_receipt(params['useVerifyReceipt'] if 'useVerifyReceipt' in params.keys() else None)
            self.set_money_id(params['moneyId'] if 'moneyId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_google_key(params['googleKey'] if 'googleKey' in params.keys() else None)
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)
            self.set_currency(params['currency'] if 'currency' in params.keys() else None)
            self.set_share_free(params['shareFree'] if 'shareFree' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_balance(params['balance'] if 'balance' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
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

    def get_money_id(self):
        """
        仮想通貨IDを取得
        :return: 仮想通貨ID
        :rtype: unicode
        """
        return self.__money_id

    def set_money_id(self, money_id):
        """
        仮想通貨IDを設定
        :param money_id: 仮想通貨ID
        :type money_id: unicode
        """
        self.__money_id = money_id

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

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_balance(self):
        """
        未使用残高を取得
        :return: 未使用残高
        :rtype: float
        """
        return self.__balance

    def set_balance(self, balance):
        """
        未使用残高を設定
        :param balance: 未使用残高
        :type balance: float
        """
        self.__balance = balance

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

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

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def to_dict(self):
        return { 
            "useVerifyReceipt": self.__use_verify_receipt,
            "moneyId": self.__money_id,
            "name": self.__name,
            "googleKey": self.__google_key,
            "priority": self.__priority,
            "currency": self.__currency,
            "shareFree": self.__share_free,
            "createAt": self.__create_at,
            "ownerId": self.__owner_id,
            "balance": self.__balance,
            "updateAt": self.__update_at,
            "appleKey": self.__apple_key,
            "description": self.__description,
        }