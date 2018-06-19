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
            self.__money_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__priority = None
            self.__share_free = None
            self.__currency = None
            self.__use_verify_receipt = None
            self.__apple_key = None
            self.__google_key = None
            self.__balance = None
            self.__create_wallet_trigger_script = None
            self.__create_wallet_done_trigger_script = None
            self.__charge_wallet_trigger_script = None
            self.__charge_wallet_done_trigger_script = None
            self.__consume_wallet_trigger_script = None
            self.__consume_wallet_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_money_id(params['moneyId'] if 'moneyId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)
            self.set_share_free(params['shareFree'] if 'shareFree' in params.keys() else None)
            self.set_currency(params['currency'] if 'currency' in params.keys() else None)
            self.set_use_verify_receipt(params['useVerifyReceipt'] if 'useVerifyReceipt' in params.keys() else None)
            self.set_apple_key(params['appleKey'] if 'appleKey' in params.keys() else None)
            self.set_google_key(params['googleKey'] if 'googleKey' in params.keys() else None)
            self.set_balance(params['balance'] if 'balance' in params.keys() else None)
            self.set_create_wallet_trigger_script(params['createWalletTriggerScript'] if 'createWalletTriggerScript' in params.keys() else None)
            self.set_create_wallet_done_trigger_script(params['createWalletDoneTriggerScript'] if 'createWalletDoneTriggerScript' in params.keys() else None)
            self.set_charge_wallet_trigger_script(params['chargeWalletTriggerScript'] if 'chargeWalletTriggerScript' in params.keys() else None)
            self.set_charge_wallet_done_trigger_script(params['chargeWalletDoneTriggerScript'] if 'chargeWalletDoneTriggerScript' in params.keys() else None)
            self.set_consume_wallet_trigger_script(params['consumeWalletTriggerScript'] if 'consumeWalletTriggerScript' in params.keys() else None)
            self.set_consume_wallet_done_trigger_script(params['consumeWalletDoneTriggerScript'] if 'consumeWalletDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_money_id(self):
        """
        課金通貨GRNを取得
        :return: 課金通貨GRN
        :rtype: unicode
        """
        return self.__money_id

    def set_money_id(self, money_id):
        """
        課金通貨GRNを設定
        :param money_id: 課金通貨GRN
        :type money_id: unicode
        """
        self.__money_id = money_id

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

    def get_name(self):
        """
        課金通貨名を取得
        :return: 課金通貨名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        課金通貨名を設定
        :param name: 課金通貨名
        :type name: unicode
        """
        self.__name = name

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

    def get_share_free(self):
        """
        無償課金通貨を異なるスロットで共有するかを取得
        :return: 無償課金通貨を異なるスロットで共有するか
        :rtype: bool
        """
        return self.__share_free

    def set_share_free(self, share_free):
        """
        無償課金通貨を異なるスロットで共有するかを設定
        :param share_free: 無償課金通貨を異なるスロットで共有するか
        :type share_free: bool
        """
        self.__share_free = share_free

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

    def get_create_wallet_trigger_script(self):
        """
        ウォレット新規作成時 に実行されるGS2-Scriptを取得
        :return: ウォレット新規作成時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_wallet_trigger_script

    def set_create_wallet_trigger_script(self, create_wallet_trigger_script):
        """
        ウォレット新規作成時 に実行されるGS2-Scriptを設定
        :param create_wallet_trigger_script: ウォレット新規作成時 に実行されるGS2-Script
        :type create_wallet_trigger_script: unicode
        """
        self.__create_wallet_trigger_script = create_wallet_trigger_script

    def get_create_wallet_done_trigger_script(self):
        """
        ウォレット新規作成完了時 に実行されるGS2-Scriptを取得
        :return: ウォレット新規作成完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_wallet_done_trigger_script

    def set_create_wallet_done_trigger_script(self, create_wallet_done_trigger_script):
        """
        ウォレット新規作成完了時 に実行されるGS2-Scriptを設定
        :param create_wallet_done_trigger_script: ウォレット新規作成完了時 に実行されるGS2-Script
        :type create_wallet_done_trigger_script: unicode
        """
        self.__create_wallet_done_trigger_script = create_wallet_done_trigger_script

    def get_charge_wallet_trigger_script(self):
        """
        ウォレット残高加算時 に実行されるGS2-Scriptを取得
        :return: ウォレット残高加算時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__charge_wallet_trigger_script

    def set_charge_wallet_trigger_script(self, charge_wallet_trigger_script):
        """
        ウォレット残高加算時 に実行されるGS2-Scriptを設定
        :param charge_wallet_trigger_script: ウォレット残高加算時 に実行されるGS2-Script
        :type charge_wallet_trigger_script: unicode
        """
        self.__charge_wallet_trigger_script = charge_wallet_trigger_script

    def get_charge_wallet_done_trigger_script(self):
        """
        ウォレット残高加算完了時 に実行されるGS2-Scriptを取得
        :return: ウォレット残高加算完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__charge_wallet_done_trigger_script

    def set_charge_wallet_done_trigger_script(self, charge_wallet_done_trigger_script):
        """
        ウォレット残高加算完了時 に実行されるGS2-Scriptを設定
        :param charge_wallet_done_trigger_script: ウォレット残高加算完了時 に実行されるGS2-Script
        :type charge_wallet_done_trigger_script: unicode
        """
        self.__charge_wallet_done_trigger_script = charge_wallet_done_trigger_script

    def get_consume_wallet_trigger_script(self):
        """
        ウォレット残高消費時 に実行されるGS2-Scriptを取得
        :return: ウォレット残高消費時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_wallet_trigger_script

    def set_consume_wallet_trigger_script(self, consume_wallet_trigger_script):
        """
        ウォレット残高消費時 に実行されるGS2-Scriptを設定
        :param consume_wallet_trigger_script: ウォレット残高消費時 に実行されるGS2-Script
        :type consume_wallet_trigger_script: unicode
        """
        self.__consume_wallet_trigger_script = consume_wallet_trigger_script

    def get_consume_wallet_done_trigger_script(self):
        """
        ウォレット残高消費完了時 に実行されるGS2-Scriptを取得
        :return: ウォレット残高消費完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_wallet_done_trigger_script

    def set_consume_wallet_done_trigger_script(self, consume_wallet_done_trigger_script):
        """
        ウォレット残高消費完了時 に実行されるGS2-Scriptを設定
        :param consume_wallet_done_trigger_script: ウォレット残高消費完了時 に実行されるGS2-Script
        :type consume_wallet_done_trigger_script: unicode
        """
        self.__consume_wallet_done_trigger_script = consume_wallet_done_trigger_script

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

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Money, self).__getitem__(key)

    def to_dict(self):
        return {
            "moneyId": self.__money_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "priority": self.__priority,
            "shareFree": self.__share_free,
            "currency": self.__currency,
            "useVerifyReceipt": self.__use_verify_receipt,
            "appleKey": self.__apple_key,
            "googleKey": self.__google_key,
            "balance": self.__balance,
            "createWalletTriggerScript": self.__create_wallet_trigger_script,
            "createWalletDoneTriggerScript": self.__create_wallet_done_trigger_script,
            "chargeWalletTriggerScript": self.__charge_wallet_trigger_script,
            "chargeWalletDoneTriggerScript": self.__charge_wallet_done_trigger_script,
            "consumeWalletTriggerScript": self.__consume_wallet_trigger_script,
            "consumeWalletDoneTriggerScript": self.__consume_wallet_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
