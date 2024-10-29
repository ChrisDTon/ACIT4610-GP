# Comparing ACO and PSO for VRPTW

## Assumptions
- Customer no.1 is the depot.
  - The documentation says that customer number 0 is the depot, but in the c101 we found no customer number 0, and as such are using number 1.
  - Customer number 1 has no demand, ready time, or service time
  - Due date for customer no.1 is closing hours and all vehicles must be back to depot before then
- Dataset uses bases time from start and a value of 1 is equal to 1 minute
  - Deliveries in dataset is for a single day
  - Due date of 1236 is in 20.6 hours from start
  - Due date of 967 is in 16.1 hours from start

# c101.txt
- c101 was formated to keep data in rows / a single line rather than columns to be more easibly used with python lists

# ACO
- Algorithm based on the food gathering and search behavior of a colony of ants
- All ants leave behind pheramon that evaporates, commonly traveled routes will have their pheramon replenished and reinforced

# PSO
- Algorithm inspired by the flocking behavior of birds, and schooling behavior of fish
- Individual keeps track of its neighbors and keep distance / follow
