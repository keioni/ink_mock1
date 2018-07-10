

create table tokens (
    rowid integer auto_increment,
    token bigint,
    user_id integer,
    ctime datetime not null,
    primary key (token),
)

create table users (
    rowid integer auto_increment,
    user_id integer,
    user_name varchar(64),
    password varchar(64) not null,
    ctime datetime,
    mtime datetime,
    primary key (user_id),
    index index_username (username),
)

create table boxes (
    rowid integer auto_increment,
    box_id integer,
    user_id integer,
    box_name varchar(32) not null,
    ctime datetime,
    mtime datetime,
    cards_in_box blob(4096),
    primary key (box_id),
    index index_user (user_id),
)

create table cards (
    rowid integer auto_increment,
    card_id integer,
    box_id integer,
    user_id integer,
    card_name varchar(32) not null,
    ctime datetime,
    mtime datetime,
    records_in_card blob(4096),
    primary key (card_id),
    index index_user_box (user_id, box_id),
)

select * from boxes where user_id=$UID
select * from cards where user_id=$UID and box_id=$BID

insert into boxes (hogehoge)
update boxes set card_id = LAST_INSERT_ID() where rowid = LAST_INSERT_ID()
