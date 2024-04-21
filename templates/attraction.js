// Function to load attraction data and display in sidebar
function loadAttractions() {
    fetch('/api/v1/attractions') // Assuming '/attractions' is the endpoint to fetch attractions from the server
        .then(response => response.json())
        .then(data => {
            const attractionsContainer = document.getElementById('attractions');
            attractionsContainer.innerHTML = ''; // Clear previous content

            data.forEach(attraction => {
                const attractionElement = document.createElement('div');
                attractionElement.classList.add('attraction');
                attractionElement.innerHTML = `
                    <img src="${attraction.image_src}" alt="${attraction.name}">
                    <p>${attraction.name}</p>
                `;
                attractionElement.addEventListener('click', () => {
                    loadAttractionDetails(attraction);
                });
                attractionsContainer.appendChild(attractionElement);
            });
        })
        .catch(error => console.error('Error loading attractions:', error));
}


// Function to load attraction details and display more information
function loadAttractionDetails(attraction) {
    // Assuming there's a separate endpoint to fetch attraction details
    fetch(`/api/v1/attractions/${attraction.id}`)
        .then(response => response.json())
        .then(details => {
            // Display attraction details however you like (e.g., in a modal or expanded view)
            console.log('Attraction Details:', details);
        })
        .catch(error => console.error('Error loading attraction details:', error));
}

// Load attractions when the page is loaded
window.addEventListener('load', loadAttractions);
