# Search Functionality Implementation

## Features Implemented:

### 1. **Predictive Autocomplete Search**
- Real-time suggestions as users type
- Shows school name, code, and location
- Click to select from suggestions
- Autocomplete list styled with hover effects
- Displays top 8 matching results

### 2. **Global Schools Database** (`schools-data.js`)
Created a centralized database containing all 12 schools:
- Bataan Peninsula State University (BPSU)
- Polytechnic University of the Philippines (PUP - Bataan)
- Limay Polytechnic College (LPC)
- AMA AKO - ACLC College of Balanga
- Asia Pacific College of Advanced Studies (APCAS)
- Bataan Heroes Memorial College (HEROES)
- Colegio de San Juan de Letran (Letran - Bataan)
- College of Subic Montessori - Dinalupihan (CSM)
- Eastwoods Professional College of Science and Technology (EASTWOODS)
- Maritime Academy of Asia and the Pacific (MAAP)
- Microcity College of Business and Technology (MCBT)
- Philippine Women's University CDCEC - Bataan (PWU CDCEC)

### 3. **Search Bar Integration Across All Pages**
- **Home Page**: Search box with predictive autocomplete
  - "Start Exploring" button redirects to campus.html with search query
  - Autocomplete appears as user types school names
  
- **Campus Page**: Full search functionality
  - Autocomplete search
  - Filter by type (SUC, LUC, Private)
  - Filter by location (Bataan, Mariveles, Limay, Balanga City, Abucay, Dinalupihan)
  - Combined filtering works together
  - Supports URL parameters for search from home page
  
- **About Page**: Link to schools-data.js (for future expansion)
- **Contact Page**: Link to schools-data.js (for future expansion)

### 4. **Key Functions in schools-data.js**
- `initializeAutocomplete(searchInputId)`: Sets up autocomplete on any page
- `filterInstitutions()`: Global filtering function
- `searchAndRedirect()`: Redirects from home to campus with search term

### 5. **How It Works**
1. User types in search box on home or campus page
2. Autocomplete suggestions appear immediately
3. User can click a suggestion or continue typing
4. From home page, "Start Exploring" redirects to campus.html with the search term
5. Campus page loads with search results already filtered
6. Filters (type and location) work in combination with search

### 6. **Files Modified**
- ✅ `home.html` - Added autocomplete, search redirect to campus
- ✅ `campus.html` - Added autocomplete, filter integration, URL parameter handling
- ✅ `about.html` - Added script reference
- ✅ `contact.html` - Added script reference
- ✅ `schools-data.js` - New file with all school data and functions

## Testing Instructions:
1. Open home.html in a browser
2. Type in the search box - you'll see autocomplete suggestions
3. Click a school name or continue typing to filter
4. Click "Start Exploring" - it will take you to campus.html with your search
5. Campus page shows matching schools
6. Use filters to narrow down further
