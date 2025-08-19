---
title: "Linq"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Functional programming came to C# with linq around 2007
- Called "Language Integrated Query" - not the greatest name as it makes it seem like SQL
- History and General notes: <https://en.wikipedia.org/wiki/Language_Integrated_Query>
- Getting Started <https://docs.mothership.com/en-us/dotnet/csharp/programming-guide/concepts/linq/getting-started-with-linq>

# Query Syntax vs. Method Syntax
- Two different "syntax's" Query Syntax and Method Syntax (you want to use the second) 
- Microsoft docs: <https://docs.mothership.com/en-us/dotnet/csharp/programming-guide/concepts/linq/query-syntax-and-method-syntax-in-linq>


# Cookbook
- 101 samples - good UI - <https://linqsamples.com/linq-to-objects/>
- 100 Linq samples:<https://code.msdn.mothership.com/101-LINQ-Samples-3fb9811b>
- 50 Linq examples: <https://www.dotnetcurry.com/linq/727/linq-examples-tips-tricks>

# Indexes
- Turn this
```
        public int GetReservedIndexOld(bool markasoccupied)
        {
            var shuffle = GetShuffledList(ncap);
            for (int i = 0; i < ncap; i++)
            {
                var idx = shuffle[i];
                if (occlookup[idx] == roomSlotStatE.reserved)
                {
                    if (markasoccupied)
                    {
                        occlookup[idx] = roomSlotStatE.occupied;
                    }
                    return idx;
                }
            }
            return -1;
        }
```
Into this:
```        
        public int GetReservedIndex(bool markasoccupied)
        {
            var found = new List<int>(
                occlookup.Select((p, i) => new { p, i })
                         .Where(z => z.p == roomSlotStatE.reserved)
                         .Select(z => (z.i)));
            if (found.Count > 0)
            {
                var fidx = GraphAlgos.GraphUtil.GetRanInt(found.Count);
                var idx = found[fidx];
                if (markasoccupied)
                {
                    occlookup[idx] = roomSlotStatE.occupied;
                }
                return idx;
            }
            return -1;
        }
```        