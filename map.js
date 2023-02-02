var map = L.map('map').setView([39, -95], 4);

L.tileLayer('http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}', {
    maxZoom: 18,
    attribution: 'Google Maps'
}).addTo(map);