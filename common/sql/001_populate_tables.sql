INSERT INTO tournaments (id, name, year, location, prize)
VALUES ('worlds2015', 'World Championship', 2015, 'Europe', 2130000);

-- Champions:

INSERT INTO champions (name, category)
VALUES ('Amumu', 'tank');

INSERT INTO champions (name, category)
VALUES ('Blitzcrank', 'tank');

INSERT INTO champions (name, category)
VALUES ('Caitlyn', 'marksman');

INSERT INTO champions (name, category)
VALUES ('Darius', 'fighter');

INSERT INTO champions (name, category)
VALUES ('Galio', 'marksman');

INSERT INTO champions (name, category)
VALUES ('Garen', 'fighter');

INSERT INTO champions (name, category)
VALUES ('Graves', 'marksman');

INSERT INTO champions (name, category)
VALUES ('Jinx', 'mage');

INSERT INTO champions (name, category)
VALUES ('Nami', 'assassin');

INSERT INTO champions (name, category)
VALUES ('Nidalee', 'assassin');

INSERT INTO champions (name, category)
VALUES ('Soraka', 'support');

INSERT INTO champions (name, category)
VALUES ('Thresh', 'support');

INSERT INTO champions (name, category)
VALUES ('Tristana', 'marksman');

INSERT INTO champions (name, category)
VALUES ('Twisted Fate', 'mage');

INSERT INTO champions (name, category)
VALUES ('Zac', 'tank');

INSERT INTO champions (name, category)
VALUES ('Zed', 'assassin');


--Items:

INSERT INTO items (id, name, basePrice)
VALUES (1, 'Quicksilver Sash', 2300);

INSERT INTO items (id, name, basePrice)
VALUES (2, 'Essence Reaver', 400);

INSERT INTO items (id, name, basePrice)
VALUES (3, 'Hextech Gunblade', 2900);

INSERT INTO items (id, name, basePrice)
VALUES (4, 'Amplifying Tome', 2300);

INSERT INTO items (id, name, basePrice)
VALUES (5, 'Statikk Shiv', 1900);


-- Teams in Worlds 2015:


-- AHQ

INSERT INTO teams (id, region, name)
VALUES ('AHQ', 'LMS', 'ahq e-Sports Club');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'AHQ', 'quarterfinals');


INSERT INTO players (id, name, careerStartDate)
VALUES (2, 'Ziv', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (3, 'Mountain', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (4, 'Westdoor', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (5, 'An', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (6, 'Albis', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (2, 'AHQ', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (3, 'AHQ', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (4, 'AHQ', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (5, 'AHQ', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (6, 'AHQ', 1980-01-01, 1980-01-02);


--Bangkok Titans

INSERT INTO teams (id, region, name)
VALUES ('BKT', 'IWC', 'Bangkok Titans');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'BKT', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (12, 'WarL0ck', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (13, '007x', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (14, 'G4', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (15, 'Lloyd', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (16, 'Moss', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (12, 'BKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (13, 'BKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (14, 'BKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (15, 'BKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (16, 'BKT', 1980-01-01, 1980-01-02);


-- Cloud 9

INSERT INTO teams (id, region, name)
VALUES ('C9', 'NA', 'Cloud 9');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'C9', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (17, 'Balls', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (18, 'Hai', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (19, 'Incarnati0n', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (20, 'Sneaky', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (21, 'LemonNation', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (17, 'C9', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (18, 'C9', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (19, 'C9', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (20, 'C9', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (21, 'C9', 1980-01-01, 1980-01-02);

-- Counter Logic Gaming

INSERT INTO teams (id, region, name)
VALUES ('CLG', 'NA', 'Counter Logic Gaming');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'CLG', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (122, 'ZionSpartan', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (123, 'Xmithie', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (124, 'Pobelter', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (125, 'Doublelift', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (126, 'Aphromoo', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (122, 'CLG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (123, 'CLG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (124, 'CLG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (125, 'CLG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (126, 'CLG', 1980-01-01, 1980-01-02);

--Edward Gaming

INSERT INTO teams (id, region, name)
VALUES ('EDG', 'LPL', 'Edward Gaming');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'EDG', 'quarterfinals');


INSERT INTO players (id, name, careerStartDate)
VALUES (132, 'Koro1', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (133, 'Clearlove', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (134, 'PawN', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (135, 'Deft', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (136, 'Meiko', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (132, 'EDG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (133, 'EDG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (134, 'EDG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (135, 'EDG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (136, 'EDG', 1980-01-01, 1980-01-02);

-- Fnatic

INSERT INTO teams (id, region, name)
VALUES ('FNC', 'EU', 'Fnatic');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'FNC', 'semifinals');


INSERT INTO players (id, name, careerStartDate)
VALUES (127, 'Huni', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (128, 'Reignover', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (129, 'Febiven', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (130, 'Rekkles', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (131, 'YellOwStaR', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (127, 'FNC', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (128, 'FNC', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (129, 'FNC', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (130, 'FNC', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (131, 'FNC', 1980-01-01, 1980-01-02);

-- Flash Wolves

INSERT INTO teams (id, region, name)
VALUES ('FW', 'LMS', 'Flash Wolves');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'FW', 'quarterfinals');


INSERT INTO players (id, name, careerStartDate)
VALUES (27, 'Steak', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (28, 'Karsa', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (29, 'Maple', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (30, 'NL', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (31, 'SwordArt', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (27, 'FW', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (28, 'FW', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (29, 'FW', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (30, 'FW', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (31, 'FW', 1980-01-01, 1980-01-02);


-- H2K

INSERT INTO teams (id, region, name)
VALUES ('H2K', 'EU', 'H2k');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'H2K', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (37, 'Odoamne', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (38, 'loulex', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (39, 'Ryu', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (40, 'Hjarnan', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (41, 'KaSing', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (37, 'H2K', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (38, 'H2K', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (39, 'H2K', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (40, 'H2K', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (41, 'H2K', 1980-01-01, 1980-01-02);

-- Invictus Gaming

INSERT INTO teams (id, region, name)
VALUES ('IG', 'LPL', 'Invictus Gaming');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'IG', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (47, 'Zzitai', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (48, 'KaKAO', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (49, 'RooKie', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (50, 'Kid', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (51, 'Kitties', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (47, 'IG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (48, 'IG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (49, 'IG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (50, 'IG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (51, 'IG', 1980-01-01, 1980-01-02);

-- Koo Tigers

INSERT INTO teams (id, region, name)
VALUES ('KOO', 'LCK', 'Koo Tigers');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'KOO', 'finals');


INSERT INTO players (id, name, careerStartDate)
VALUES (57, 'Smeb', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (58, 'hojin', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (59, 'Kuro', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (60, 'PraY', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (61, 'GorillA', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (57, 'KOO', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (58, 'KOO', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (59, 'KOO', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (60, 'KOO', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (61, 'KOO', 1980-01-01, 1980-01-02);

-- KT Rollster

INSERT INTO teams (id, region, name)
VALUES ('KT', 'LCK', 'KT Rollster');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'KT', 'quarterfinals');


INSERT INTO players (id, name, careerStartDate)
VALUES (67, 'Ssumday', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (68, 'Score', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (69, 'Nagne', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (70, 'Arrow', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (71, 'Piccaboo', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (67, 'KT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (68, 'KT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (69, 'KT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (70, 'KT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (71, 'KT', 1980-01-01, 1980-01-02);

-- LGD Gaming

INSERT INTO teams (id, region, name)
VALUES ('LGD', 'LPL', 'LGD Gaming');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'LGD', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (77, 'Acorn', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (78, 'TBQ', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (79, 'GODV', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (80, 'imp', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (81, 'Pyl', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (77, 'LGD', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (78, 'LGD', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (79, 'LGD', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (80, 'LGD', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (81, 'LGD', 1980-01-01, 1980-01-02);

-- Origen

INSERT INTO teams (id, region, name)
VALUES ('OG', 'EU', 'Origen');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'OG', 'semifinals');


INSERT INTO players (id, name, careerStartDate)
VALUES (87, 'sOAZ', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (88, 'Amazing', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (89, 'xPeke', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (90, 'Niels', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (91, 'Mithy', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (87, 'OG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (88, 'OG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (89, 'OG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (90, 'OG', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (91, 'OG', 1980-01-01, 1980-01-02);

-- paiN Gaming

INSERT INTO teams (id, region, name)
VALUES ('PAIN', 'IWC', 'paiN Gaming');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'PAIN', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (117, 'Mylon', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (118, 'SirT', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (119, 'Kami', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (120, 'brTT', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (121, 'Dioud', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (117, 'PAIN', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (118, 'PAIN', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (119, 'PAIN', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (120, 'PAIN', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (121, 'PAIN', 1980-01-01, 1980-01-02);

-- SK Telecom T1

INSERT INTO teams (id, region, name)
VALUES ('SKT', 'LCK', 'SK Telecom T1');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'SKT', 'finals');


INSERT INTO players (id, name, careerStartDate)
VALUES (97, 'MaRin', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (98, 'bengi', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (1, 'Faker', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (100, 'Bang', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (101, 'Wolf', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (97, 'SKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (98, 'SKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (99, 'SKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (100, 'SKT', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (101, 'SKT', 1980-01-01, 1980-01-02);

-- Team SoloMid

INSERT INTO teams (id, region, name)
VALUES ('TSM', 'NA', 'Team SoloMid');

INSERT INTO participates (tournamentID, teamID, stageReached)
VALUES ('worlds2015', 'TSM', 'groups');


INSERT INTO players (id, name, careerStartDate)
VALUES (107, 'Dyrus', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (108, 'Santorin', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (109, 'Bjergsen', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (110, 'WildTurtule', 1980-01-01);

INSERT INTO players (id, name, careerStartDate)
VALUES (111, 'Lustboy', 1980-01-01);


INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (107, 'TSM', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (108, 'TSM', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (109, 'TSM', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (110, 'TSM', 1980-01-01, 1980-01-02);

INSERT INTO registers (playerID, teamID, dateJoined, dateLeft)
VALUES (111, 'TSM', 1980-01-01, 1980-01-02);


-- Group stage:

-- AHQ vs BKT:

INSERT INTO series (id, bestOfCount)
VALUES (1, 1);

INSERT INTO organizes (tournamentID, seriesID, stage)
VALUES ('worlds2015', 1, 'groups');

INSERT INTO competes (seriesID, team1ID, team2ID, winner)
VALUES (1, 'AHQ', 'BKT', 'BKT');

INSERT INTO matches (seriesID, matchNumber, date)
VALUES (1, 1, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('AHQ', 1, 1, 4, 7, 0, 1, 3, 0);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('BKT', 1, 1, 2, 5, 0, 0, 1, 1);

-- AHQ bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (1, 1, 'Zac');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (1, 1, 'Zed');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (1, 1, 'Twisted Fate');

-- BKT bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (1, 1, 'Tristana');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (1, 1, 'Thresh');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (1, 1, 'Soraka');

--AHQ picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 2, 'Nidalee', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 3, 'Nami', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 4, 'Jinx', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 5, 'Graves', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 6, 'Garen', 'support', 10, 7, 15, 27000, 23, 14700);

--BKT Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 12, 'Galio', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 13, 'Darius', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 14, 'Caitlyn', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 15, 'Blitzcrank', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (1, 1, 16, 'Amumu', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (1, 1, 14, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (1, 1, 13, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (1, 1, 12, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (1, 1, 10, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (1, 1, 3, 5, 6789, 1, 345);

-- AHQ vs C9:

INSERT INTO series (id, bestOfCount)
VALUES (2, 1);

INSERT INTO organizes (tournamentID, seriesID, stage)
VALUES ('worlds2015', 2, 'groups');

INSERT INTO competes (seriesID, team1ID, team2ID, winner)
VALUES (2, 'AHQ', 'C9', 'C9');

INSERT INTO matches (seriesID, matchNumber, date)
VALUES (2, 1, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('AHQ', 2, 1, 4, 7, 0, 1, 3, 0);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('C9', 2, 1, 2, 5, 0, 0, 1, 1);

-- AHQ bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (2, 1, 'Zac');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (2, 1, 'Zed');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (2, 1, 'Twisted Fate');

-- C9 bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (2, 1, 'Tristana');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (2, 1, 'Thresh');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (2, 1, 'Soraka');

--AHQ picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 2, 'Nidalee', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 3, 'Nami', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 4, 'Jinx', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 5, 'Graves', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 6, 'Garen', 'support', 10, 7, 15, 27000, 23, 14700);

--C9 Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 22, 'Galio', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 23, 'Darius', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 24, 'Caitlyn', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 25, 'Blitzcrank', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (2, 1, 26, 'Amumu', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (2, 1, 22, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (2, 1, 23, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (2, 1, 2, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (2, 1, 3, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (2, 1, 25, 5, 6789, 1, 345);

-- AHQ vs CLG:

INSERT INTO series (id, bestOfCount)
VALUES (3, 1);

INSERT INTO organizes (tournamentID, seriesID, stage)
VALUES ('worlds2015', 3, 'groups');

INSERT INTO competes (seriesID, team1ID, team2ID, winner)
VALUES (3, 'AHQ', 'CLG', 'CLG');

INSERT INTO matches (seriesID, matchNumber, date)
VALUES (3, 1, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('AHQ', 3, 1, 4, 7, 0, 1, 3, 0);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('CLG', 3, 1, 2, 5, 0, 0, 1, 1);

-- AHQ bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (3, 1, 'Zac');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (3, 1, 'Zed');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (3, 1, 'Twisted Fate');

-- CLG bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (3, 1, 'Tristana');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (3, 1, 'Thresh');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (3, 1, 'Soraka');

--AHQ picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 2, 'Nidalee', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 3, 'Nami', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 4, 'Jinx', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 5, 'Graves', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 6, 'Garen', 'support', 10, 7, 15, 27000, 23, 14700);

--CLG Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 122, 'Galio', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 123, 'Darius', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 124, 'Caitlyn', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 125, 'Blitzcrank', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (3, 1, 126, 'Amumu', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (3, 1, 122, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (3, 1, 123, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (3, 1, 2, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (3, 1, 3, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (3, 1, 125, 5, 6789, 1, 345);


-- AHQ vs EDG:

INSERT INTO series (id, bestOfCount)
VALUES (4, 1);

INSERT INTO organizes (tournamentID, seriesID, stage)
VALUES ('worlds2015', 4, 'groups');

INSERT INTO competes (seriesID, team1ID, team2ID, winner)
VALUES (4, 'AHQ', 'EDG', 'EDG');

INSERT INTO matches (seriesID, matchNumber, date)
VALUES (4, 1, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('AHQ', 4, 1, 4, 7, 0, 1, 3, 0);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('EDG', 4, 1, 2, 5, 0, 0, 1, 1);

-- AHQ bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (4, 1, 'Zac');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (4, 1, 'Zed');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (4, 1, 'Twisted Fate');

-- EDG bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (4, 1, 'Tristana');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (4, 1, 'Thresh');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (4, 1, 'Soraka');

--AHQ picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 2, 'Nidalee', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 3, 'Nami', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 4, 'Jinx', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 5, 'Graves', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 6, 'Garen', 'support', 10, 7, 15, 27000, 23, 14700);

--EDG Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 132, 'Galio', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 133, 'Darius', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 134, 'Caitlyn', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 135, 'Blitzcrank', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (4, 1, 136, 'Amumu', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (4, 1, 132, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (4, 1, 133, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (4, 1, 2, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (4, 1, 3, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (4, 1, 135, 5, 6789, 1, 345);

-- Series between FNC and EDG

INSERT INTO series (id, bestOfCount)
VALUES (50, 5);

INSERT INTO organizes (tournamentID, seriesID, stage)
VALUES ('worlds2015', 50, 'quarterfinals');

INSERT INTO competes (seriesID, team1ID, team2ID, winner)
VALUES (50, 'FNC', 'EDG', 'FNC');

-- FNC vs EDG match 1
INSERT INTO matches (seriesID, matchNumber, date)
VALUES (50, 1, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('FNC', 50, 1, 4, 7, 0, 1, 3, 1);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('EDG', 50, 1, 2, 5, 0, 0, 1, 0);

-- FNC bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 1, 'Amumu');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 1, 'Blitzcrank');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 1, 'Caitlyn');

-- EDG bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 1, 'Darius');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 1, 'Galio');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 1, 'Garen');

--FNC picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 127, 'Graves', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 128, 'Jinx', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 129, 'Nami', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 130, 'Nidalee', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 131, 'Soraka', 'support', 10, 7, 15, 27000, 23, 14700);

--EDG Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 132, 'Thresh', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 133, 'Tristana', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 134, 'Twisted Fate', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 135, 'Zac', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 1, 136, 'Zed', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 1, 127, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 1, 129, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 1, 129, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 1, 131, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 1, 132, 5, 6789, 1, 345);

-- FNC vs EDG match 2
INSERT INTO matches (seriesID, matchNumber, date)
VALUES (50, 2, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('FNC', 50, 2, 4, 7, 0, 1, 3, 1);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('EDG', 50, 2, 2, 5, 0, 0, 1, 0);

-- FNC bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 2, 'Amumu');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 2, 'Blitzcrank');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 2, 'Caitlyn');

-- EDG bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 2, 'Darius');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 2, 'Galio');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 2, 'Garen');

--FNC picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 127, 'Graves', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 128, 'Jinx', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 129, 'Nami', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 130, 'Nidalee', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 131, 'Soraka', 'support', 10, 7, 15, 27000, 23, 14700);

--EDG Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 132, 'Thresh', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 133, 'Tristana', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 134, 'Twisted Fate', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 135, 'Zac', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 2, 136, 'Zed', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 2, 127, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 2, 129, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 2, 129, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 2, 131, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 2, 132, 5, 6789, 1, 345);

-- FNC vs EDG match 3
INSERT INTO matches (seriesID, matchNumber, date)
VALUES (50, 3, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('FNC', 50, 3, 4, 7, 0, 1, 3, 0);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('EDG', 50, 3, 2, 11, 0, 0, 1, 1);

-- FNC bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 3, 'Amumu');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 3, 'Blitzcrank');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 3, 'Caitlyn');

-- EDG bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 3, 'Darius');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 3, 'Galio');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 3, 'Garen');

--FNC picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 127, 'Graves', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 128, 'Jinx', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 129, 'Nami', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 130, 'Nidalee', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 131, 'Soraka', 'support', 10, 7, 15, 27000, 23, 14700);

--EDG Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 132, 'Thresh', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 133, 'Tristana', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 134, 'Twisted Fate', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 135, 'Zac', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 3, 136, 'Zed', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 3, 127, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 3, 129, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 3, 129, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 3, 131, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 3, 132, 5, 6789, 1, 345);

-- FND vs EDG match 4
INSERT INTO matches (seriesID, matchNumber, date)
VALUES (50, 4, 1980-01-01);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('FNC', 50, 4, 4, 7, 0, 1, 3, 1);

INSERT INTO scores (teamID, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus)
VALUES ('EDG', 50, 4, 2, 5, 0, 0, 1, 0);

-- FNC bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 4, 'Amumu');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 4, 'Blitzcrank');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 4, 'Caitlyn');

-- EDG bans

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 4, 'Darius');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 4, 'Galio');

INSERT INTO bans (seriesID, matchNumber, name)
VALUES (50, 4, 'Garen');

--FNC picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 127, 'Graves', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 128, 'Jinx', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 129, 'Nami', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 130, 'Nidalee', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 131, 'Soraka', 'support', 10, 7, 15, 27000, 23, 14700);

--EDG Picks

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 132, 'Thresh', 'top', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 133, 'Tristana', 'jungle', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 134, 'Twisted Fate', 'mid', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 135, 'Zac', 'adc', 10, 7, 15, 27000, 23, 14700);

INSERT INTO plays (seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold)
VALUES (50, 4, 136, 'Zed', 'support', 10, 7, 15, 27000, 23, 14700);

-- Item buys/sells

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 4, 127, 4, 1426, 1, 400);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 4, 129, 1, 1928, 0, -1900);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 4, 129, 2, 2120, 1, 2348);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 4, 131, 3, 3848, 1, 7463);

INSERT INTO interacts (seriesID, matchNumber, playerID, itemID, time, isBuy, spent)
VALUES (50, 4, 132, 5, 6789, 1, 345);
