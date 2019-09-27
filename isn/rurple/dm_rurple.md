# DM RURPLE

## Énoncé de la mission :
Dans un monde aux dimensions aléatoires, des sonnettes sont disposées au hasard.
Rurple doit ramasser ces sonnettes puis les positionner dans les angles de ce monde (il y a autant de sonnettes que d'angles dans le monde).
Votre programme doit pouvoir fonctionner dans n'importe quel monde.

## Ma façon de procéder

D’après la consigne je comprends que Purple doit être capable de placer une sonnette dans les coins de chaque n’importe quel monde en utilisant uniquement des sonnettes récupérées sur ce monde. Par n’importe quel monde j’entends n’importe quel monde où il est existe une solution au problème (càd que Rurple a accès à assez de sonnettes et que l’on parle de coins accessibles). Dans ces conditions la solution la plus simple qui fonctionnerait à chaque fois me semble d’être de parcourir le monde <u>**entièrement**</u> dans le but de trouver toutes les sonnettes, puis de chercher à placer une sonnette dans chaque coin du monde.

## Comment parcourir le monde entièrement ?

