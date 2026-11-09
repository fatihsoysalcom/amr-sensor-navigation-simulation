import time
import random

class AMR:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.battery = 100
        self.sensors = {
            'lidar': {'range': 5, 'obstacles': []},
            'camera': {'objects': []}
        }
        self.target_reached = False

    def move(self, dx, dy):
        # Simulate movement, consume battery
        self.x += dx
        self.y += dy
        self.battery -= 1
        print(f"AMR moved to ({self.x}, {self.y}). Battery: {self.battery}%")

    def scan_environment(self):
        # Simulate sensor readings
        # Lidar: Detect obstacles within range
        self.sensors['lidar']['obstacles'] = []
        for _ in range(random.randint(0, 3)):
            obs_x = self.x + random.uniform(-self.sensors['lidar']['range'], self.sensors['lidar']['range'])
            obs_y = self.y + random.uniform(-self.sensors['lidar']['range'], self.sensors['lidar']['range'])
            self.sensors['lidar']['obstacles'].append((obs_x, obs_y))

        # Camera: Detect objects (simplified)
        self.sensors['camera']['objects'] = []
        if random.random() < 0.2:
            self.sensors['camera']['objects'].append("package")

        print(f"Lidar detected {len(self.sensors['lidar']['obstacles'])} obstacles. Camera detected {len(self.sensors['camera']['objects'])} objects.")

    def navigate_to(self, target_x, target_y):
        print(f"Navigating to ({target_x}, {target_y})...")
        while not self.target_reached and self.battery > 0:
            self.scan_environment()

            # Basic obstacle avoidance (if lidar detects something close)
            avoidance_move = False
            for obs_x, obs_y in self.sensors['lidar']['obstacles']:
                if abs(obs_x - self.x) < 1 and abs(obs_y - self.y) < 1:
                    print("Obstacle detected, attempting to avoid.")
                    # Simple avoidance: move perpendicular to obstacle direction
                    if abs(target_x - self.x) > abs(target_y - self.y):
                        self.move(0, 1 if target_y > self.y else -1)
                    else:
                        self.move(1 if target_x > self.x else -1, 0)
                    avoidance_move = True
                    break
            if avoidance_move:
                continue

            # Move towards target
            dx, dy = 0, 0
            if self.x < target_x:
                dx = 1
            elif self.x > target_x:
                dx = -1

            if self.y < target_y:
                dy = 1
            elif self.y > target_y:
                dy = -1

            self.move(dx, dy)

            if self.x == target_x and self.y == target_y:
                self.target_reached = True
                print("Target reached!")
            
            time.sleep(0.5) # Simulate time passing

        if self.battery <= 0:
            print("Battery depleted. Navigation failed.")

if __name__ == "__main__":
    # Initialize AMR at (0,0) with 100% battery
    robot = AMR(x=0, y=0)
    
    # Define a target destination
    target_x, target_y = 5, 5
    
    # Start navigation simulation
    robot.navigate_to(target_x, target_y)
