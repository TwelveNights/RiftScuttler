-- Entities

CREATE TABLE champions (
  id        INTEGER,
  name      VARCHAR(16) NOT NULL UNIQUE,
  PRIMARY KEY (id)
);

CREATE TABLE series (
  id          INTEGER,
  bestOfCount INTEGER NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE items (
  id          INTEGER,
  name        VARCHAR(64) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE players (
  name              VARCHAR(16) NOT NULL,
  careerStartDate   DATE,
  PRIMARY KEY (name)
);

CREATE TABLE teams (
  id        VARCHAR(6),
  region    VARCHAR(2),
  name      TEXT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE tournaments (
  id        VARCHAR(16),
  name      VARCHAR(256),
  year      INTEGER,
  location  TEXT    NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE matches (
  seriesID    INTEGER,
  matchNumber INTEGER,
  matchDate   DATE  NOT NULL,
  PRIMARY KEY (seriesID, matchNumber),
  FOREIGN KEY (seriesID) REFERENCES series(id) ON DELETE CASCADE
);

CREATE TABLE wins (
  teamID    VARCHAR(6),
  wins      INTEGER NOT NULL,
  CHECK (wins >= 0),
  PRIMARY KEY (teamID),
  FOREIGN KEY (teamID) REFERENCES teams(id)
);

-- Relations

-- Add ban order?
CREATE TABLE bans (
  seriesID      INTEGER,
  matchNumber   INTEGER,
  championID    INTEGER,
  pickTurn      INTEGER,
  PRIMARY KEY (seriesID, matchNumber, championID),
  FOREIGN KEY (championID)    REFERENCES  champions(id) ON DELETE CASCADE,
  FOREIGN KEY (seriesID, matchNumber)  REFERENCES  matches(seriesID, matchNumber) ON DELETE CASCADE
);

CREATE TABLE organizes (
  tournamentID  VARCHAR(256),
  seriesID      INTEGER,
  stage         TEXT,
  PRIMARY KEY (tournamentID, seriesID),
  FOREIGN KEY (tournamentID)  REFERENCES tournaments(id) ON DELETE CASCADE,
  FOREIGN KEY (seriesID)      REFERENCES series(id) ON DELETE CASCADE
);

CREATE TABLE competes (
  seriesID        INTEGER,
  teamID          VARCHAR(6),
  blueSide        BOOLEAN,
  PRIMARY KEY (seriesID, teamID),
  FOREIGN KEY (seriesID) REFERENCES series(id) ON DELETE CASCADE,
  FOREIGN KEY (teamID) REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE interacts (
  seriesID    INTEGER,
  matchNumber INTEGER,
  player      VARCHAR(16),
  itemID      INTEGER,
  time        INTEGER,
  isBuy       INTEGER,
  CHECK (isBuy = 0 OR isBuy = 1),
  PRIMARY KEY (seriesID, matchNumber, player, itemID, time),
  FOREIGN KEY (seriesID, matchNumber) REFERENCES matches(seriesID, matchNumber) ON DELETE CASCADE,
  FOREIGN KEY (player)            REFERENCES players(name) ON DELETE CASCADE,
  FOREIGN KEY (itemID)              REFERENCES items(id) ON DELETE RESTRICT
);

CREATE TABLE participates (
  tournamentID  VARCHAR(256),
  teamID        VARCHAR(6),
  stageReached  TEXT NOT NULL,
  PRIMARY KEY (tournamentID, teamID),
  FOREIGN KEY (tournamentID) REFERENCES tournaments(id) ON DELETE CASCADE,
  FOREIGN KEY (teamID) REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE plays (
  seriesID        INTEGER,
  matchNumber     INTEGER,
  player    VARCHAR(16),
  championID      INTEGER,
  role            VARCHAR(6)    NOT NULL,
  kills           INTEGER       NOT NULL,
  deaths          INTEGER       NOT NULL,
  assists         INTEGER       NOT NULL,
  damageDealt     INTEGER       NOT NULL,
  wardsPlaced     INTEGER       NOT NULL,
  wardsDestroyed  INTEGER    NOT NULL,
  cs              INTEGER       NOT NULL,
  teamJungleMinions INTEGER NOT NULL,
  enemyJungleMinions INTEGER NOT NULL,
  gold        INTEGER       NOT NULL,
  PRIMARY KEY (seriesID, matchNumber, player, championID),
  FOREIGN KEY (seriesID, matchNumber) REFERENCES matches(seriesID, matchNumber) ON DELETE CASCADE,
  FOREIGN KEY (player)            REFERENCES players(name) ON DELETE CASCADE,
  FOREIGN KEY (championID)            REFERENCES champions(id) ON DELETE CASCADE
);

CREATE TABLE registers (
  player    VARCHAR(16),
  teamID      VARCHAR(6),
  dateJoined  DATE        NOT NULL,
  dateLeft    DATE,
  PRIMARY KEY (player, teamID),
  FOREIGN KEY (player) REFERENCES players(name) ON DELETE CASCADE,
  FOREIGN KEY (teamID) REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE scores (
  teamID      VARCHAR(6),
  seriesID    INTEGER,
  matchNumber INTEGER,
  inhibitors  INTEGER NOT NULL,
  towers      INTEGER NOT NULL,
  riftHeralds INTEGER NOT NULL,
  barons      INTEGER NOT NULL,
  dragons     INTEGER NOT NULL,
  nexus       INTEGER NOT NULL,
  CHECK (nexus = 0 OR nexus = 1),
  PRIMARY KEY (teamID, seriesID, matchNumber),
  FOREIGN KEY (teamID)   REFERENCES teams(id) ON DELETE CASCADE,
  FOREIGN KEY (seriesID, matchNumber)  REFERENCES matches(seriesID, matchNumber) ON DELETE CASCADE
);


-- Triggers

CREATE TRIGGER trigger_add_team_to_wins AFTER INSERT
ON teams
BEGIN
   INSERT INTO wins(teamID, wins) VALUES (new.id, 0);
END;


CREATE TRIGGER trigger_delete_teams_from_win AFTER DELETE
ON teams
BEGIN
   DELETE FROM wins WHERE teamID=OLD.id;
END;


CREATE TRIGGER trigger_update_wins_on_adding_scores AFTER INSERT
ON scores
WHEN NEW.nexus = 1
BEGIN
    UPDATE wins SET wins=wins+1 WHERE teamID=NEW.teamID;
END;

CREATE TRIGGER trigger_update_wins_on_deleting_scores AFTER DELETE
ON scores
WHEN OLD.nexus = 1
BEGIN
    UPDATE wins SET wins=wins-1 WHERE teamID=OLD.teamID;
END;

CREATE TRIGGER trigger_update_wins_on_updating_scores1 AFTER UPDATE
ON scores
WHEN NEW.nexus = 1 AND OLD.nexus = 0
BEGIN
    UPDATE wins SET wins=wins+1 WHERE teamID=OLD.teamID;
END;

CREATE TRIGGER trigger_update_wins_on_updating_scores2 AFTER UPDATE
ON scores
WHEN NEW.nexus = 0 AND OLD.nexus = 1
BEGIN
    UPDATE wins SET wins=wins-1 WHERE teamID=NEW.teamID;
END;
