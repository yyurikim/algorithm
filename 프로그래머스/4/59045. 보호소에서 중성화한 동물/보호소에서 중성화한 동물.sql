SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE 'INTACT%' AND (O.SEX_UPON_OUTCOME LIKE 'SPAYED%' OR O.SEX_UPON_OUTCOME LIKE 'NEUTERED%')
ORDER BY I.ANIMAL_ID;