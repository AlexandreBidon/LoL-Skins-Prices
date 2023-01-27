CREATE TABLE IF NOT EXISTS Champions (
   ChampionId int PRIMARY KEY,
   Name VARCHAR(100)  NOT NULL
);

CREATE TABLE IF NOT EXISTS Skins (
   SkinId int PRIMARY KEY,
   Name VARCHAR(100)  NOT NULL,
   Num int NOT NULL
);

CREATE TABLE IF NOT EXISTS Champions_Skins (
   ChampionId int NOT NULL,
   SkinId int NOT NULL,
   PRIMARY KEY (ChampionId, SkinId),
   FOREIGN KEY (ChampionId) REFERENCES Champions(ChampionId),
   FOREIGN KEY (SkinId) REFERENCES Skins(SkinId)
);

CREATE TABLE IF NOT EXISTS SkinPrices (
   SkinId int NOT NULL,
   Price int  NOT NULL,
   ChangedOn DATE NOT NULL,
   PRIMARY KEY (SkinId, ChangedOn),
   FOREIGN KEY (SkinId) REFERENCES Skins(SkinId)
);