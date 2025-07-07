CREATE TABLE IF NOT EXISTS coupon (
    couponId SERIAL PRIMARY KEY NOT NULL,
    code44 VARCHAR(44),
    purchaseDate TIMESTAMP,
    totalValue INT,
    companyDocument VARCHAR(50),
    State VARCHAR(2),
    createdAt TIMESTAMP DEFAULT NOW(),
    deletedAt TIMESTAMP
);

CREATE TABLE IF NOT EXISTS coupon_product (
    couponProductId SERIAL PRIMARY KEY NOT NULL,
    couponId INT,
    name VARCHAR(100),
    ean VARCHAR(44),
    unitaryPrice INT,
    quantity INT,
    createdAt TIMESTAMP DEFAULT NOW(),
    deletedAt TIMESTAMP,
    CONSTRAINT fk_coupon
    FOREIGN KEY(couponId) 
      REFERENCES coupon(couponId)
);