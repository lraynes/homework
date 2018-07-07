use sakila;

-- Display the first and last names of all actors from the table actor.
SELECT first_name, last_name FROM actor;

-- Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS 'Actor Name' FROM actor;

-- You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT * FROM actor
WHERE first_name = "joe";

-- Find all actors whose last name contain the letters GEN:
SELECT * FROM actor
WHERE last_name like "%gen%";

-- Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT last_name, first_name FROM actor
WHERE last_name like "%li%";


-- Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country FROM country
WHERE country IN ("Afghanistan", "Bangladesh", "China");

-- Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(225) AFTER first_name;

-- You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
ALTER TABLE actor
MODIFY COLUMN middle_name BLOB;

-- Now delete the middle_name column.
ALTER TABLE actor
DROP COLUMN middle_name;

-- List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(last_name) from actor
GROUP BY last_name;

-- List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, COUNT(last_name) from actor
GROUP BY last_name
HAVING COUNT(last_name) > 1;

-- Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
select * from actor WHERE first_name = "GROUCHO" AND last_name = "Williams"; -- to find actor_id

UPDATE actor
SET first_name = "HARPO"
WHERE actor_id = 172;

-- Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO. 
-- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
UPDATE actor 
SET first_name = IF(first_name='HARPO', 'GROUCHO', 'MUCHO GROUCHO') 
WHERE actor_id = 172;


-- You cannot locate the schema of the address table. Which query would you use to re-create it? Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html
SHOW CREATE TABLE address;

-- Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select c.first_name, c.last_name, a.address
from address a
join staff c
on (a.address_id = c.address_id);

-- Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select s.first_name, sum(p.amount)
from payment p
join staff s
on (s.staff_id = p.staff_id)
GROUP BY s.staff_id;

-- List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select count(a.actor_id) as 'Number of Actors', f.title
from film_actor a
inner join film f
on (f.film_id = a.film_id)
group by f.film_id;

-- How many copies of the film Hunchback Impossible exist in the inventory system?
select f.title, count(i.film_id) as 'Number in Inventory' 
from film f
join inventory i
on (f.film_id = i.film_id)
and f.title = "Hunchback Impossible"
group by i.film_id;

-- Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name.
select c.first_name, c.last_name, sum(p.amount) as 'Total Paid'
from customer c
join payment p
on (c.customer_id = p.customer_id)
group by c.customer_id
order by c.last_name;

-- The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select f.title, l.name
from film f
join language l
on (f.language_id = l.language_id)
where f.title in (
	select title from film
    where title like "Q%" or title like "K%"
)
and f.language_id = 1;

-- Use subqueries to display all actors who appear in the film Alone Trip.
select first_name, last_name, actor_id from actor
where actor_id in(
	select actor_id from film_actor
    where film_id in(
		select film_id from film
        where title = "alone trip"
    )
);

-- You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
select * from customer; -- email and address id
select * from address; -- address id to city id
select * from city; -- city id to country id
select * from country; -- country id to canada

select o.country, c.city, u.email
from country o
join city c
on (o.country_id = c.country_id)
and o.country = "Canada"
join address a
on (c.city_id = a.city_id)
join customer u
on (a.address_id = u.address_id);


-- Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
select title from film
where film_id in(
	select film_id from film_category
    where category_id in(
		select category_id from category
        where name = "Family"
    )
);

-- Display the most frequently rented movies in descending order.
select f.title, count(f.title) as 'Number of Rentals'
from film f
join inventory i
on (f.film_id = i.film_id)
join rental r
on (r.inventory_id = i.inventory_id)
group by f.title
order by count(f.title) desc;

-- Write a query to display how much business, in dollars, each store brought in.
select f.store_id, sum(p.amount) as 'Business in Dollars'
from payment p
join staff f
on (p.staff_id = f.staff_id)
join store o
on (f.store_id = o.store_id)
group by o.store_id;

-- Write a query to display for each store its store ID, city, and country.
select s.store_id, c.city, co.country
from store s
join address a
on (s.address_id = a.address_id)
join city c
on (a.city_id = c.city_id)
join country co
on (c.country_id = co.country_id);

-- List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select c.name, sum(p.amount) as 'Gross Revenue'
from category c
join film_category f
on (c.category_id = f.category_id)
join inventory i
on (f.film_id = i.film_id)
join rental r
on (i.inventory_id = r.inventory_id)
join payment p
on (r.rental_id = p.rental_id)
group by c.name 
order by sum(p.amount) desc
limit 5;

-- In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
create view top_five_genres as
select c.name, sum(p.amount) as 'Gross Revenue'
from category c
join film_category f
on (c.category_id = f.category_id)
join inventory i
on (f.film_id = i.film_id)
join rental r
on (i.inventory_id = r.inventory_id)
join payment p
on (r.rental_id = p.rental_id)
group by c.name 
order by sum(p.amount) desc
limit 5;

-- How would you display the view that you created in 8a?
select * from top_five_genres;

-- You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view top_five_genres;