# URDF for Humanoid Robots: Defining the Physical Form

To accurately simulate, visualize, and control a robotic system, especially a complex humanoid, its physical properties and structure must be precisely defined. The Unified Robot Description Format (**URDF**) is an XML-based file format in ROS that serves this purpose. It allows you to describe a robot's kinematics (how its parts are connected and move) and dynamics (mass, inertia).

## Structure, Joints, and Links: The Building Blocks

URDF describes a robot as a tree-like structure composed of **links** and **joints**.

### Links: The Robot's Body Segments

A **link** represents a rigid body segment of the robot. This could be a robot's torso, upper arm, forearm, hand, head, or a wheel. For each link, you define:

*   **Visual Properties (`<visual>` tag):** How the link looks in a simulator or RViz (ROS visualization tool). This includes the geometry (e.g., box, cylinder, mesh file like `.stl` or `.dae`), material (color, texture), and its origin (position and orientation relative to the link's frame).
*   **Collision Properties (`<collision>` tag):** How the link interacts physically with other objects in a simulation. This also includes geometry and origin, which can be a simplified version of the visual geometry to reduce computation for collision detection.
*   **Inertial Properties (`<inertial>` tag):** The mass and inertia tensor of the link, crucial for accurate physics simulation.

**Example Link (Simplified):**
```xml
<link name="torso">
  <visual>
    <geometry><box size="0.2 0.4 0.6" /></geometry>
    <material name="blue" />
  </visual>
  <collision>
    <geometry><box size="0.2 0.4 0.6" /></geometry>
  </collision>
  <inertial>
    <mass value="10.0" />
    <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0" />
  </inertial>
</link>
```

### Joints: Connecting the Segments

A **joint** describes the kinematic and dynamic properties of the connection between two links. Joints define how links can move relative to each other.

*   **Parent and Child Links:** Each joint connects a `parent` link to a `child` link. The robot's structure typically starts with a `base_link` (often a fixed reference to the world or the robot's root).
*   **Type (`type` attribute):** Specifies the degree of freedom (DOF) of the joint. Common types for humanoids include:
    *   **`revolute`:** Rotational joint with a limited range (e.g., elbow, knee).
    *   **`continuous`:** Rotational joint with unlimited range (e.g., spinning wheel).
    *   **`prismatic`:** Linear joint with a limited range (e.g., telescoping arm).
    *   **`fixed`:** No movement; rigidly attaches two links (e.g., a camera mounted to a head link).
*   **Origin (`<origin>` tag):** Defines the joint's position and orientation relative to its parent link.
*   **Axis (`<axis>` tag):** For revolute and prismatic joints, defines the axis of rotation or translation.
*   **Limit (`<limit>` tag):** For revolute and prismatic joints, specifies the upper and lower bounds of motion, and velocity/effort limits.

**Example Joint (Simplified):**
```xml
<joint name="shoulder_pitch_joint" type="revolute">
  <parent link="torso" />
  <child link="upper_arm_link" />
  <origin xyz="0 0.2 0.3" rpy="0 0 0" />
  <axis xyz="0 1 0" />
  <limit lower="-1.57" upper="1.57" effort="100" velocity="0.5" />
</joint>
```

## Why URDF is Critical for Humanoid Robotics

URDF is foundational for humanoid robotics development for several reasons:

1.  **Simulation:** Simulators like Gazebo parse URDF files to build the virtual robot model, apply physics (gravity, collisions), and render it visually. Without an accurate URDF, realistic simulation is impossible.
2.  **Visualization:** Tools like RViz use URDF to display the robot's 3D model and its current joint states, aiding in debugging and understanding robot behavior.
3.  **Kinematics and Dynamics:** Libraries for inverse kinematics (calculating joint angles to reach a target end-effector position) and dynamics (understanding forces and torques) rely on the kinematic and inertial properties defined in the URDF.
4.  **Control:** Robot control software uses the joint limits, velocity limits, and effort limits from the URDF to plan motions and ensure safe operation.
5.  **Standardization:** URDF provides a standardized, robot-agnostic way to describe physical robots, promoting reusability and interoperability within the ROS ecosystem.

For humanoids, defining an accurate URDF involves carefully modeling each segment of the body, including many degrees of freedom for the torso, arms, legs, and head. This detailed description is the first step towards bringing a humanoid robot to life, both in simulation and in the real world. The next section will summarize Module 1 and provide real-world mapping.
