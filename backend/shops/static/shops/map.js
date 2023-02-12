var map = L.map('map').setView([39, -95], 3);

const osm = L.tileLayer('http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}', {
    maxZoom: 18,
    attribution: 'Google Maps'
})

osm.name = 'googleBaseMap'
osm.addTo(map);





const form = document.getElementById('home-form');

form.addEventListener('submit', (e) => {
    e.preventDefault()

    const formData = new FormData();

    const zip_code = document.getElementById('zip_code').value
    const search_radius = document.getElementById('search_radius').value
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    formData.append('zip_code', zip_code);
    formData.append('search_radius', search_radius);


    const request = new Request(
        form.action,
        {
            method: 'POST',
            headers: {
                'X-CSRFtoken':
                    csrftoken
            },
            mode: 'same-origin',
            body: formData

        })

    fetch(request)
        .then(res => res.json())
        .then((data) => {
            const messageBox = document.getElementById('alert')
            messageBox.className = ''
            messageBox.classList.add('mx-3', 'py-2', 'alert')
            document.getElementById('table-div').style.display = 'none'
            
            map.eachLayer((layer) => {
                if (!(layer.name == 'googleBaseMap')) {
                    layer.remove();
                }
            })
            if (data.code == 1) {
                messageBox.classList.add('alert-danger')
                messageBox.innerText = 'Zip code not found.'
            }
            else if (data.code == 2) {
                messageBox.classList.add('alert-warning')
                messageBox.innerText = 'No shop found.'

            }
            else {
                let gj = JSON.parse(data['data'])
                messageBox.classList.add('alert-success')
                messageBox.innerText = `Your query return ${gj.features.length} shops`

                let geoJSONLayer = L.geoJSON(gj, {
                    style: { color: 'red' }

                }).bindPopup(layer => `<b>Name:</b> ${layer.feature.properties.business_name}`)

                geoJSONLayer.addTo(map)
                map.fitBounds(geoJSONLayer.getBounds());

                let table = data['table']

                let highest_values = table['highest']
                let lowest_values = table['lowest']
                let average_values = table['average']

                Array.from(document.getElementById('highest').children)
                .map((td, idx, _) => {
                    if (idx != 0){
                        td.innerHTML = `$${highest_values[idx-1]}`
                    }
                })

                Array.from(document.getElementById('lowest').children)
                .map((td, idx, _) => {
                    if (idx != 0){
                        td.innerHTML = `$${lowest_values[idx-1]}`
                    }
                })

                Array.from(document.getElementById('average').children)
                .map((td, idx, _) => {
                    if (idx != 0){
                        td.innerHTML = `$${average_values[idx-1]}`
                    }
                })

                document.getElementById('table-div').style.display = 'block'




                
            }

            messageBox.style.display = 'block'
        })
})




