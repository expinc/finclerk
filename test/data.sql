insert into accounts (name, password) values
    ("account1", "pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f"),
    ("account2", "pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79");

insert into products (code, name, type, account_id) values
    ("code1", "product1", "STOCK", 1),
    ("code2", "product2", "FUND", 1),
    ("code3", "product3", "FUTURE", 2);

insert into trades (product_id, side, price, quantity, datetime) values
    (1, "BUY", 10.5, 100, "2021-01-01"),
    (1, "SELL", 5, 50, "2021-05-01"),
    (2, "BUY", 23.1, 345, "2021-03-01");
