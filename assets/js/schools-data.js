// Schools Database
const schoolsDatabase = [
    { name: "Bataan Peninsula State University", code: "BPSU", type: "SUC", location: "Bataan" },
    { name: "Polytechnic University of the Philippines", code: "PUP - Bataan", type: "SUC", location: "Mariveles, Bataan" },
    { name: "Limay Polytechnic College", code: "LPC", type: "LUC", location: "Limay, Bataan" },
    { name: "AMA AKO - ACLC College of Balanga", code: "ACLC - Bataan", type: "Private", location: "Balanga City, Bataan" },
    { name: "Asia Pacific College of Advanced Studies", code: "APCAS", type: "Private", location: "Balanga City, Bataan" },
    { name: "Bataan Heroes Memorial College", code: "HEROES", type: "Private", location: "Balanga City, Bataan" },
    { name: "Colegio de San Juan de Letran", code: "Letran - Bataan", type: "Private", location: "Abucay, Bataan" },
    { name: "College of Subic Montessori - Dinalupihan", code: "CSM - Dinalupihan", type: "Private", location: "Dinalupihan, Bataan" },
    { name: "Eastwoods Professional College of Science and Technology", code: "EASTWOODS", type: "Private", location: "Bataan" },
    { name: "Maritime Academy of Asia and the Pacific", code: "MAAP", type: "Private", location: "Mariveles, Bataan" },
    { name: "Microcity College of Business and Technology", code: "MCBT", type: "Private", location: "Balanga City, Bataan" },
    { name: "Philippine Women's University CDCEC - Bataan", code: "PWU CDCEC", type: "Private", location: "Balanga City, Bataan" }
];

// Initialize autocomplete
function initializeAutocomplete(searchInputId) {
    const searchInput = document.getElementById(searchInputId);
    if (!searchInput) return;

    // Create autocomplete container
    const autocompleteContainer = document.createElement('div');
    autocompleteContainer.id = 'autocomplete-suggestions';
    autocompleteContainer.style.cssText = `
        position: absolute;
        background: white;
        border: 1px solid #dee2e6;
        border-top: none;
        border-radius: 0 0 10px 10px;
        max-height: 300px;
        overflow-y: auto;
        width: 100%;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        display: none;
        z-index: 1001;
        top: 100%;
        left: 0;
    `;

    // Make search box container relative for autocomplete positioning
    const searchBox = searchInput.parentElement;
    searchBox.style.position = 'relative';
    searchBox.appendChild(autocompleteContainer);

    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase().trim();
        
        if (searchTerm.length === 0) {
            autocompleteContainer.style.display = 'none';
            return;
        }

        // Filter schools based on search term
        const filteredSchools = schoolsDatabase.filter(school =>
            school.name.toLowerCase().includes(searchTerm) ||
            school.code.toLowerCase().includes(searchTerm)
        );

        if (filteredSchools.length === 0) {
            autocompleteContainer.style.display = 'none';
            return;
        }

        // Populate autocomplete suggestions
        autocompleteContainer.innerHTML = '';
        filteredSchools.slice(0, 8).forEach(school => {
            const suggestionItem = document.createElement('div');
            suggestionItem.style.cssText = `
                padding: 1rem;
                border-bottom: 1px solid #f1f3f5;
                cursor: pointer;
                transition: background-color 0.2s;
                display: flex;
                justify-content: space-between;
                align-items: center;
            `;
            
            suggestionItem.innerHTML = `
                <div>
                    <div style="font-weight: 600; color: #2542ff;">${school.name}</div>
                    <div style="font-size: 0.85rem; color: #666;">${school.code} • ${school.location}</div>
                </div>
            `;

            suggestionItem.addEventListener('mouseenter', function() {
                this.style.backgroundColor = '#f8f9fa';
            });

            suggestionItem.addEventListener('mouseleave', function() {
                this.style.backgroundColor = 'transparent';
            });

            suggestionItem.addEventListener('click', function() {
                searchInput.value = school.name;
                autocompleteContainer.style.display = 'none';
                // Trigger filter
                filterInstitutions();
            });

            autocompleteContainer.appendChild(suggestionItem);
        });

        autocompleteContainer.style.display = 'block';
    });

    // Hide autocomplete when clicking outside
    document.addEventListener('click', function(e) {
        if (e.target !== searchInput && !autocompleteContainer.contains(e.target)) {
            autocompleteContainer.style.display = 'none';
        }
    });
}

// Global filter function for institutions
function filterInstitutions() {
    const searchInput = document.getElementById('searchInput');
    const typeFilter = document.getElementById('typeFilter');
    const locationFilter = document.getElementById('locationFilter');
    const institutionsGrid = document.getElementById('institutionsGrid');

    if (!searchInput || !institutionsGrid) return;

    const searchTerm = searchInput.value.toLowerCase();
    const typeValue = typeFilter ? typeFilter.value : '';
    const locationValue = locationFilter ? locationFilter.value : '';
    const cards = institutionsGrid.getElementsByClassName('institution-card');

    Array.from(cards).forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();
        const code = card.querySelector('.institution-code').textContent.toLowerCase();
        const badge = card.getAttribute('data-type') || '';
        const location = card.getAttribute('data-location') || '';

        const matchesSearch = !searchTerm || title.includes(searchTerm) || code.includes(searchTerm);
        const matchesType = !typeValue || badge === typeValue;
        const matchesLocation = !locationValue || location.includes(locationValue);

        if (matchesSearch && matchesType && matchesLocation) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Search redirect from home page
function searchAndRedirect() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput && searchInput.value.trim().length > 0) {
        window.location.href = 'campus.html?search=' + encodeURIComponent(searchInput.value);
    }
}

// Auto-inject responsive Google Maps iframe into pages that have a `.campus-map` container.
(function injectCampusMaps(){
    try {
        document.querySelectorAll('.campus-header').forEach(el=>el.style.position='relative');
        document.querySelectorAll('.campus-map').forEach(el=>{
            el.style.overflow='hidden';
            el.style.display='block';
            el.style.boxShadow='0 1px 6px rgba(0,0,0,0.08)';
            if(el.querySelector('iframe')) return;
            var titleEl = document.querySelector('.campus-info h1') || document.querySelector('.school-header-info h1') || document.querySelector('h1');
            var q = titleEl ? titleEl.textContent.trim() : document.title.replace(/ - Campus Details/i, '');
            if(!q) return;
            var src = 'https://www.google.com/maps?q=' + encodeURIComponent(q + ', Bataan, Philippines') + '&output=embed';
            el.innerHTML = '<iframe src="'+src+'" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>' +
                '<p style="font-size:0.85rem;color:#666;margin-top:0.5rem;">If the map does not load, <a href="https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(q+' Bataan, Philippines')+'" style="color:#2542ff;">open in Google Maps</a>.</p>';
        });
    } catch(e) {
        console.warn('Map injector error', e);
    }
})();
