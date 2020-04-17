# -*- coding: utf-8 -*-
#!/usr/bin/env python

INSERT_HISTORY = "INSERT INTO history VALUES(?, ?, ?, ?)"
INSERT_ALLOWED_IDS = "INSERT INTO allowed_ids VALUES(?, ?)"
SELECT_FROM_ALLOWED_IDS_BY_ID = "SELECT * FROM allowed_ids WHERE id=?"
SELECT_FROM_HISTORY_BY_ID = "SELECT * FROM history WHERE id=?"
SELECT_FROM_HISTORY_BY_GTE_DATE = "SELECT * FROM history WHERE created_date >= ?"
DELETE_FROM_ALLOWED_IDS_BY_ID = "DELETE FROM allowed_ids WHERE id=?"
UPDATE_ALLOWED_IDS_TEXT_BY_ID = "UPDATE allowed_ids SET text=? WHERE id=?"
