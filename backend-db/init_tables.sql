CREATE TABLE IF NOT EXISTS champions (
   ChampionId INT PRIMARY KEY,
   Name VARCHAR(100)  NOT NULL,
   Title VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS Skins (
   SkinId int PRIMARY KEY,
   Name VARCHAR(100)  NOT NULL,
   Num int NOT NULL
);

CREATE TABLE IF NOT EXISTS Champions_Skins (
   ChampionId INT NOT NULL,
   SkinId INT NOT NULL,
   PRIMARY KEY (ChampionId, SkinId),
   FOREIGN KEY (ChampionId) REFERENCES Champions(ChampionId),
   FOREIGN KEY (SkinId) REFERENCES Skins(SkinId)
);

CREATE TABLE IF NOT EXISTS SkinPrices (
   SkinId INT NOT NULL,
   Price INT  NOT NULL,
   ChangedOn DATE NOT NULL,
   PRIMARY KEY (SkinId, ChangedOn),
   FOREIGN KEY (SkinId) REFERENCES Skins(SkinId)
);


INSERT INTO champions
VALUES 
(266, 'Aatrox', 'the Darkin Blade'), 
(103, 'Ahri', 'the Nine-Tailed Fox'),
(107, 'Rengar', 'the Pridestalker'),
(268, 'Azir', 'the Emperor of the Sands'),
(245, 'Ekko', 'the Boy Who Shattered Time');

INSERT INTO Skins
VALUES
(268005, 'Elderwood Azir', 5),
(268004, 'Warring Kingdoms Azir', 4),
(245001, 'Sandstorm Ekko', 1);

INSERT INTO Champions_Skins
VALUES
(268, 268005),
(268, 268004),
(245, 245001);

INSERT INTO SkinPrices
VALUES
(268005, 1820, '2023-02-10'),
(268005, 1500, '2023-02-09'),
(268005, 1820, '2023-02-01'),
(268004, 1820, '2023-02-09'),
(268004, 1520, '2023-02-01'),
(245001, 1820, '2023-02-09');