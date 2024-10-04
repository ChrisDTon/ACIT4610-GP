# Comparing ACO and PSO for VRPTW

## Assumptions
- Customer no.1 is the depot.
  - The documentation says that customer number 0 is the depot, but in the c101 we found no customer number 0, and as such are using number 1.
  - Customer number 1 has no demand, ready time, or service time
- Dataset uses "1900 date system"
  - Dates are saved as number values, and are the days since January 0th 1900
  - e.g.
    - 0 = 00/01/1900
    - 1 = 01/01/1900
    - 2 = 02/01/1900
