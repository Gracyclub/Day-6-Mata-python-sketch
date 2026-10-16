import cv2
import numpy as np
import random
import math

class GlowParticle:
    def __init__(self, target_x, target_y, color):
        self.target_x = target_x
        self.target_y = target_y
        # Bright vibrant color amplification for neon look
        self.color = [min(255, int(c * 1.5)) for c in color]
        
        # Spawn in a vast cosmic orbit far away
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(350, 750)
        self.x = 640 + distance * math.cos(angle)
        self.y = 360 + distance * math.sin(angle)
        
        # Spiral-gravitational mechanics
        self.speed = random.uniform(0.04, 0.08)
        self.angle_offset = random.uniform(-0.1, 0.1)

    def update(self, start_gravity):
        if not start_gravity:
            # Orbital spiral floating pre-trigger
            dx = self.x - 640
            dy = self.y - 360
            dist = math.hypot(dx, dy)
            current_angle = math.atan2(dy, dx)
            
            # Gentle orbital shrinkage into the vortex
            new_angle = current_angle + 0.015 + self.angle_offset * 0.01
            new_dist = dist * 0.992
            self.x = 640 + new_dist * math.cos(new_angle)
            self.y = 360 + new_dist * math.sin(new_angle)
        else:
            # Cinematic gravity snap to exact image features
            self.x += (self.target_x - self.x) * self.speed
            self.y += (self.target_y - self.y) * self.speed

def main():
    img_path = "katyayani.png"
    target_img = cv2.imread(img_path)

    if target_img is None:
        print(f"Error: Couldn't find '{img_path}'. Add the space neon image first!")
        return

    H, W = 720, 1280
    target_img = cv2.resize(target_img, (W, H), interpolation=cv2.INTER_AREA)

    window_name = "Navratri Day 6 - Maa Katyayani Space Neon Assembly"
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # 1. Image features scanning
    gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 40, 120)
    
    indices = np.where(edges > 0)
    edge_points = list(zip(indices[1], indices[0]))
    random.shuffle(edge_points)
    
    # 2. Particle distribution (Edgework + vibrant fill)
    particles = []
    for x, y in edge_points[:3800]:
        particles.append(GlowParticle(x, y, target_img[y, x]))

    for _ in range(4500):
        rx, ry = random.randint(0, W - 1), random.randint(0, H - 1)
        color = target_img[ry, rx]
        if sum(color) > 110: # Only colorful features
            particles.append(GlowParticle(rx, ry, color))

    total_frames = 260
    trigger_magnetic_assembly = False

    print("Playing Celestial Neon Particle Assembly... Press any key inside GUI to force jump.")

    for frame in range(total_frames):
        # Time markers
        if frame > 65:
            trigger_magnetic_assembly = True

        canvas = np.zeros((H, W, 3), dtype=np.uint8)

        # 3. Ambient space stardust background
        for _ in range(35):
            sx, sy = random.randint(0, W - 1), random.randint(0, H - 1)
            bright = random.randint(100, 255)
            cv2.circle(canvas, (sx, sy), 1, (bright, bright - 40, 255), -1)

        # 4. Cinematic Cyber glitches (Matrix registration look)
        if frame % 18 == 0 and frame < 150:
            glitch_y = random.randint(100, H - 100)
            cv2.line(canvas, (0, glitch_y), (W, glitch_y), (180, 0, 100), 1)
            cv2.line(canvas, (0, glitch_y + 4), (W, glitch_y + 4), (0, 180, 255), 1)

        # 5. Visualizer Energy Portal at center (Until converged)
        if frame < 185:
            center_wave = int(110 + 25 * math.sin(frame * 0.15))
            cv2.circle(canvas, (640, 360), center_wave, (255, 30, 80), -1, cv2.LINE_AA) # outer pink portal
            cv2.circle(canvas, (640, 360), int(center_wave * 0.65), (0, 190, 255), -1, cv2.LINE_AA) # inner orange portal
            cv2.circle(canvas, (640, 360), int(center_wave * 0.2), (255, 255, 255), -1, cv2.LINE_AA) # hot core

        # 6. Smooth Particle mechanics & tracer lines
        for p in particles:
            p.update(trigger_magnetic_assembly)
            px, py = int(p.x), int(p.y)
            if 0 <= px < W and 0 <= py < H:
                cv2.circle(canvas, (px, py), 1, p.color, -1)

        # 7. Hologram fading transition
        if frame > 120:
            alpha = min(1.0, (frame - 120) / 80.0)
            canvas = cv2.addWeighted(target_img, alpha, canvas, 1.0 - alpha, 0)

        # Bottom loading telemetry / cyber overlays
        if frame < 195:
            percent = min(100, int((frame / 195) * 100))
            text = f">> ASSEMBLING CELESTIAL ALGORITHM (DAY 6)... {percent}%"
            cv2.putText(canvas, text, (40, H - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 220, 255), 1, cv2.LINE_AA)
            cv2.rectangle(canvas, (40, H - 28), (40 + int(percent * 2.5), H - 24), (0, 215, 255), -1)
        else:
            cv2.putText(canvas, "|| JAI MAA KATYAYANI ||", (W // 2 - 140, H - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow(window_name, canvas)

        if cv2.waitKey(23) & 0xFF == 27: # Esc
            break

    # Stay on original image
    cv2.imshow(window_name, target_img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()