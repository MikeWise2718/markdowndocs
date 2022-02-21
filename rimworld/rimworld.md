---
title: "RimWorld"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
RimWorld the game

- Interesting RimWorld Fridge Physics - (https://www.reddit.com/r/RimWorld/comments/b1wz9a/rimworld_temperature_physics_allow_you_to_build/)
- Fire - (https://www.reddit.com/r/RimWorld/comments/6sqnhl/i_learned_some_really_valuable_lessons_about_fire/)


# Zen Garden
- Mod written originally by cuproPanda, now mantrasong
- Link to Steam Page:(https://steamcommunity.com/sharedfiles/filedetails/?id=1554147049)
- Link to Github Pate:(https://github.com/mantrasong/Zen-Garden)
- Cherry trees not giving 10 beauty:
    - Steam Comment:
```    
Signal 19 Jan @ 2:48am 
I noticed that trees added by this mod only have beauty 1, despite having a beauty rating of up to 10. I found that they're missing the BeautyOutdoors property (presumably new for Ideology or 1.3). Adding BeautyOutdoors to the trees in Plants.xml makes the trees beautiful again, so my colonists can truly enjoy the cherry trees surrounding the garden.
```

## Plants.xml
```
C:\Program Files (x86)\Steam\steamapps>dir /s plants.xml
 Volume in drive C is Absol System
 Volume Serial Number is 8E1E-E55C

 Directory of C:\Program Files (x86)\Steam\steamapps\workshop\content\294100\1554147049\1.0\Defs\ThingDefs

02-Aug-21  21:04             8,171 Plants.xml
               1 File(s)          8,171 bytes

 Directory of C:\Program Files (x86)\Steam\steamapps\workshop\content\294100\1554147049\1.1\Defs\ThingDefs

06-Sep-20  21:48             8,097 Plants.xml
               1 File(s)          8,097 bytes

 Directory of C:\Program Files (x86)\Steam\steamapps\workshop\content\294100\1554147049\1.2\Defs\ThingDefs

02-Aug-21  21:04             8,097 Plants.xml
               1 File(s)          8,097 bytes

 Directory of C:\Program Files (x86)\Steam\steamapps\workshop\content\294100\1554147049\1.3\Defs\ThingDefs

02-Aug-21  21:04             8,097 Plants.xml
               1 File(s)          8,097 bytes
```

## BeautyOutdoors
```
C:\Program Files (x86)\Steam\steamapps>findstr /s /a:e /i BeautyOut *.xml
common\RimWorld\Data\Core\Defs\Stats\Stats_Basics_General.xml:    <defName>BeautyOutdoors</defName>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Natural.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\TerrainDefs\Terrain_Water.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Misc\Various_Stone.xml:      <BeautyOutdoors>0</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Bases.xml:      <BeautyOutdoors>1</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Cave.xml:      <BeautyOutdoors>2</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Cave.xml:      <BeautyOutdoors>4</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Cultivated_Decorative.xml:      <BeautyOutdoors>14</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Cultivated_Decorative.xml:      <BeautyOutdoors>18</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Cultivated_Farm.xml:      <BeautyOutdoors>2</BeautyOutdoors>
common\RimWorld\Data\Core\Defs\ThingDefs_Plants\Plants_Wild_Swamp.xml:      <BeautyOutdoors>2</BeautyOutdoors>
... deleted several lines...
common\RimWorld\Data\Royalty\Defs\ThingDefs_Plants\Plants_Wild.xml:      <BeautyOutdoors>5</BeautyOutdoors>

C:\Program Files (x86)\Steam\steamapps>
```