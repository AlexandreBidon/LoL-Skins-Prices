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
VALUES (266, 'Aatrox', 'the Darkin Blade'), (103, 'Ahri', 'the Nine-Tailed Fox');