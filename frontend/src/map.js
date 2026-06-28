import L from 'leaflet';

// Initialize the map (centered on a default location)
const map = L.map('map').setView([20.5937, 78.9629], 5); // Default to India

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// We'll update this map dynamically later when the Spatial Agent streams coordinates!
