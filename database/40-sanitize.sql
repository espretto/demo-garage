
-- increase garage capacity where necessary
update garage set max_capacity = (
  select count(c.id) from car c where c.garage_id = garage.id
) where id in (
  select g.id from garage g left join car c
  on g.id = c.garage_id
  group by c.garage_id
  having count(c.id) > g.max_capacity
);