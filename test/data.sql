insert into accounts (name, password) values
    ("account1", "pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f"),
    ("account2", "pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79");

insert into products (code, name, type, account_id) values
    ("601318", "中国平安", "STOCK", 1),
    ("050002", "博时沪深300指数A", "FUND", 1),
    ("601318", "中国平安", "STOCK", 2);

-- insert into trades (product_id, side, price, quantity, datetime) values
--     (1, "BUY", 10.5, 100, "2022-01-01"),
--     (1, "SELL", 5, 50, "2022-05-01"),
--     (2, "BUY", 23.1, 345, "2022-03-01");

-- 601318
insert into trades (product_id, side, price, quantity, datetime) values
    (1, "BUY", 51.1, 200, "2022-03-01"),
    (1, "SELL", 50.9, 100, "2022-03-03"),
    (1, "BUY", 49.2, 400, "2022-03-07"),
    (1, "SELL", 47.9, 300, "2022-03-09"),
    (1, "BUY", 46.0, 800, "2022-03-11");

-- 050002
insert into trades (product_id, side, price, quantity, datetime) values
    (2, "BUY", 1.7652, 10000, "2022-03-01");
