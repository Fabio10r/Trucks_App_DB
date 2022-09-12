CREATE TABLE IF NOT EXISTS public.trucks
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default",
    postCode character varying COLLATE pg_catalog."default",
    phone character varying COLLATE pg_catalog."default",
    country character varying COLLATE pg_catalog."default",
    county character varying COLLATE pg_catalog."default",
    long character varying COLLATE pg_catalog."default",
    lat character varying COLLATE pg_catalog."default",
    hasSpecialCharacters boolean,
    noSpecialCharacters character varying COLLATE pg_catalog."default",
    CONSTRAINT "Trucks_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.trucks
    OWNER to postgres;