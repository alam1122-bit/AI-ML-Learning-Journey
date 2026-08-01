# 📌 Exercise 1: Listing Pineapple Routes

### 📖 Problem Overview
In this exercise, we need to generate all possible valid travel routes starting from **Panama (PAN)** and visiting all other ports (`AMS`, `CAS`, `NYC`, `HEL`) **exactly once**.

Instead of hardcoding port names as strings, ports are represented as integer indexes:
- `0`: PAN (Panama)
- `1`: AMS (Amsterdam)
- `2`: CAS (Casablanca)
- `3`: NYC (New York)
- `4`: HEL (Helsinki)

---

### 💡 Beginner Level

#### Question:
How many routes would there be if all the people in Helsinki were allergic to pineapple? In other words, what is the number of routes from a given starting point to three other ports (instead of four)?

#### Answer:
The formula for counting the number of routes is $1 \times 2 \times 3 \times \dots$ where the last number is the number of ports, not including the starting points. So if there are three other ports, the number is:

$$1 \times 2 \times 3 = 6$$

---

### 💡 Intermediate Level

```python
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def main():
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if(len(set(route))==5):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()


---

### 💡 Advanced  Level

```python

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    if(len(ports)==0):
    # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
        return
    for i in range(len(ports)):
        new_route = route + [ports[i]] # 1st iteration [0,1], 2nd iteration here,i=0
        remaining_ports = ports[:i] + ports[i+1:] # ports[:1] = [0] & ports[2:] = [3,4]
        permutations(new_route, remaining_ports)
# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames)))) # list 1,2,3,4
