BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "region" (
	"id"	INTEGER,
	"name"	TEXT
);
CREATE TABLE IF NOT EXISTS "address" (
	"id"	INTEGER,
	"root_to"	TEXT,
	"city"	TEXT,
	"street"	TEXT,
	"building"	TEXT,
	"region_id"	INTEGER
);
CREATE TABLE IF NOT EXISTS "type_phys_channel" (
	"id"	INTEGER,
	"name"	TEXT
);
CREATE TABLE IF NOT EXISTS "type_channel" (
	"id"	INTEGER,
	"name"	TEXT
);
CREATE TABLE IF NOT EXISTS "main" (
	"id"	INTEGER,
	"address_id"	INTEGER,
	"type_channel_id"	INTEGER,
	"type_phys_channel_id"	INTEGER
);
COMMIT;
