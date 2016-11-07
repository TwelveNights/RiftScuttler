CREATE VIEW IF NOT EXISTS roles AS
  SELECT
  playerID,
  role,
  COUNT(*) AS rolecount,
  AVG(wardsPlaced) AS  avgw,
  AVG(gold) AS avgg
  FROM plays
  GROUP BY playerID, role;