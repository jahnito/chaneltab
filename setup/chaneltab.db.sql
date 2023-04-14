BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "address" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"area"	TEXT,
	"city"	TEXT,
	"street"	TEXT,
	"building"	TEXT,
	"region_id"	INTEGER,
	"area_id"	INTEGER
);

CREATE TABLE IF NOT EXISTS "areas" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"area_name"	TEXT UNIQUE
);

CREATE TABLE "main" (
	"id"	INTEGER,
	"address_id"	INTEGER,
	"type_channel_id"	INTEGER,
	"type_phys_channel_id"	INTEGER
);

CREATE TABLE "region" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT UNIQUE
);

CREATE TABLE "technical_possibility" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"service"	TEXT,
	"object_id"	INTEGER,
	"type_channel"	INTEGER,
	"type_phys_channel"	INTEGER
);

CREATE TABLE "type_channel" (
	"id"	INTEGER,
	"name"	TEXT
);

CREATE TABLE "type_phys_channel" (
	"id"	INTEGER,
	"name"	TEXT
);

COMMIT;
