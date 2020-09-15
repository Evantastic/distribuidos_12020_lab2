CREATE TABLE IF NOT EXISTS pipeline.deteccion (
    id uuid,
    objectid bigint,
    info map<text, double>,
    PRIMARY KEY (objectid, id)
);