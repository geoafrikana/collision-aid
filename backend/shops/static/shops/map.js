var map = L.map('map').setView([39, -95], 3);

L.tileLayer('http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}', {
    maxZoom: 18,
    attribution: 'Google Maps'
}).addTo(map);


const form  = document.getElementById('home-form');

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    
    const formData = new FormData();
    
    const zip_code = document.getElementById('zip_code').value
    const search_radius = document.getElementById('search_radius').value
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    formData.append('zip_code', zip_code);
    formData.append('search_radius', search_radius);


    const request = new Request (
        form.action,
        {method:'POST',
        headers: {'X-CSRFtoken': 
        csrftoken},
        mode: 'same-origin',
        body: formData
        
    })

    fetch(request)
    .then(x => x.text())
    .then(data => {
        data = JSON.parse(data);
        console.log(data)
        L.geoJSON(data, {
            style: {
                color: 'red'
            }

        }).bindPopup(layer=>`<b>Name:</b> ${layer.feature.properties.name}`).addTo(map)
    })
    

})




