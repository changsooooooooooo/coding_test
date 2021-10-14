------ web-backend 2021 1st --------
SELECT * from places
where host_id in
      (
          select p.host_id
          from places p
          group by p.host_id
          having 1<count(p.host_id)
      )
order by id;
