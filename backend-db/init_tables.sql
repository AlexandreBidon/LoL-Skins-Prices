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
(245, 'Ekko', 'the Boy Who Shattered Time'),
(24, 'Jax', 'Grandmaster at Arms'),
(238, 'Zed', 'the Master of Shadows'),
(161, 'Vel''Koz', 'the Eye of the Void');

INSERT INTO Skins
VALUES
(268005, 'Elderwood Azir', 5),
(268004, 'Warring Kingdoms Azir', 4),
(245001, 'Sandstorm Ekko', 1),
(24005, 'Jaximus', 5),
(24014, 'Mecha Kingdoms Jax', 14),
(238003, 'PROJECT: Zed', 3),
(238013, 'Galaxy Slayer Zed', 13),
(103001, 'Dynasty Ahri', 1),
(103002, 'Midnight Ahri', 2),
(103003, 'Foxfire Ahri', 3),
(161004, 'Infernal Vel''Koz', 4);

INSERT INTO Champions_Skins
VALUES
(268, 268005),
(268, 268004),
(245, 245001),
(24, 24005),
(24, 24014),
(238, 238003),
(238, 238013),
(103, 103001),
(103, 103002),
(103, 103003),
(161, 161004);

INSERT INTO SkinPrices
VALUES
(268005, 1820, '2023-02-10'),
(268005, 1500, '2023-02-09'),
(268005, 1820, '2023-02-01'),
(268004, 1820, '2023-02-09'),
(268004, 1520, '2023-02-01'),
(245001, 1820, '2023-02-09'),
(24005, 1820, '2023-02-01'),
(24014, 1820, '2023-02-01'),
(238003, 1820, '2023-02-01'),
(238013, 1820, '2023-02-01'),
(103001, 1820, '2023-02-01'),
(103002, 1820, '2023-02-01'),
(103003, 1820, '2023-02-01'),
(161004, 1820, '2023-02-01');