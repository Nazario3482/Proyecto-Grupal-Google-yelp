## DICIONARIO DE DATOS

>### Tabla "reviews"

>**user_id:** STRING (PK)
-> identificador unico de usuario

>**business_id:** STRING (FK)

>**rating:** INTEGER

>**timestamp:** TIMESTAMP

>**sentiment_analysis:** INTEGER

### Tabla "business"

**business_id:** STRING (PK)

**name:** STRING

**latitude:** FLOAT

**longitude:** FLOAT

**category:** STRING

**avg_rating:** FLOAT

**num_of_reviews:** INTEGER