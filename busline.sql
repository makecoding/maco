BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `temp` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	INTEGER
);
INSERT INTO `temp` VALUES (1,'ddddd');
INSERT INTO `temp` VALUES (4,'ddddd');
INSERT INTO `temp` VALUES (1234777,'lejasek');
INSERT INTO `temp` VALUES (12341234,'lejasek');
COMMIT;
