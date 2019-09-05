CREATE DATABASE "acoustid";
CREATE DATABASE "acoustid_test";

CREATE DATABASE "acoustid_import";
CREATE DATABASE "acoustid_import_test";

\c acoustid
create extension intarray;
create extension pgcrypto;
create extension acoustid;
create extension cube;

\c acoustid_test
create extension intarray;
create extension pgcrypto;
create extension acoustid;
create extension cube;

\c acoustid_import
create extension intarray;
create extension pgcrypto;
create extension acoustid;
create extension cube;

\c acoustid_import_test
create extension intarray;
create extension pgcrypto;
create extension acoustid;
create extension cube;
