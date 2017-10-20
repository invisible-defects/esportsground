drop table if exists users;
create table users (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
