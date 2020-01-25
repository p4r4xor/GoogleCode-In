# Hardware Acceleration
Hardware acceleration is the process by which an app will use other hardware components on your system to perform certain tasks in order to work more efficiently. Why do we need it? Well, our CPUs are supposed to handle the majority of tasks and GPUs are for the computationally intensive functions.

For example, CPU does this — Order your food, Write an email, Chat on Facebook, Draw images on paint in 2 minutes. And a GPU does — Calculate 12838742! in 0.5 sec. Go!

Where is this used? Visual processes are sometimes offloaded to a GPU for enabling higher-quality playback of videos and games which free up the CPU for additional tasks.

### Hardware used for acceleration

* **Graphics Processing Units (GPUs)**

Mainly used for providing images for computer games. More number of ALU units makes this computationally faster but fails as a multitasker. Supports parallel processing, which is considered better than serial processing.

* **Field Programmable Gate Arrays (FPGAs)**

These guys have a reconfigureable circuit. You can customize a part of a chip while the remaining area of a chip is working. As these consume a lot of power, running hardware accelerations is costly but worth it. FPGAs are also used for cryptocurrency mining, but everything comes with a cost. 

* **Application-Specific Integrated Circuits (ASICs)**

ASICs have complete analog based circuitry, which makes it relatively harder than the other two to perform Hardware Acceleration. These aren't suited for many applications, but yet these are mass produced as most of the current-gen ASICs are cheap and do most basic human inputs.

```
Some common uses of hardware acceleration is tethering hardware acceleration, while acting as a WiFi hotspot, will offload operations involving tethering onto a WiFi chip, reducing system workload and increasing energy efficiency.
```

### When to Use Hardware Acceleration

Normally, A lot of developers tend to use algorithm optimization techniques like Dynamic programming with bitmasking, Flows and Matchings, Convex Hull trick, Lagrange's Interpoletion etc. This takes some deep understanding of Graph theory and Dynamic programming, but sometimes we can't afford to do so when the code runs fine as per the client.

An alternate would be using Hardware acceleration through FPGAs (ASICs do not provide much acceleration because they are hard wired and cannot be much customized -- An example would be an Intel CPU). Why use FPGAs? Because they are loosely programmed in verilog and no optimizations take place through the code (Unless you use Data Structures like trees and graphs). This gives us a huge advantage in the Hardware category because they can be used for developing a different processor architecture, or split the code across two processors to run in parallel.
