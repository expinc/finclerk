pragma encoding = 'UTF-8';

drop table if exists accounts;
create table accounts (
    id integer primary key autoincrement,
    account_name text unique not null,
    password text not null
);

drop table if exists products;
create table products (
    id integer primary key autoincrement,
    code text unique not null,
    name text not null,
    type text not null,
    account_id integer not null,
    foreign key (account_id) references accounts (id)
);

drop table if exists trades;
create table trades (
    id integer primary key autoincrement,
    product_id integer not null,
    side text not null,
    price real not null,
    quantity real not null,
    datetime text not null,
    foreign key (product_id) references products (id)
);
