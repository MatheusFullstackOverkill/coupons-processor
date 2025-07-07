from sqlalchemy.sql import text
from utils.sqlalchemy_serializer import fetchone

from db import db_engine


def create(data):
    conn = db_engine.connect()

    result = conn.execute(
        text('''
            INSERT INTO coupon (
                code44,
                purchaseDate,
                totalValue,
                companyDocument,
                State
            ) VALUES (
                :code44,
                :purchaseDate,
                :totalValue,
                :companyDocument,
                :State
            ) RETURNING
                couponId as "couponId",
                code44,
                purchaseDate,
                totalValue,
                companyDocument,
                State
        '''), **data)

    conn.close()

    return fetchone(result)

def create_coupon_product(data):
    conn = db_engine.connect()

    result = conn.execute(
        text('''
            INSERT INTO coupon_product (
                couponId,
                name,
                ean,
                unitaryPrice,
                quantity
            ) VALUES (
                :couponId,
                :name,
                :ean,
                :unitaryPrice,
                :quantity
            ) RETURNING
                name,
                ean,
                unitaryPrice,
                quantity
        '''), **data)

    conn.close()

    return fetchone(result)

