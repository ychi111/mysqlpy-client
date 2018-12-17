drop database octave;
create database octave;
use octave;

--Создание таблицы о зарегистрированных пользователях;
create table users(user_id tinyint(1) not null primary key, login char(20) not null, password char(20) not null, privileges tinyint(1));
insert into users values(0, 'admin', 'admin', 1);
insert into users values(1, "sec_adm", "hehmda123", 1);

--Создание таблицы о комнатах;
create table rooms(room_id tinyint(1) not null primary key, name char(10) not null, price int(4), size char(6) not null, status tinyint(1));
insert into rooms values(0, 'first', 800, '5x5m', 0);
insert into rooms values(1, 'second', 1400, '7x8m', 0);
insert into rooms values(2, 'third', 650, '4x5m', 0);

--Создание таблицы о сотрудниках;
create table employees(name char(20) not null, surname char(20), post char(50));
insert into employees values('Anton', 'Yakovlev', 'main admin');
	insert into employees values('neAnton', 'neYakovlev', 'database_manager');

--Информация об оборудовании в комнатах;
create table room_equip(room_id tinyint(1) not null, drums char(100) not null, guitar_amp1 char(100), guitar_amp2 char(100), bass_amp char(100));
insert into room_equip values(0, 'Sonor 2007', 'Laney GH100TI & 4x12"+2х12" Yerasov cab ', 'Mesa Boogie Dual Rectifier & Randall 4x12" cab', 'Ampeg SVT450 & Ampeg 6x10 cab ');
insert into room_equip values(1, 'DDrum Reflex Uptown', 'Marshall JCM900 & Marhall 1960 twin 4x12" cab', 'Mesa Boogie Triple Rectifier & twin 4x12" cab', 'Gallien-Krueger 1001rb & Gallien-Krueger 8x10" cab');
insert into room_equip values(2, 'Sonor 2005', 'Marshall AVT150 & Marshall 4x12" cab', 'Peavey ValveKing & 4x12" cab', 'Warwick ProFet 5.2 & 4x10"+1x15" cab');

--Информация о текущих бронированиях;
create table cur_status(user_id tinyint(1) not null, room_id tinyint(1) not null, time date not null);
