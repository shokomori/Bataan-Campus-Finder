## Search & Autocomplete System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    schools-data.js                          │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ schoolsDatabase = [                                     ││
│  │   { name, code, type, location },                       ││
│  │   { ... } × 12 schools                                  ││
│  │ ]                                                       ││
│  │                                                          ││
│  │ Functions:                                              ││
│  │ • initializeAutocomplete(id)                            ││
│  │ • filterInstitutions()                                  ││
│  │ • searchAndRedirect()                                   ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
                            ↑
                    (imported by all pages)
                            
    ┌──────────────────────┬──────────────────────┐
    │                      │                      │
┌─────────────┐   ┌──────────────────┐   ┌──────────────┐
│  home.html  │   │  campus.html     │   │ about.html   │
│             │   │                  │   │  contact.html│
│ • Search    │   │ • Search         │   │              │
│   box with  │   │ • Autocomplete   │   │ (script      │
│   autocmplt │   │ • Filters (type, │   │  referenced) │
│             │   │   location)      │   │              │
│ • Start     │   │ • URL params     │   │              │
│   Exploring │   │   from home      │   │              │
│   button    │   │                  │   │              │
│   →campus   │   │                  │   │              │
└─────────────┘   └──────────────────┘   └──────────────┘
     │                    ▲
     │                    │
     │            (search result)
     └────────────────────┘

USER FLOW:
1. Home Page → Type school name → Autocomplete appears
2. Click school or "Start Exploring" → Go to Campus page with search
3. Campus page → Autocomplete + Filters + Results
4. Results update in real-time as user types or filters
```

## Autocomplete Features:
- **Trigger**: User types in search input
- **Display**: Top 8 matching results
- **Match**: School name or code (case-insensitive)
- **Selection**: Click suggestion → Fill input → Filter
- **Style**: White box with hover effect, positioned below search

## Filter Features:
- **Type Filter**: SUC, LUC, Private
- **Location Filter**: Bataan, Mariveles, Limay, Balanga City, Abucay, Dinalupihan
- **Combined**: All filters work together
- **Search + Filters**: Search term + Type + Location all apply simultaneously

## Database (12 Schools):
1. BPSU - Bataan Peninsula State University (SUC, Bataan)
2. PUP - Polytechnic University of the Philippines (SUC, Mariveles)
3. LPC - Limay Polytechnic College (LUC, Limay)
4. ACLC - AMA AKO - ACLC College of Balanga (Private, Balanga City)
5. APCAS - Asia Pacific College of Advanced Studies (Private, Balanga City)
6. HEROES - Bataan Heroes Memorial College (Private, Balanga City)
7. Letran - Colegio de San Juan de Letran (Private, Abucay)
8. CSM - College of Subic Montessori - Dinalupihan (Private, Dinalupihan)
9. EASTWOODS - Eastwoods Professional College (Private, Bataan)
10. MAAP - Maritime Academy of Asia and the Pacific (Private, Mariveles)
11. MCBT - Microcity College of Business and Technology (Private, Balanga City)
12. PWU CDCEC - Philippine Women's University (Private, Balanga City)
