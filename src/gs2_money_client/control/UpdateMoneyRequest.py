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
        else:
            self.set_money_name(params['moneyName'] if 'moneyName' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__priority = None
        else:
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)
        if params is None:
            self.__use_verify_receipt = None
        else:
            self.set_use_verify_receipt(params['useVerifyReceipt'] if 'useVerifyReceipt' in params.keys() else None)
        if params is None:
            self.__apple_key = None
        else:
            self.set_apple_key(params['appleKey'] if 'appleKey' in params.keys() else None)
        if params is None:
            self.__google_key = None
        else:
            self.set_google_key(params['googleKey'] if 'googleKey' in params.keys() else None)
        if params is None:
            self.__create_wallet_trigger_script = None
        else:
            self.set_create_wallet_trigger_script(params['createWalletTriggerScript'] if 'createWalletTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_wallet_done_trigger_script = None
        else:
            self.set_create_wallet_done_trigger_script(params['createWalletDoneTriggerScript'] if 'createWalletDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__charge_wallet_trigger_script = None
        else:
            self.set_charge_wallet_trigger_script(params['chargeWalletTriggerScript'] if 'chargeWalletTriggerScript' in params.keys() else None)
        if params is None:
            self.__charge_wallet_done_trigger_script = None
        else:
            self.set_charge_wallet_done_trigger_script(params['chargeWalletDoneTriggerScript'] if 'chargeWalletDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__consume_wallet_trigger_script = None
        else:
            self.set_consume_wallet_trigger_script(params['consumeWalletTriggerScript'] if 'consumeWalletTriggerScript' in params.keys() else None)
        if params is None:
            self.__consume_wallet_done_trigger_script = None
        else:
            self.set_consume_wallet_done_trigger_script(params['consumeWalletDoneTriggerScript'] if 'consumeWalletDoneTriggerScript' in params.keys() else None)

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
        if not isinstance(money_name, unicode):
            raise TypeError(type(money_name))
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
        if not isinstance(description, unicode):
            raise TypeError(type(description))
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
        if not isinstance(priority, unicode):
            raise TypeError(type(priority))
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
        if not isinstance(use_verify_receipt, bool):
            raise TypeError(type(use_verify_receipt))
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
        if not isinstance(apple_key, unicode):
            raise TypeError(type(apple_key))
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
        if not isinstance(google_key, unicode):
            raise TypeError(type(google_key))
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
        if not isinstance(create_wallet_trigger_script, unicode):
            raise TypeError(type(create_wallet_trigger_script))
        self.__create_wallet_trigger_script = create_wallet_trigger_script

    def with_create_wallet_trigger_script(self, create_wallet_trigger_script):
        """
        ウォレット新規作成時 に実行されるGS2-Scriptを設定
        :param create_wallet_trigger_script: ウォレット新規作成時 に実行されるGS2-Script
        :type create_wallet_trigger_script: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_create_wallet_trigger_script(create_wallet_trigger_script)
        return self

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
        if not isinstance(create_wallet_done_trigger_script, unicode):
            raise TypeError(type(create_wallet_done_trigger_script))
        self.__create_wallet_done_trigger_script = create_wallet_done_trigger_script

    def with_create_wallet_done_trigger_script(self, create_wallet_done_trigger_script):
        """
        ウォレット新規作成完了時 に実行されるGS2-Scriptを設定
        :param create_wallet_done_trigger_script: ウォレット新規作成完了時 に実行されるGS2-Script
        :type create_wallet_done_trigger_script: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_create_wallet_done_trigger_script(create_wallet_done_trigger_script)
        return self

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
        if not isinstance(charge_wallet_trigger_script, unicode):
            raise TypeError(type(charge_wallet_trigger_script))
        self.__charge_wallet_trigger_script = charge_wallet_trigger_script

    def with_charge_wallet_trigger_script(self, charge_wallet_trigger_script):
        """
        ウォレット残高加算時 に実行されるGS2-Scriptを設定
        :param charge_wallet_trigger_script: ウォレット残高加算時 に実行されるGS2-Script
        :type charge_wallet_trigger_script: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_charge_wallet_trigger_script(charge_wallet_trigger_script)
        return self

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
        if not isinstance(charge_wallet_done_trigger_script, unicode):
            raise TypeError(type(charge_wallet_done_trigger_script))
        self.__charge_wallet_done_trigger_script = charge_wallet_done_trigger_script

    def with_charge_wallet_done_trigger_script(self, charge_wallet_done_trigger_script):
        """
        ウォレット残高加算完了時 に実行されるGS2-Scriptを設定
        :param charge_wallet_done_trigger_script: ウォレット残高加算完了時 に実行されるGS2-Script
        :type charge_wallet_done_trigger_script: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_charge_wallet_done_trigger_script(charge_wallet_done_trigger_script)
        return self

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
        if not isinstance(consume_wallet_trigger_script, unicode):
            raise TypeError(type(consume_wallet_trigger_script))
        self.__consume_wallet_trigger_script = consume_wallet_trigger_script

    def with_consume_wallet_trigger_script(self, consume_wallet_trigger_script):
        """
        ウォレット残高消費時 に実行されるGS2-Scriptを設定
        :param consume_wallet_trigger_script: ウォレット残高消費時 に実行されるGS2-Script
        :type consume_wallet_trigger_script: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_consume_wallet_trigger_script(consume_wallet_trigger_script)
        return self

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
        if not isinstance(consume_wallet_done_trigger_script, unicode):
            raise TypeError(type(consume_wallet_done_trigger_script))
        self.__consume_wallet_done_trigger_script = consume_wallet_done_trigger_script

    def with_consume_wallet_done_trigger_script(self, consume_wallet_done_trigger_script):
        """
        ウォレット残高消費完了時 に実行されるGS2-Scriptを設定
        :param consume_wallet_done_trigger_script: ウォレット残高消費完了時 に実行されるGS2-Script
        :type consume_wallet_done_trigger_script: unicode
        :return: this
        :rtype: UpdateMoneyRequest
        """
        self.set_consume_wallet_done_trigger_script(consume_wallet_done_trigger_script)
        return self
