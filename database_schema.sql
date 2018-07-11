

create table tokens (
    rowid integer auto_increment,
    token bigint,
    user_num integer,
    ctime datetime not null,
    primary key (token),
)

create table users (
    user_num integer auto_increment,
    user_id varchar(64),
    password varchar(64) not null,
    ctime datetime,
    mtime datetime,
    primary key (user_num),
    index index_id (user_id),
)

create table boxes (
    box_num integer auto_increment,
    user_num integer,
    box_title varchar(32) not null,
    ctime datetime,
    mtime datetime,
    primary key (box_num),
    index index_user (user_num),
)

create table cards (
    card_num integer auto_increment,
    box_num integer,
    user_num integer,
    card_title varchar(32) not null,
    ctime datetime,
    mtime datetime,
    recent_records char(340),
    primary key (card_num),
    index index_user_box (user_num, box_num),
)

create table records (
    rowid integer auto_increment,
    card_num integer,
    record char(16),
    primary key (rowid),
    index index_card (card_num),
)

select * from boxes where user_num=$UID
select * from cards where user_num=$UID
select * from cards where user_num=$UID and box_num=$BID
select record from records where card_num=$CID
