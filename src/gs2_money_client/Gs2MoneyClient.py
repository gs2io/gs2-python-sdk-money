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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2MoneyClient(AbstractGs2Client):

    ENDPOINT = "money"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2MoneyClient, self).__init__(credential, region)


    def charge_wallet(self, request):
        """
        ウォレットに仮想通貨をチャージします<br>
        <br>
        trasactionId にトランザクションIDを指定することで、<br>
        1回の課金処理で複数回仮想通貨をチャージすることを防ぐことが出来ます。<br>
        重複したリクエストが発生した場合は 409エラー(ConflictException) が発生しますが、正常処理とするべきです。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.ChargeWalletRequest.ChargeWalletRequest
        :return: 結果
        :rtype: gs2_money_client.control.ChargeWalletResult.ChargeWalletResult
        """
        body = { 
            "count": request.get_count(),
            "price": request.get_price(),
        }

        if request.get_transaction_id() is not None:
            body["transactionId"] = request.get_transaction_id()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_money_client.control.ChargeWalletRequest import ChargeWalletRequest

        from gs2_money_client.control.ChargeWalletResult import ChargeWalletResult
        return ChargeWalletResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/wallet/" + str(("null" if request.get_slot() is None else request.get_slot())) + "/charge",
            service=self.ENDPOINT,
            module=ChargeWalletRequest.Constant.MODULE,
            function=ChargeWalletRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def charge_wallet_by_user(self, request):
        """
        ウォレットに仮想通貨をチャージします<br>
        <br>
        trasactionId にトランザクションIDを指定することで、<br>
        1回の課金処理で複数回仮想通貨をチャージすることを防ぐことが出来ます。<br>
        重複したリクエストが発生した場合は 409エラー(ConflictException) が発生しますが、正常処理とするべきです。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.ChargeWalletByUserRequest.ChargeWalletByUserRequest
        :return: 結果
        :rtype: gs2_money_client.control.ChargeWalletByUserResult.ChargeWalletByUserResult
        """
        body = { 
            "count": request.get_count(),
            "price": request.get_price(),
        }

        if request.get_transaction_id() is not None:
            body["transactionId"] = request.get_transaction_id()
        headers = { 
        }
        from gs2_money_client.control.ChargeWalletByUserRequest import ChargeWalletByUserRequest

        from gs2_money_client.control.ChargeWalletByUserResult import ChargeWalletByUserResult
        return ChargeWalletByUserResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/wallet/" + str(("null" if request.get_slot() is None else request.get_slot())) + "/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "/charge",
            service=self.ENDPOINT,
            module=ChargeWalletByUserRequest.Constant.MODULE,
            function=ChargeWalletByUserRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def consume_wallet(self, request):
        """
        ウォレットから仮想通貨を消費します<br>
        <br>
        paidOnly に true を指定することで、有償仮想通貨のみ消費対象とすることが出来ます。<br>
        プレミアムなサービスの提供時などに活用してください。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.ConsumeWalletRequest.ConsumeWalletRequest
        :return: 結果
        :rtype: gs2_money_client.control.ConsumeWalletResult.ConsumeWalletResult
        """
        body = { 
            "count": request.get_count(),
            "use": request.get_use(),
        }

        if request.get_paid_only() is not None:
            body["paidOnly"] = request.get_paid_only()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_money_client.control.ConsumeWalletRequest import ConsumeWalletRequest

        from gs2_money_client.control.ConsumeWalletResult import ConsumeWalletResult
        return ConsumeWalletResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/wallet/" + str(("null" if request.get_slot() is None else request.get_slot())) + "/consume",
            service=self.ENDPOINT,
            module=ConsumeWalletRequest.Constant.MODULE,
            function=ConsumeWalletRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_item(self, request):
        """
        商品を新規作成します<br>
        <br>
        このデータは GS2-Money のレシート検証機能を利用するときにのみ登録する必要があります。<br>
        これはレシート検証の結果妥当だった場合対価として仮想通貨を付与するために、<br>
        どのような価値の仮想通貨をいくらで販売しているのかという情報を GS2-Money が持っていなければサービスを実現できないためです。<br>
        <br>
        - 商品(仮想通貨 60個)<br>
        -- プラットフォーム個別商品(AppleAppStore 120円)<br>
        -- プラットフォーム個別商品(GooglePlay 120円)<br>
        <br>
        という構造で商品を登録する必要があります。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.CreateItemRequest.CreateItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.CreateItemResult.CreateItemResult
        """
        body = { 
            "count": request.get_count(),
            "name": request.get_name(),
        }

        headers = { 
        }
        from gs2_money_client.control.CreateItemRequest import CreateItemRequest

        from gs2_money_client.control.CreateItemResult import CreateItemResult
        return CreateItemResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item",
            service=self.ENDPOINT,
            module=CreateItemRequest.Constant.MODULE,
            function=CreateItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_money(self, request):
        """
        仮想通貨を新規作成します<br>
        <br>
        priority には仮想通貨の消費優先度を指定することが出来ます。<br>
        無償仮想通貨を優先して消費する場合は free を、有償仮想通貨を優先して消費する場合は paid を指定します。<br>
        資金決済法への対応としては有償仮想通貨を優先して消費するほうが未使用残高が溜まりにくく効率的ですが、<br>
        有償仮想通貨でしか購入できないアイテムを提供している場合はユーザの心象は悪いかもしれません。<br>
        <br>
        ユーザごとにウォレットという財布のようなものを用意し、仮想通貨はそこにチャージされます。<br>
        ウォレットにはスロットという概念があり、各ユーザ複数の財布を持つことが出来ます。<br>
        これはガイドラインによってプラットフォームごとに仮想通貨を分けて管理する必要があるためです。<br>
        このガイドラインは有償仮想通貨にのみ適用される者で、無償仮想通貨はその義務は生じません。<br>
        そのため shareFree という設定値があり、ここを true に設定することですべてのスロットで無償仮想通貨を共有することができるようになります。<br>
        この際、あらゆるスロットにアクセスしても無償仮想通貨に関してはスロット0の仮想通貨が利用される。という挙動を取ります。<br>
        <br>
        useVerifyReceipt で課金時に各プラットフォームから取得できるレシートを検証する機能を利用できるようになります。<br>
        レシートの検証機能を利用する場合は各プラットフォームごとに検証に必要な要素を登録しておく必要があります。<br>
        <br>
        AppleAppStore におけるレシートの検証を実現するには appleKey を指定します。<br>
        appleKey にはアプリケーションの bundle_id を指定してください。<br>
        異なるアプリケーションで決済されたトランザクションで仮想通貨をチャージすることを防ぐ意味があります。<br>
        <br>
        GooglePlay におけるレシートの検証を実現するには googleKey を指定します。<br>
        googleKey には Google Play Developer Console で取得できる公開鍵を指定してください。<br>
        レシートが改ざんされていないか検証するために利用します。<br>
        <br>
        GS2-Money は資金決済法における前払式支払手段(自家型)に対応します。<br>
        マネージメントコンソールやAPIで取得できる未使用残高が1,000万円を超えると法的な責任が発生します。<br>
        詳しくはドキュメントを参照してください。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.CreateMoneyRequest.CreateMoneyRequest
        :return: 結果
        :rtype: gs2_money_client.control.CreateMoneyResult.CreateMoneyResult
        """
        body = { 
            "useVerifyReceipt": request.get_use_verify_receipt(),
            "name": request.get_name(),
            "priority": request.get_priority(),
            "shareFree": request.get_share_free(),
            "description": request.get_description(),
        }

        if request.get_google_key() is not None:
            body["googleKey"] = request.get_google_key()
        if request.get_currency() is not None:
            body["currency"] = request.get_currency()
        if request.get_apple_key() is not None:
            body["appleKey"] = request.get_apple_key()
        headers = { 
        }
        from gs2_money_client.control.CreateMoneyRequest import CreateMoneyRequest

        from gs2_money_client.control.CreateMoneyResult import CreateMoneyResult
        return CreateMoneyResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money",
            service=self.ENDPOINT,
            module=CreateMoneyRequest.Constant.MODULE,
            function=CreateMoneyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_platformed_item(self, request):
        """
        プラットフォーム個別商品を新規作成します<br>
        <br>
        name には各プラットフォームの管理コンソールで作成した消費型アイテムの名前を指定してください。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.CreatePlatformedItemRequest.CreatePlatformedItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.CreatePlatformedItemResult.CreatePlatformedItemResult
        """
        body = { 
            "platform": request.get_platform(),
            "price": request.get_price(),
            "name": request.get_name(),
        }

        headers = { 
        }
        from gs2_money_client.control.CreatePlatformedItemRequest import CreatePlatformedItemRequest

        from gs2_money_client.control.CreatePlatformedItemResult import CreatePlatformedItemResult
        return CreatePlatformedItemResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "/platformedItem",
            service=self.ENDPOINT,
            module=CreatePlatformedItemRequest.Constant.MODULE,
            function=CreatePlatformedItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_item(self, request):
        """
        商品を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DeleteItemRequest.DeleteItemRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.DeleteItemRequest import DeleteItemRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "",
            service=self.ENDPOINT,
            module=DeleteItemRequest.Constant.MODULE,
            function=DeleteItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_money(self, request):
        """
        仮想通貨を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DeleteMoneyRequest.DeleteMoneyRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.DeleteMoneyRequest import DeleteMoneyRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "",
            service=self.ENDPOINT,
            module=DeleteMoneyRequest.Constant.MODULE,
            function=DeleteMoneyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_platformed_item(self, request):
        """
        プラットフォーム個別商品を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DeletePlatformedItemRequest.DeletePlatformedItemRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.DeletePlatformedItemRequest import DeletePlatformedItemRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "/platformedItem/" + str(("null" if request.get_platform() is None else request.get_platform())) + "",
            service=self.ENDPOINT,
            module=DeletePlatformedItemRequest.Constant.MODULE,
            function=DeletePlatformedItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_item(self, request):
        """
        商品の一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DescribeItemRequest.DescribeItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.DescribeItemResult.DescribeItemResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_money_client.control.DescribeItemRequest import DescribeItemRequest

        from gs2_money_client.control.DescribeItemResult import DescribeItemResult
        return DescribeItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item",
            service=self.ENDPOINT,
            module=DescribeItemRequest.Constant.MODULE,
            function=DescribeItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_money(self, request):
        """
        仮想通貨の一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DescribeMoneyRequest.DescribeMoneyRequest
        :return: 結果
        :rtype: gs2_money_client.control.DescribeMoneyResult.DescribeMoneyResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_money_client.control.DescribeMoneyRequest import DescribeMoneyRequest

        from gs2_money_client.control.DescribeMoneyResult import DescribeMoneyResult
        return DescribeMoneyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money",
            service=self.ENDPOINT,
            module=DescribeMoneyRequest.Constant.MODULE,
            function=DescribeMoneyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_platformed_item(self, request):
        """
        プラットフォーム個別商品の一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DescribePlatformedItemRequest.DescribePlatformedItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.DescribePlatformedItemResult.DescribePlatformedItemResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_money_client.control.DescribePlatformedItemRequest import DescribePlatformedItemRequest

        from gs2_money_client.control.DescribePlatformedItemResult import DescribePlatformedItemResult
        return DescribePlatformedItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "/platformedItem",
            service=self.ENDPOINT,
            module=DescribePlatformedItemRequest.Constant.MODULE,
            function=DescribePlatformedItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_receipt(self, request):
        """
        レシートを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DescribeReceiptRequest.DescribeReceiptRequest
        :return: 結果
        :rtype: gs2_money_client.control.DescribeReceiptResult.DescribeReceiptResult
        """

        query_strings = {

            'begin': request.get_begin(),

            'end': request.get_end(),

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_money_client.control.DescribeReceiptRequest import DescribeReceiptRequest

        from gs2_money_client.control.DescribeReceiptResult import DescribeReceiptResult
        return DescribeReceiptResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/receipt",
            service=self.ENDPOINT,
            module=DescribeReceiptRequest.Constant.MODULE,
            function=DescribeReceiptRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_receipt_by_user_and_slot(self, request):
        """
        指定したユーザ・スロット番号のレシートを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DescribeReceiptByUserAndSlotRequest.DescribeReceiptByUserAndSlotRequest
        :return: 結果
        :rtype: gs2_money_client.control.DescribeReceiptByUserAndSlotResult.DescribeReceiptByUserAndSlotResult
        """

        query_strings = {

            'begin': request.get_begin(),

            'end': request.get_end(),

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_money_client.control.DescribeReceiptByUserAndSlotRequest import DescribeReceiptByUserAndSlotRequest

        from gs2_money_client.control.DescribeReceiptByUserAndSlotResult import DescribeReceiptByUserAndSlotResult
        return DescribeReceiptByUserAndSlotResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/receipt/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "/" + str(("null" if request.get_slot() is None else request.get_slot())) + "",
            service=self.ENDPOINT,
            module=DescribeReceiptByUserAndSlotRequest.Constant.MODULE,
            function=DescribeReceiptByUserAndSlotRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_wallet(self, request):
        """
        ウォレット一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.DescribeWalletRequest.DescribeWalletRequest
        :return: 結果
        :rtype: gs2_money_client.control.DescribeWalletResult.DescribeWalletResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

            'userId': request.get_user_id(),

        }
        headers = { 
        }
        from gs2_money_client.control.DescribeWalletRequest import DescribeWalletRequest

        from gs2_money_client.control.DescribeWalletResult import DescribeWalletResult
        return DescribeWalletResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/wallet",
            service=self.ENDPOINT,
            module=DescribeWalletRequest.Constant.MODULE,
            function=DescribeWalletRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_item(self, request):
        """
        商品を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.GetItemRequest.GetItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.GetItemResult.GetItemResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.GetItemRequest import GetItemRequest

        from gs2_money_client.control.GetItemResult import GetItemResult
        return GetItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "",
            service=self.ENDPOINT,
            module=GetItemRequest.Constant.MODULE,
            function=GetItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_money(self, request):
        """
        仮想通貨を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.GetMoneyRequest.GetMoneyRequest
        :return: 結果
        :rtype: gs2_money_client.control.GetMoneyResult.GetMoneyResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.GetMoneyRequest import GetMoneyRequest

        from gs2_money_client.control.GetMoneyResult import GetMoneyResult
        return GetMoneyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "",
            service=self.ENDPOINT,
            module=GetMoneyRequest.Constant.MODULE,
            function=GetMoneyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_money_status(self, request):
        """
        仮想通貨の状態を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.GetMoneyStatusRequest.GetMoneyStatusRequest
        :return: 結果
        :rtype: gs2_money_client.control.GetMoneyStatusResult.GetMoneyStatusResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.GetMoneyStatusRequest import GetMoneyStatusRequest

        from gs2_money_client.control.GetMoneyStatusResult import GetMoneyStatusResult
        return GetMoneyStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/status",
            service=self.ENDPOINT,
            module=GetMoneyStatusRequest.Constant.MODULE,
            function=GetMoneyStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_platformed_item(self, request):
        """
        プラットフォーム個別商品を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.GetPlatformedItemRequest.GetPlatformedItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.GetPlatformedItemResult.GetPlatformedItemResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.GetPlatformedItemRequest import GetPlatformedItemRequest

        from gs2_money_client.control.GetPlatformedItemResult import GetPlatformedItemResult
        return GetPlatformedItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "/platformedItem/" + str(("null" if request.get_platform() is None else request.get_platform())) + "",
            service=self.ENDPOINT,
            module=GetPlatformedItemRequest.Constant.MODULE,
            function=GetPlatformedItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_wallet(self, request):
        """
        ウォレットを取得します<br>
        <br>
        ここでは有償仮想通貨と無償仮想通貨の数が取得できます。<br>
        有償仮想通貨は単価ごとに所持数量が別途管理されています。<br>
        詳細な構成を取得したい場合は Gs2Money:GetWalletDetail を使ってください。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.GetWalletRequest.GetWalletRequest
        :return: 結果
        :rtype: gs2_money_client.control.GetWalletResult.GetWalletResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_money_client.control.GetWalletRequest import GetWalletRequest

        from gs2_money_client.control.GetWalletResult import GetWalletResult
        return GetWalletResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/wallet/" + str(("null" if request.get_slot() is None else request.get_slot())) + "",
            service=self.ENDPOINT,
            module=GetWalletRequest.Constant.MODULE,
            function=GetWalletRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_wallet_detail(self, request):
        """
        ウォレットの詳細を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.GetWalletDetailRequest.GetWalletDetailRequest
        :return: 結果
        :rtype: gs2_money_client.control.GetWalletDetailResult.GetWalletDetailResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_money_client.control.GetWalletDetailRequest import GetWalletDetailRequest

        from gs2_money_client.control.GetWalletDetailResult import GetWalletDetailResult
        return GetWalletDetailResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/wallet/" + str(("null" if request.get_slot() is None else request.get_slot())) + "/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "/detail",
            service=self.ENDPOINT,
            module=GetWalletDetailRequest.Constant.MODULE,
            function=GetWalletDetailRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def update_item(self, request):
        """
        商品を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.UpdateItemRequest.UpdateItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.UpdateItemResult.UpdateItemResult
        """
        body = { 
            "count": request.get_count(),
        }

        headers = { 
        }
        from gs2_money_client.control.UpdateItemRequest import UpdateItemRequest

        from gs2_money_client.control.UpdateItemResult import UpdateItemResult
        return UpdateItemResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "",
            service=self.ENDPOINT,
            module=UpdateItemRequest.Constant.MODULE,
            function=UpdateItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def update_money(self, request):
        """
        仮想通貨を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.UpdateMoneyRequest.UpdateMoneyRequest
        :return: 結果
        :rtype: gs2_money_client.control.UpdateMoneyResult.UpdateMoneyResult
        """
        body = { 
            "priority": request.get_priority(),
            "useVerifyReceipt": request.get_use_verify_receipt(),
            "description": request.get_description(),
        }

        if request.get_google_key() is not None:
            body["googleKey"] = request.get_google_key()
        if request.get_apple_key() is not None:
            body["appleKey"] = request.get_apple_key()
        headers = { 
        }
        from gs2_money_client.control.UpdateMoneyRequest import UpdateMoneyRequest

        from gs2_money_client.control.UpdateMoneyResult import UpdateMoneyResult
        return UpdateMoneyResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "",
            service=self.ENDPOINT,
            module=UpdateMoneyRequest.Constant.MODULE,
            function=UpdateMoneyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def update_platformed_item(self, request):
        """
        プラットフォーム個別商品を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.UpdatePlatformedItemRequest.UpdatePlatformedItemRequest
        :return: 結果
        :rtype: gs2_money_client.control.UpdatePlatformedItemResult.UpdatePlatformedItemResult
        """
        body = { 
            "price": request.get_price(),
            "name": request.get_name(),
        }

        headers = { 
        }
        from gs2_money_client.control.UpdatePlatformedItemRequest import UpdatePlatformedItemRequest

        from gs2_money_client.control.UpdatePlatformedItemResult import UpdatePlatformedItemResult
        return UpdatePlatformedItemResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/item/" + str(("null" if request.get_item_name() is None else request.get_item_name())) + "/platformedItem/" + str(("null" if request.get_platform() is None else request.get_platform())) + "",
            service=self.ENDPOINT,
            module=UpdatePlatformedItemRequest.Constant.MODULE,
            function=UpdatePlatformedItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def verify(self, request):
        """
        レシートを検証する<br>
        <br>
        下記フォーマットのレシートをPOSTすることでレシートを検証し、仮想通貨のチャージまでアトミックに実行できます。<br>
        {<br>
          'Store': ストア名,<br>
          'Payload': レシート本体<br>
        }<br>
        <br>
        現在ストア名には<br>
        - AppleAppStore<br>
        - GooglePlay<br>
        が指定できます。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_money_client.control.VerifyRequest.VerifyRequest
        :return: 結果
        :rtype: gs2_money_client.control.VerifyResult.VerifyResult
        """
        body = { 
            "slot": request.get_slot(),
            "receipt": request.get_receipt(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_money_client.control.VerifyRequest import VerifyRequest

        from gs2_money_client.control.VerifyResult import VerifyResult
        return VerifyResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/money/" + str(("null" if request.get_money_name() is None else request.get_money_name())) + "/verify",
            service=self.ENDPOINT,
            module=VerifyRequest.Constant.MODULE,
            function=VerifyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

