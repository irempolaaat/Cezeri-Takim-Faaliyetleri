import matplotlib.pyplot as mpt
import numpy as np
import matplotlib.animation as animation # type: ignore
class Drone:
    def __init__(self, x1, y1, total_distance):
        self.x1 = x1
        self.y1 = y1
        self.changing_x = x1
        self.changing_y = y1  
        self.total_distance = total_distance  
        self.current_distance = 0 
    

    def update_position(self, velocity):

        dx_unit = -1
        dy_unit = 1
        
        if self.current_distance + velocity >= self.total_distance:

            self.changing_x += dx_unit * (self.total_distance - self.current_distance)
            self.changing_y += dy_unit * (self.total_distance - self.current_distance)
            self.current_distance = self.total_distance
            return True  # Reached the target
        else:

            self.changing_x += dx_unit * velocity
            self.changing_y += dy_unit * velocity
            self.current_distance += velocity
            return False  # not reached the target

class Swarm:
    def __init__(self, number_of_drones):
        self.number_of_drones = number_of_drones
        self.drones = []

        self.x1 = np.random.randint(2, 7, self.number_of_drones)
        self.y1 = np.random.randint(2, 7, self.number_of_drones)

        self.total_distance = 3  

        for i in range(self.number_of_drones):
            drone = Drone(self.x1[i], self.y1[i], self.total_distance)
            self.drones.append(drone)

        mpt.scatter(self.x1, self.y1, color="blue", marker='*')

    def update_all(self, velocity):
        # Update positions of all drones
        all_done = True
        for drone in self.drones:
            if not drone.update_position(velocity):
                all_done = False
        return all_done

fig, ax = mpt.subplots()
ax.set_xlim(0, 11)  
ax.set_ylim(0, 11)  

swarm = Swarm(7)  
velocity = 0.1  

drone_lines = []
for _ in range(swarm.number_of_drones):
    
    line, = ax.plot([], [], 'ro', markersize=5)
    drone_lines.append(line)

def update(frame):

    all_done = swarm.update_all(velocity)

    # Update the new position of each drone
    for i, drone in enumerate(swarm.drones):
        drone_lines[i].set_data(drone.changing_x, drone.changing_y)

    if all_done:
        print("All drones have reached the target!")
        return drone_lines
    return drone_lines

ani = animation.FuncAnimation(fig, update, frames=100, interval=70, blit=False)

mpt.show()
