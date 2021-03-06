
-- increase garage capacity where necessary
update garage set max_capacity = (
  select count(c.id) from car as c where c.garage_id = garage.id
) where id in (
  select g.id from garage as g left join car as c
  on g.id = c.garage_id
  group by c.garage_id
  having count(c.id) > g.max_capacity
);