from flask import Blueprint, request
import json as json_lib

from repository import coupon as coupon_repo
from utils.response import DefaultResponse
from tasks import get_buyers_data

couponBlueprint = Blueprint('coupons', __name__)

@couponBlueprint.route('/', methods=['POST'])
def create():
    try:
        json = request.json

        result = coupon_repo.create(json)

        result['products'] = []

        for product in json['products']:
            product['couponId'] = result['couponId']

            product_result = coupon_repo.create_coupon_product(product)

            result['products'].append(product_result)

        get_buyers_data.delay(json_lib.dumps(result))
        
        return DefaultResponse(result, 201)
    except Exception as e:
        return DefaultResponse({'error': str(e)}, 400)