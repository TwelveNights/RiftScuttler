CREATE VIEW IF NOT EXISTS roles AS
  SELECT
  player,
  role,
  COUNT(*) AS rolecount,
  AVG(wardsPlaced) AS  avgw,
  AVG(gold) AS avgg,
  AVG(wardsDestroyed) AS avgwd,
  AVG(cs) AS avgcs,
  AVG(teamJungleMinions) AS avgtJungle,
  AVG(enemyJungleMinions) AS avgeJungle,
  AVG(damageDealt) AS avgdmg
  FROM plays
  GROUP BY player, role;