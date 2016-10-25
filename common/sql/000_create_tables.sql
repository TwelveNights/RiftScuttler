-- Entities

CREATE TABLE champions (
  name      VARCHAR(16),
  category  VARCHAR(10),
  PRIMARY KEY (name)
);

CREATE TABLE series (
  id          INTEGER,
  bestOfCount INTEGER NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE items (
  id          INTEGER,
  name        TEXT      NOT NULL,
  basePrice   INTEGER   NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE players (
  id                INTEGER,
  name              VARCHAR(16) NOT NULL,
  careerStartDate   DATETIME    NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE teams (
  id        VARCHAR(6),
  region    VARCHAR(2),
  name      TEXT NOT NULL,
  PRIMARY KEY (id, region)
);

CREATE TABLE tournaments (
  id        VARCHAR(256),
  year      INTEGER,
  location  TEXT    NOT NULL,
  prize     INTEGER NOT NULL,
  PRIMARY KEY (id, year)
);

CREATE TABLE matches (
  seriesID    INTEGER,
  matchNumber INTEGER,
  date        DATETIME  NOT NULL,
  PRIMARY KEY (seriesID, matchNumber),
  FOREIGN KEY (seriesID) REFERENCES series(id)
);

-- Relations

CREATE TABLE bans (
  seriesID        INTEGER,
  matchNumber   INTEGER,
  name          VARCHAR(16),
  PRIMARY KEY (seriesID, matchNumber, name),
  FOREIGN KEY (name)    REFERENCES  champions(name),
  FOREIGN KEY (seriesID, matchNumber)  REFERENCES  matches(seriesID, matchNumber)
);

CREATE TABLE organizes (
  tournamentID  VARCHAR(256),
  year          INTEGER,
  seriesID      INTEGER,
  stage         TEXT,
  PRIMARY KEY (tournamentID, year, seriesID),
  FOREIGN KEY (tournamentID, year)  REFERENCES tournaments(id, year),
  FOREIGN KEY (seriesID)              REFERENCES games(id)
);

CREATE TABLE competes (
  seriesID        INTEGER,
  team1ID         VARCHAR(6),
  team1Region     VARCHAR(2),
  team2ID         VARCHAR(6),
  team2Region     VARCHAR(2),
  winner    VARCHAR(2),
  CHECK (winner = team1ID OR winner = team2ID),
  PRIMARY KEY (seriesID, team1ID, team1Region, team2ID, team2Region),
  FOREIGN KEY (seriesID) REFERENCES series(id),
  FOREIGN KEY (team1Region, team1ID) REFERENCES teams(region, id),
  FOREIGN KEY (team2Region, team2ID) REFERENCES teams(region, id)
);

CREATE TABLE interacts (
  seriesID      INTEGER,
  matchNumber INTEGER,
  playerID    INTEGER,
  itemID      INTEGER,
  time        INTEGER,
  isBuy       BOOLEAN NOT NULL,
  spent       INTEGER NOT NULL,
  PRIMARY KEY (seriesID, matchNumber, playerID, itemID, time),
  FOREIGN KEY (seriesID, matchNumber) REFERENCES matches(seriesID, matchNumber),
  FOREIGN KEY (playerID)            REFERENCES players(id),
  FOREIGN KEY (itemID)              REFERENCES items(id)
);

CREATE TABLE participates (
  tournamentID  VARCHAR(256),
  teamID        VARCHAR(6),
  teamRegion    VARCHAR(2),
  year          INTEGER,
  stageReached  TEXT NOT NULL,
  PRIMARY KEY (tournamentID, teamID, teamRegion, year),
  FOREIGN KEY (tournamentID, year) REFERENCES tournaments(id, year),
  FOREIGN KEY (teamID, teamRegion) REFERENCES teams(id, region)
);

CREATE TABLE plays (
  seriesID      INTEGER,
  matchNumber INTEGER,
  playerID    INTEGER,
  champion    VARCHAR(16),
  role        VARCHAR(6)    NOT NULL,
  kills       INTEGER       NOT NULL,
  deaths      INTEGER       NOT NULL,
  assists     INTEGER       NOT NULL,
  damageDealt INTEGER       NOT NULL,
  wardsPlaced INTEGER       NOT NULL,
  gold        INTEGER       NOT NULL,
  PRIMARY KEY (seriesID, matchNumber, playerID, champion),
  FOREIGN KEY (seriesID, matchNumber) REFERENCES matches(seriesID, matchNumber),
  FOREIGN KEY (playerID)            REFERENCES players(id),
  FOREIGN KEY (champion)            REFERENCES champions(name)
);

CREATE TABLE registers (
  playerID    INTEGER,
  teamID      VARCHAR(6),
  teamRegion  VARCHAR(2),
  dateJoined  DATE        NOT NULL,
  dateLeft    DATE,
  PRIMARY KEY (playerID, teamID, teamRegion),
  FOREIGN KEY (playerID)           REFERENCES players(id),
  FOREIGN KEY (teamID, teamRegion) REFERENCES teams(id, region)
);

CREATE TABLE scores (
  teamID      VARCHAR(6),
  teamRegion  VARCHAR(6),
  seriesID      INTEGER,
  matchNumber INTEGER,
  inhibitors  INTEGER NOT NULL,
  towers      INTEGER NOT NULL,
  riftHeralds INTEGER NOT NULL,
  barons      INTEGER NOT NULL,
  dragons     INTEGER NOT NULL,
  nexus       INTEGER NOT NULL,
  CHECK (nexus = 0 OR nexus = 1),
  PRIMARY KEY (teamID, teamRegion, seriesID, matchNumber),
  FOREIGN KEY (teamID, teamRegion)   REFERENCES teams(id, region),
  FOREIGN KEY (seriesID, matchNumber)  REFERENCES matches(seriesID, matchNumber)
);
