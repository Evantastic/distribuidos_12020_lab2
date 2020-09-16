CREATE TABLE IF NOT EXISTS pipeline.deteccion (
    id uuid,
    objectid text,
    info map<text, double>,
    PRIMARY KEY (objectid, id)
);
