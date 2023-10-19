ALTER TABLE <table name>(
ADD CONSTRAINT <constraint name> FORIEGN KEY <attribute list>
REFERENCE <parent table name> (<attribute list>);
)