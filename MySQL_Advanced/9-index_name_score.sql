-- script that creates an index idx_name_first_score on the table names and the first letter of name and the score.
-- Cet index est particulièrement utile pour des applications nécessitant des recherches rapides par la première lettre des noms et des plages de scores.


CREATE  INDEX idx_name_first_score ON names(name(1), score)