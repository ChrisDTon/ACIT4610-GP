# Comparing ACO and PSO for VRPTW
## Execution explanation
Python version: 3.12.4
Dependancies:
- numpy
- matplotlib
Press: Run All or similar function of code editor

## Approach
### ACO
The ACO uses pheromones and the distance between current position and candidate positions to construct routes. The amount of vehicles used is dynamic with a maximum number assignable. Fine-tuning parameters can all be updated by passing to the run. An ant constructs a route for all the vehicles and leaves a trail of pheromones, where the strength of the pheromones is dependant on the fitness of the solution. The lower the cost the route / solution the ant constructed, the stronger the pheromone trail.

Step by step:
1. Run starts a loop the length of the desired iterations
    1. In the loop construct_solution is called and constructs a solution for each iteration
        1. Each ant constructs a routes for all vehicles
        2. select_next_customer is called during route construction to select next customer in route based on attractiveness (how close the customer is to vehicle location, and pheromone trail), and constraint violation (time windows and capacity)
    2. Pheromone trails are updated

### PSO
The PSO uses global best position, personal best position, and inertia to construct routes. The amount of vehicles used is dynamic with a maximum number assignable. Fine-tuning prameters are all kept in a config at the top for ease of updating. A particle is a full solution (the vehicle routes), not a single vehicle, and is in a search space made up of all possible solutions the algorithm could explore.

Theoretical perspective of the search space for the particles:
- The search space is multi-dimensional, represented by all possible combinations of variables involved in the problem.
- A particle represents a solution
- The position of the particle in the search space represents the a particular configuration of the variables involved in the problem.
- The global best position is the position in the search space that a previous particle has been in with the highest rated fitness i.e. the configuration of variables that gave the highest rated fitness
- The personal best posistion is the position with the highest rated fitness this particular particle has been to i.e. the configuration of variables that has given this particle its highest rated fitness
- Inertia is how much a particle wants to continue to move in the same direction in the search space

Step by step:
1. Optimize starts a loop the length of the desired iterations
    1. In the loop we use a for loop to make the particles construct their routes
      1. First in the route for all vehicles are depot
      2. The first customer is decided by distance to depot
      3. The rest of the customers are decided using nearest neighbor
    2. Update position and velocity / inertia of the particles
    3. We evaluate the fitness of the particles
    4. Update global variables

## c101.txt
- c101 was formated to keep data in rows / a single line rather than columns to be more easibly used with python lists and more readable
- Was sourced from [https://www.sintef.no/globalassets/project/top/vrptw/solomon/solomon-100.zip], Oct. 2024

## ACO
- Algorithm based on the food gathering and search behavior of a colony of ants
- All ants leave behind pheramon that evaporates, commonly traveled routes will have their pheramon replenished and reinforced due to distance and later amount of ants traveling them

## PSO
- Algorithm inspired by the flocking behavior of birds, and schooling behavior of fish
- Individual keeps track of its neighbors and keep distance / follow
- Global best and personal best

# Assumptions
- Customer no.0 is the depot.
  - The documentation says that customer number 0 is the depot, but in the c101 we found no customer number 0, and as such are using number 1.
  - Customer number 1 has no demand, ready time, or service time
  - Due date for customer no.1 is closing hours and all vehicles must be back to depot before then
- Dataset uses bases time from start and a value of 1 is equal to 1 minute
  - Deliveries in dataset is for a single day
  - Due date of 1236 is in 20.6 hours from start
  - Due date of 967 is in 16.1 hours from start