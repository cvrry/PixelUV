# PixelUV

## What does it do?
A blender addon that takes a family of objects with named vertex groups and maps them onto a single unique point on a UV Map

Each object is a "level" and each vertex group is a "zone"

Obj Data  ->  UVmap<br />
zones     ->  X axis<br />
levels    ->  Y axis<br />

![pixelUV explain](https://user-images.githubusercontent.com/15632432/234484113-3403ec87-c966-4d4a-a72a-b801cc786a42.png)

### e.g.
With 3 levels and 3 Zones, we get UVs like this <br/>
![image](https://user-images.githubusercontent.com/15632432/234534373-22829d54-3746-41e4-a050-254669c6e6c9.png)


## Installation
- Navigate to `Blender > Edit > PReferences > Add-ons > Install >`
+ Select the `__PixelUV.py__` from the latest release <br/>
![image](https://user-images.githubusercontent.com/15632432/234527676-c9346871-3959-47a5-8520-b84565731bf8.png)

## Usage

- Make a collection with the family of objects `levels` (the numbering enforces the order) <br\>
![image](https://user-images.githubusercontent.com/15632432/234530681-8144c355-12f5-4e74-8c8a-eba4dfa3c338.png)

+ Create vertex Groups with a common starting tag e.g. __bz___ (the numbering matters decides the location) <br/>
![image](https://user-images.githubusercontent.com/15632432/234530971-555adfaa-2a4e-468a-97ca-70a4a2a7b43c.png) <br/>
_Make Sure to all the vertices belong to atleast one vertex group_

+ With the collection selected, type in the identifying tag given to the vertex groups into the addon ; available on the __toolbar__ <br/>
Hit the `Generate Pixel UV map` button
![image](https://user-images.githubusercontent.com/15632432/234532549-cd47b779-ba07-4bf2-9b78-3f6a8779702a.png)

UVs should now be arranged


### Note:
The levels will just be arranged in ascenting order, while the zones will be arranged according to the numbering.
This is done to allow for missing limbs or parts across the levels, but be tolerant towards naming of the levels.
