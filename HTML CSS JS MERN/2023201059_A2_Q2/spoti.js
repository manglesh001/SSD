// Replace with your Spotify API credentials
const clientId = 'Client Id key';   // Replace with client Id key like ef45hj5jk-------------
const clientSecret = 'Client Secret key';   // Replace with client Secret key like r5h6kjdjj3j99395-------------

// Spotify API endpoints
const apiUrl = 'https://api.spotify.com/v1';
const newReleasesEndpoint = '/browse/new-releases';

// Function to fetch new releases from Spotify API
async function getNewReleases() {
    console.log('uiop');
    try {
        // Fetch an access token using your client ID and client secret
        const response = await fetch('https://accounts.spotify.com/api/token', {
            method: 'POST',
            headers: {
                'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret),
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'grant_type=client_credentials',
        });
console.log(JSON.stringify(response));
        if (!response.ok) {
            throw new Error('Failed to get access token');
        }

        const data = await response.json();
        const accessToken = data.access_token;

        // Fetch new releases using the access token
        const newReleasesResponse = await fetch(apiUrl + newReleasesEndpoint, {
            headers: {
                'Authorization': 'Bearer ' + accessToken,
            },
        });

        if (!newReleasesResponse.ok) {
            throw new Error('Failed to fetch new releases');
        }

        const newReleasesData = await newReleasesResponse.json();

        // Display new releases on the webpage
        const newReleasesContainer = document.getElementById('newReleases');
        newReleasesData.albums.items.forEach((release) => {
            const releaseCard = document.createElement('div');
            releaseCard.classList.add('col-md-4', 'mb-4');
            releaseCard.innerHTML = `
                <div class="card">
                    <img src="${release.images[0].url}" class="card-img-top" alt="${release.name}">
                    <div class="card-body">
                        <h5 class="card-title">${release.name}</h5>
                        <p class="card-text">${release.artists[0].name}</p>
                        <a class="card-text" target='_blank' href='${release.external_urls['spotify']}' >Play</p>
                    </div>
                </div>
            `;
            newReleasesContainer.appendChild(releaseCard);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the function to fetch and display new releases
// getNewReleases();

