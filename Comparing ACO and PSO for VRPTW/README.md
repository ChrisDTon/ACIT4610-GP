# Comparing ACO and PSO for VRPTW

## Assumptions
- Customer no.1 is the depot.
  - The documentation says that customer number 0 is the depot, but in the c101 we found no customer number 0, and as such are using number 1.
  - Customer number 1 has no demand, ready time, or service time
  - Due date for customer no.1 is closing hours and all vehicles must be back to depot before then
- Dataset uses bases time from start and a value of 1 is equal to 1 minute
  - Due date of 1236 is in 20.6 hours from start
  - Due date of 967 is in 16.1 hours from start
