BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "address" (
	"id"	INTEGER,
	"area_id"	INTEGER,
	"city"	TEXT,
	"street"	TEXT,
	"building"	TEXT,
	"region_id"	INTEGER,
	"area_owner"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "areas" (
	"id"	INTEGER UNIQUE,
	"area_name"	TEXT UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "areas_owners" (
	"id"	INTEGER UNIQUE,
	"area_name"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
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
