

create table tokens (
    token bigint primary key,
    user_id integer,
    ctime datetime not null,
)

create table users (
    user_id integer primary key auto increment,
    username varchar(64) primary key,
    password varchar(64) not null,
    ctime datetime,
    mtime datetime,
)

create table boxes (
    user_id integer,
    box_id integer,
    box_name varchar(32) not null,
    ctime datetime,
    mtime datetime,
    cards_in_box blob(4096),
)

create table cards (
    card_id integer primary key auto increment,
    card_name varchar(32) not null,
    ctime datetime,
    mtime datetime,
    card_caption varchar(64),
)

